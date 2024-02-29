# Standard Libraries
import os
import glob

# Third-party Libraries
from tqdm.auto import tqdm
from spacy.tokens import DocBin

CHUNK = 5000  # Limit the number of spacy objects to store in spacy bin.


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
            doc_bin.to_disk(os.path.join(spacy_path, f"spacy_disk_chunk_{i}.spacy"))
            doc_bin = DocBin()

    doc_bin.to_disk(os.path.join(spacy_path, f"spacy_disk_chunk_{i}.spacy"))

    return None


def get_bins(spacy_path: str, nlp) -> dict:
    """get_bins.

    Get spacy text from bins, either previously stored or newly created.

    Parameters
    ----------
    spacy_path : str
        Path to store to disk.
    nlp : spacy.lang.en.English
        SpaCy Object.

    Returns
    -------
    dict
        A dictionary of text: token pairs.

    Example
    -------
    >>> text_to_nlp = spacy_bins.get_bins(spacy_path, nlp)
    """
    docs = []
    unique_docs = []

    # Object to get spacy bins.
    doc_bin = DocBin()

    # All spacy files.
    spacy_files = glob.glob(spacy_path + r"\*.spacy")

    for i in tqdm(spacy_files, total=len(spacy_files)):

        # Start from here if loading spacy data.
        # Note: This stores text from spacy bin. No need to store to a variable or else this will create duplicates in data returned.
        doc_bin.from_disk(i)

        # Store bin objects to a list.
        # Condition if more than one spacy file is found and how to store the spacy objects to a list.
        if len(spacy_files) > 1:
            docs.extend(list(doc_bin.get_docs(nlp.vocab)))
        else:
            docs = list(doc_bin.get_docs(nlp.vocab))  # + docs

        # This removes duplicates from doc list.
        # Source(s): https://stackoverflow.com/questions/62426331/i-have-a-problem-removing-duplicates-from-a-list
        unique_docs = list({a.__repr__(): a for a in docs}.values())

        # # Debug
        # print(i)
        # print("Ori", list(doc_bin.get_docs(nlp.vocab)))
        # print("\n")
        # print("Uni", unique_docs)
        # print("="*120)

    # Note: text_to_nlp!=sc_to_nlp2, but the keys and values.to_json() are equivalent, which is good enough.
    text_to_nlp = {}

    # Loop through the unique list of spacy objects to create the text: token dictionary.
    for doc in tqdm(unique_docs, total=len(unique_docs), desc="Get existing spacy bins."):
        text_to_nlp[doc.text] = doc

    return text_to_nlp


def update_bins(spacy_path: str, doc_list_diff: list, nlp, text_to_nlp: dict) -> dict:
    """update_bins.

    Update spacy bins if new text is found.

    Parameters
    ----------
    spacy_path : str
        Path to store to disk.
    doc_list_diff : list
        List of text to store in doc that isn't in text_to_nlp.
    nlp : spacy.lang.en.English
        SpaCy Object.
    text_to_nlp : dict
        A dictionary of text: token pairs.

    Returns
    -------
    dict
        A dictionary of text: token pairs.

    Example
    -------
    >>> for i in doc_list:
    ...     if i not in text_to_nlp.keys():
    ...         doc_list_diff.append(i)
    >>> if doc_list_diff:
    ...     text_to_nlp = spacy_bins.update_bins(spacy_path, doc_list_diff, nlp, text_to_nlp)
    """
    doc_bin_update = DocBin()
    counter = 0

    # First loop through the doc_list_diff to get the difference of text stored in doc compared to text_to_nlp.
    for doc in tqdm(doc_list_diff, total=len(doc_list_diff), desc="Updating text_to_nlp with new text"):

        if doc[:nlp.max_length] not in text_to_nlp:

            # Convert to spacy nlp text.
            spacy_text = nlp(doc[:nlp.max_length])

            # Store to a dictionary.
            text_to_nlp[doc[:nlp.max_length]] = spacy_text

        else:

            # Lookup saved spacy representation of the text.
            spacy_text = text_to_nlp[doc[:nlp.max_length]]

    # Then loop through text_to_nlp dictionary and write new files.
    # Using this method to ensure we are updating the file with the total values.
    for value in tqdm(text_to_nlp.values(), total=len(text_to_nlp), desc="Updating spacy bins total"):

        # Add spacy text to bin.
        doc_bin_update.add(value)

        # Counter for CHUNK.
        counter += 1

        # Store value for module.
        split = counter % CHUNK

        # If CHUNK value is reached, split off and store to another file.
        if split == 0:

            # # Debug
            # print(f"Writing {counter}", os.path.join(spacy_path, f"spacy_disk_chunk_{counter}.spacy"))

            doc_bin_update.to_disk(os.path.join(spacy_path, f"spacy_disk_chunk_{counter}.spacy"))

            # Condition to prevent chunk 50 from being overwritten to empty.
            if len(text_to_nlp) > CHUNK:
                doc_bin_update = DocBin()

    # Write out final file.
    # NOTE: Ignore variable unbound warning, this method prevents multiple files being written for each chunk.
    # This way keeps the files grouped by CHUNK.
    if split > 0:

        # # Debug
        # print(f"Writing {counter}", os.path.join(spacy_path, f"spacy_disk_chunk_{counter}.spacy"))
        doc_bin_update.to_disk(os.path.join(spacy_path, f"spacy_disk_chunk_{counter}.spacy"))

    else:

        # # Debug
        # print(f"Writing {CHUNK}", os.path.join(spacy_path, f"spacy_disk_chunk_{CHUNK}.spacy"))
        doc_bin_update.to_disk(os.path.join(spacy_path, f"spacy_disk_chunk_{CHUNK}.spacy"))

    return text_to_nlp
