# Standard Libraries
import os

# Third-party Libraries
import torch
from tqdm.auto import tqdm
from transformers import AutoTokenizer, AutoModel

# Path to model.
# Source(s):
# - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# - https://www.sbert.net/

# BERT_MODEL_PATH = os.path.abspath("sentence-transformers/all-MiniLM-L6-v2")
TOKENIZER = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
MODEL = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
BATCH_SIZE = 32
MAX_TEXT_LENGTH = 256
DEVICE = torch.device("cpu")

# NOTE: May potentially be updated.


def _mean_pooling(model_output, attention_mask):

    # Get BaseModelOutputWithPoolingAndCrossAttention.
    token_embeddings = model_output[0]

    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()

    mean = torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    return mean


def _get_embedding_batch(sentences: list) -> torch.FloatTensor:

    # Preprocessing text into tokens and tokens into tensors.
    # Truncation set to True to ensure text is no longer than max_length.
    encoded_input = TOKENIZER(sentences, padding="max_length", truncation=True, max_length=MAX_TEXT_LENGTH, return_tensors="pt")  # Pytorch version
    encoded_input_dev = {key: value.to(DEVICE) for key, value in encoded_input.items()}

    # Run the model based on the passed in tokens.
    output = MODEL(**encoded_input_dev)

    # Get mean pooling.
    embed_mean = _mean_pooling(output, encoded_input_dev["attention_mask"]).cpu()
    embed_lens = torch.norm(embed_mean, dim=-1, keepdim=True)
    embed_batch = embed_mean / embed_lens

    return embed_batch


def get_embeddings(sentences: list = None):

    with torch.no_grad():
        embeds = []

        for i in tqdm(range(0, len(sentences), BATCH_SIZE)):
            embeds.append(_get_embedding_batch(sentences[i:i+BATCH_SIZE]))

    return torch.cat(embeds)


def get_expanded_context(x):

    context = x["Sentence"]
    text_nlp = x["NLP_Text"]

    # Get the length of the sentence context.
    expanded_context_len = len(TOKENIZER(context.text, max_length=MAX_TEXT_LENGTH)["input_ids"])  # Warning: Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy.
    context_sent_id = 0

    # Loop through the nlp text to collect the full text.
    # Get the id number of the sentence from the full text.
    for i, s in enumerate(list(text_nlp.sents)):

        if s.text == context.text:
            context_sent_id = 1
            break

    # Condition to get expanded context for sentence.
    if expanded_context_len < MAX_TEXT_LENGTH:

        # Condition for the first sentence?
        if context_sent_id == 0 and len(list(text_nlp.sents)) > 1:
            context_sent_id += 1

        # Context sentences.
        sentence_before = list(text_nlp.sents)[context_sent_id-1].text
        current_sentence = list(text_nlp.sents)[context_sent_id].text
        # sentence_after = list(text_nlp.sents)[context_sent_id+1].text

        # Store expanded context and get new length.
        expanded_context = sentence_before + current_sentence
        expanded_context_len = en(TOKENIZER(expanded_context, max_length=MAX_TEXT_LENGTH)["input_ids"])

        if expanded_context_len < MAX_TEXT_LENGTH:

            # Condition for last sentence?
            if context_sent_id == len(list(text_nlp.sents))-1 and len(list(text_nlp.sents)) > 2:
                context_sent_id -= 1

            try:
                if len(list(text_nlp.sents)) > 2:
                    expanded_context = list(text_nlp.sents)[context_sent_id-1].text + list(text_nlp.sents)[context_sent_id].text + list(text_nlp.sents)[context_sent_id+1].text
            except:
                print("Broken here")
                print(context_sent_id)
                print(len(list(text_nlp.sents)))
                print(context.text)
                expanded_context = list(text_nlp.sents)[context_sent_id-1].text + list(text_nlp.sents)[context_sent_id].text + list(text_nlp.sents)[context_sent_id+1].text

    else:
        expanded_context = context.text

    return expanded_context
