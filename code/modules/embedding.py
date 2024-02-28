# Third-party Libraries
import torch
from tqdm.auto import tqdm

# Path to model.
# Source(s):
# - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# - https://www.sbert.net/


def store_to_device(embeddings: dict, device: str = "cpu") -> dict:
    """store_to_device.

    Changes the device for running embeddings.

    Parameters
    ----------
    embeddings : dict
        Embedding dictionary from tokenizer.
    device : str, optional
        Device to declare (i.e. "cpu" or "gpu").

    Returns
    -------
    dict
        Embedding dictionary from tokenizer.

    Example
    -------
    >>> embeddings = tokenizer(text, padding="max_length", truncation=True, max_length=256, return_tensors="pt")
    >>> cos_score_tensor = embedding.store_to_device(embeddings)
    """
    embeddings = {key: value.to(torch.device(device)) for key, value in embeddings.items()}
    return embeddings


def get_model_output(model, encoded_input: dict):
    """get_model_output.

    Compute token embeddings.

    Parameters
    ----------
    model : transformers.models.bert.modeling_bert.BertModel
        Transformers BERT model.
    encoded_input : dict
        Embedding dictionary from tokenizer.

    Returns
    -------
    transformers.modeling_outputs.BaseModelOutputWithPoolingAndCrossAttentions
        BERT model output.

    Example
    -------
    >>> output = embedding.get_model_output(model, embeddings)
    """
    with torch.no_grad():
        model_output = model(**encoded_input)
    return model_output


def mean_pooling(model_output, attention_mask):
    """mean_pooling.

    Take attention mask into account for correct averaging.
    This also helps reduce the number of numpy array dimensions.

    Parameters
    ----------
    model_output : transformers.models.bert.modeling_bert.BertModel
        Transformers BERT model.
    attention_mask : torch.Tensor
        Attention mask from model.

    Returns
    -------
    torch.Tensor
        Torch tensors.

    Example
    -------
    >>> mean = embedding.mean_pooling(model_output, embeddings["attention_mask"])
    """
    # Get BaseModelOutputWithPoolingAndCrossAttentions.
    token_embeddings = model_output[0]

    # Expand torch tensors.
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()

    # Calculate the sum of the torch embeddings.
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)

    # Mask the sum of the embeddings up to the max_text_length
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    # Get the mean of the embeddings.
    mean = sum_embeddings / sum_mask

    return mean


def get_embedding_batch(sentences: list, model, tokenizer, max_text_length: int = 512, device: str = "cpu"):
    """get_embedding_batch.

    Get embedding of batch of text.

    Parameters
    ----------
    sentences : list
        List of sentences.
    model : transformers.models.bert.modeling_bert.BertModel
        Transformers BERT model.
    tokenizer : transformers.models.bert.tokenization_bert_fast.BertTokenizerFast
        Transformers BERT tokenizer.
    max_text_length : int, optional
        _description_, by default 512
    device : str, optional
        Device to declare (i.e. "cpu" or "gpu").

    Returns
    -------
    pytorch
        Pytorch embeds.

    Example
    -------
    >>> embed_batch = embedding.get_embedding_batch(sentences, model, tokenizer)
    """
    # Preprocessing text into tokens and tokens into tensors.
    # Truncation set to True to ensure text is no longer than max_length.
    encoded_input = tokenizer(sentences, padding="max_length", truncation=True, max_length=max_text_length, return_tensors="pt")  # Pytorch version

    # encoded_input_dev = {key: value.to(DEVICE) for key, value in encoded_input.items()}
    encoded_input_dev = store_to_device(encoded_input, device)

    # Run the model based on the passed in tokens.
    output = get_model_output(model, encoded_input_dev)

    # Get mean pooling
    embed_mean = mean_pooling(output, encoded_input_dev["attention_mask"]).cpu()

    # Get the norm value.
    embed_lens = torch.norm(embed_mean, dim=-1, keepdim=True)

    # Get the average embeddings between mean and norm.
    embed_batch = embed_mean / embed_lens

    return embed_batch


def get_embeddings(sentences: list, model, tokenizer, batch_size: int = 32, max_text_length: int = 512, device: str = "cpu"):
    """get_embeddings.

    Get embedding of text.

    Parameters
    ----------
    sentences : list
        List of sentences.
    model : transformers.models.bert.modeling_bert.BertModel
        Transformers BERT model.
    tokenizer : transformers.models.bert.tokenization_bert_fast.BertTokenizerFast
        Transformers BERT tokenizer.
    batch_size : int, optional
        _description_, by default 32
    max_text_length : int, optional
        _description_, by default 512
    device : str, optional
        Device to declare (i.e. "cpu" or "gpu").

    Returns
    -------
    pytorch
        Pytorch embeds.

    Example
    -------
    >>> embeds_list = embedding.get_embeddings(sentences, model, tokenizer)
    """
    with torch.no_grad():
        embeds_list = []

        for i in tqdm(range(0, len(sentences), batch_size)):
            embeds_list.append(get_embedding_batch(sentences[i:i + batch_size], model, tokenizer, max_text_length, device))

    return torch.cat(embeds_list)


# def get_expanded_context(x):

#     context = x["Sentence"]
#     text_nlp = x["NLP_Text"]

#     # Get the length of the sentence context.
#     expanded_context_len = len(TOKENIZER(context.text, max_length=MAX_TEXT_LENGTH)["input_ids"])  # Warning: Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy.
#     context_sent_id = 0

#     # Loop through the nlp text to collect the full text.
#     # Get the id number of the sentence from the full text.
#     for i, s in enumerate(list(text_nlp.sents)):

#         if s.text == context.text:
#             context_sent_id = 1
#             break

#     # Condition to get expanded context for sentence.
#     if expanded_context_len < MAX_TEXT_LENGTH:

#         # Condition for the first sentence?
#         if context_sent_id == 0 and len(list(text_nlp.sents)) > 1:
#             context_sent_id += 1

#         # Context sentences.
#         sentence_before = list(text_nlp.sents)[context_sent_id-1].text
#         current_sentence = list(text_nlp.sents)[context_sent_id].text
#         # sentence_after = list(text_nlp.sents)[context_sent_id+1].text

#         # Store expanded context and get new length.
#         expanded_context = sentence_before + current_sentence
#         expanded_context_len = en(TOKENIZER(expanded_context, max_length=MAX_TEXT_LENGTH)["input_ids"])

#         if expanded_context_len < MAX_TEXT_LENGTH:

#             # Condition for last sentence?
#             if context_sent_id == len(list(text_nlp.sents))-1 and len(list(text_nlp.sents)) > 2:
#                 context_sent_id -= 1

#             try:
#                 if len(list(text_nlp.sents)) > 2:
#                     expanded_context = list(text_nlp.sents)[context_sent_id-1].text + list(text_nlp.sents)[context_sent_id].text + list(text_nlp.sents)[context_sent_id+1].text
#             except:
#                 print("Broken here")
#                 print(context_sent_id)
#                 print(len(list(text_nlp.sents)))
#                 print(context.text)
#                 expanded_context = list(text_nlp.sents)[context_sent_id-1].text + list(text_nlp.sents)[context_sent_id].text + list(text_nlp.sents)[context_sent_id+1].text

#     else:
#         expanded_context = context.text

#     return expanded_context
