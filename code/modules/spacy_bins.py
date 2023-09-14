# Standard Libraries
import os
import glob

# Third-party Libraries
from tqdm.auto import tqdm
from spacy.tokens import DocBin

CHUNK = 5000


def create_bins(spacy_path: str, doc_list: list, nlp) -> None:
    """create_bins.

    Save spacy text to disk for future use.

    Parameters
    ----------
    spacy_path : str
        Path to store to disk.
    doc_list : list
        List of text to store.
    nlp : _type_
        SpaCy Object.

    Returns
    -------
    None
    """
    # Create path if it doesn't exist.
    if not os.path.exists(spacy_path):
        os.makedirs(spacy_path)

    # Start from here if generating spaCy data.
    doc_bin = DocBin()
    text_to_nlp = {}

    for i, text in tqdm(enumerate(doc_list), total=len(doc_list), desc="Creating spacy bins"):

        # Counter for CHUNK.
        i += 1

        # Convert to spacy nlp text.
        spacy_text = nlp(text[:nlp.max_length])

        # Store to a dictionary.
        text_to_nlp[text[:nlp.max_length]] = spacy_text

        # Add spacy text to bin.
        doc_bin.add(spacy_text)

        if i % CHUNK == 0:
            doc_bin = DocBin()
            doc_bin.to_disk(os.path.join(spacy_path, "spacy_disk_chunk_{}.spacy".format(i)))

    return None


def get_bins(spacy_path: str, nlp) -> dict:
    """get_bins.

    Get spacy text from bins, either previously stored or newly created.

    Parameters
    ----------
    spacy_path : str
        Path to store to disk.
    nlp : _type_
        SpaCy Object.

    Returns
    -------
    dict
        A dictionary of text: token pairs.
    """
    docs = []

    # Object to get spacy bins.
    doc_bin = DocBin()

    for i in glob.glob(spacy_path + "\\*.spacy"):

        # Start from here if loading spacy data.
        # Note: This stores text from spacy bin. No need to store to a variable or else this will create duplicates in data returned.
        doc_bin.from_disk(i)

        # Store bin objects to a list.
        docs = docs + list(doc_bin.get_docs(nlp.vocab))

    # Note: text_to_nlp!=sc_to_nlp2, but the keys and values.to_json() are equivalent, which is good enough.
    text_to_nlp = {}

    for doc in tqdm(docs, total=len(docs), desc="Get existing spacy bins."):
        text_to_nlp[doc.text] = doc

    return text_to_nlp


def update_bins(spacy_path: str, doc_list: list, nlp, text_to_nlp: dict) -> dict:
    """update_bins.

    Update spacy bins if new text is found.

    Parameters
    ----------
    spacy_path : str
        Path to store to disk.
    doc_list : list
        List of text to store.
    nlp : _type_
        SpaCy Object.
    text_to_nlp : dict
        A dictionary of text: token pairs.

    Returns
    -------
    dict
        A dictionary of text: token pairs.
    """
    doc_bin_update = DocBin()

    for i, text in tqdm(enumerate(doc_list), total=len(doc_list), desc="Updating spacy bins"):

        # Counter for CHUNK.
        i += 1

        # Condition to check if new docs are in the spacy bins list.
        # If not, then add them to the dictionary.
        if text[:nlp.max_length] not in text_to_nlp:

            # Debug statement.
            # print(text, "NOT IN")

            # Convert to spacy nlp text.
            spacy_text = nlp(text[:nlp.max_length])

            # Store to a dictionary.
            text_to_nlp[text[:nlp.max_length]] = spacy_text

        else:

            # Debug statement.
            # print(text, "IS IN")

            # Lookup saved spacy representation of the text.
            spacy_text = text_to_nlp[text[:nlp.max_length]]

        # Add spacy text to bin.
        doc_bin_update.add(spacy_text)

        if i % CHUNK == 0:
            doc_bin_update = DocBin()
            doc_bin_update.to_disk(os.path.join(spacy_path, "spacy_disk_chunk_{}.spacy".format(i)))

    doc_bin_update.to_disk(os.path.join(spacy_path, "spacy_disk_chunk_{}.spacy".format(i)))

    return text_to_nlp
