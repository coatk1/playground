# Standard Libraries
import os

# Third-party Libraries
import torch

from modules import embeddings


def save_embeds(pytorch_path: str, sentence: list, file: str = None) -> None:

    # Create path if it doesn't exist.
    if not os.path.exists(pytorch_path):
        os.makedirs(pytorch_path)

    sentence_embeds = embeddings.get_embeddings(sentences=sentence)

    embeds_dict = {}

    for s, e in zip(sentence, sentence_embeds):
        embeds_dict[s] = e

    if file:
        saved_file = os.path.join(pytorch_path, "embeddings_{}.pth".format(file))
    else:
        saved_file = os.path.join(pytorch_path, "embeddings_file.pth".format(file))

    torch.save(embeds_dict, saved_file)

    return None


def load_embeds(pytorch_path: str, file: str = None) -> dict:

    if file:
        saved_file = os.path.join(pytorch_path, "embeddings_{}.pth".format(file))
    else:
        saved_file = os.path.join(pytorch_path, "embeddings_file.pth".format(file))

    embeds_dict = torch.load(saved_file)

    return embeds_dict
