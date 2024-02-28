# Standard Libraries
import os

# Third-party Libraries
import torch

from .embedding import get_embeddings


def save_embeds(pytorch_path: str, text: list, sent_embed=None, model=None, tokenizer=None, file: str = "file") -> dict:
    """save_embeds.

    Save the embeddings to reduce compute time in the future.
    Map them to the original string in a list.

    Parameters
    ----------
    pytorch_path : str
        The path to save the pytorch embeds.
    text : list
        A list of sentences.
    sent_embed : pytorch, optional
        Pytorch embeds.
    model : transformers.models.bert.modeling_bert.BertModel, optional
        Transformers BERT model.
    tokenizer : transformers.models.bert.tokenization_bert_fast.BertTokenizerFast, optional
        Transformers BERT tokenizer.
    file : str, optional
        The file name to save it under.

    Returns
    -------
    dict
        A dictionary of the sentences mapped to their embeddings.

    Example
    -------
    >>> embeds_list = embedding.get_embeddings(sentences, model, tokenizer)  # For manual saving of embeddings.
    >>> manual_embeds_dict = pytorch_embeds.save_embeds(pytorch_path=pytorch_path, text=sentences, sent_embed=embeds_list, file="file")  # For manual saving of embeddings.
    >>> auto_embeds_dict = pytorch_embeds.save_embeds(pytorch_path=pytorch_path, text=sentences, model=model, tokenizer=tokenizer, file="file")  # For automatic saving of embeddings.
    """
    # Create path if it doesn't exist.
    if not os.path.exists(pytorch_path):
        os.makedirs(pytorch_path)

    embeds_dict = {}

    if sent_embed is None:
        print("Automatically create embeddings.")
        sent_embed = get_embeddings(text, model, tokenizer)

    # Map the embeddings to the sentence and store to a dictionary.
    for s, e in zip(text, sent_embed):
        embeds_dict[s] = e

    saved_file = os.path.join(pytorch_path, f"embeddings_{file}.pth")

    # Save embeddings file.
    torch.save(embeds_dict, saved_file)

    # Only returning if saving in the same session.
    return embeds_dict


def load_embeds(pytorch_path: str, file: str = "file") -> dict:
    """load_embeds.

    Load the embeddings from the drive to reduce compute time in the future.

    Parameters
    ----------
    pytorch_path : str
        The path to save the pytorch embeds.
    file : str, optional
        The file name to save it under.

    Returns
    -------
    dict
        A dictionary of the sentences mapped to their embeddings.

    Example
    -------
    >>> embeds_dict = pytorch_embeds.load_embeds(pytorch_path)
    """
    saved_file = os.path.join(pytorch_path, f"embeddings_{file}.pth")

    embeds_dict = torch.load(saved_file)

    return embeds_dict


def check_embeddings(pytorch_path: str, text: list, sent_embed=None, model=None, tokenizer=None, file: str = "file") -> dict:
    """check_embeddings.

    This method checks the embeddings from sentences and look for new
    embeddings compared to the combined embeddings file.

    Parameters
    ----------
    pytorch_path : str
        The path to save the pytorch embeds.
    text : list
        A list of sentences.
    sent_embed : pytorch, optional
        Pytorch embeds.
    model : transformers.models.bert.modeling_bert.BertModel, optional
        Transformers BERT model.
    tokenizer : transformers.models.bert.tokenization_bert_fast.BertTokenizerFast, optional
        Transformers BERT tokenizer.
    file : str, optional
        The file name to save it under.

    Returns
    -------
    dict
        A dictionary of the new embedded sentences.

    Example
    -------
    >>> embeds_list = embedding.get_embeddings(sentences, model, tokenizer)  # For manual saving of embeddings.
    >>> manual_embeds_dict = pytorch_embeds.check_embeddings(pytorch_path=pytorch_path, text=sentences, sent_embed=embeds_list, file="file")  # For manual saving of embeddings.
    >>> auto_embeds_dict = pytorch_embeds.check_embeddings(pytorch_path=pytorch_path, text=sentences, model=model, tokenizer=tokenizer, file="file")  # For automatic saving of embeddings.
    """
    sents_dict = {}
    diff_dict = {}

    # Get the associated embeddings for the sentences.
    if sent_embed is None:
        print("Automatically create embeddings.")
        sent_embed = get_embeddings(text, model, tokenizer)

    # Store sentences: embeddings to a dictionary.
    for s, e in zip(text, sent_embed):
        sents_dict[s] = e

    saved_file = os.path.join(pytorch_path, f"embeddings_{file}.pth")

    # Load current embeddings.
    embeds_dict = torch.load(saved_file)

    # Get the difference between the new embeddings and the stored embeddings.
    for i, j in sents_dict.items():
        if i not in embeds_dict.keys():
            diff_dict[i] = j

    return diff_dict


def update_embeds(pytorch_path: str, diff_dict: dict, file: str = "file") -> dict:
    """update_embeds.

    Method to update the combined embeddings file.

    Parameters
    ----------
    pytorch_path : str
        The path to save the combined embeds.
    diff_dict : dict
        A dictionary of sentences: embeddings pairs of the difference between the main combined file.
    file : str, optional
        The file name to save it under.

    Returns
    -------
    dict
        A dictionary of the updated embedded sentences.

    Example
    -------
    >>> embeds_dict = pytorch_embeds.update_embeds(pytorch_path=pytorch_path, diff_dict=diff_dict)
    """
    # Create path if it doesn't exist.
    if not os.path.exists(pytorch_path):
        os.makedirs(pytorch_path)

    saved_file = os.path.join(pytorch_path, f"embeddings_{file}.pth")

    embeds_dict = torch.load(saved_file)
    print(len(embeds_dict))

    embeds_dict.update(diff_dict)
    print(len(embeds_dict))

    torch.save(embeds_dict, saved_file)

    return embeds_dict
