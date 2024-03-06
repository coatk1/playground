# Third-party Libraries
import numpy as np
from typing import Dict, List
# from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity


def get_embeddings_average(list_of_labels: list, label_df) -> Dict[str, List[List]]:
    """get_embeddings_average.

    Method to calculate the average embeddings of the labeled data.

    Parameters
    ----------
    list_of_labels : list
        A list of labels.
    label_df : pd.DataFrame
        Dataframe with labeled data.

    Returns
    -------
    Dict[str, List[List]]
        Returns a dictionary of each label and their respective embedding averaged.

    Example
    -------
    >>> labels_dict = get_embeddings_average(list_of_labels, label_df)
    """
    labels_dict = {}

    # Loop through the list to process each label.
    for i in range(len(list_of_labels)):

        # Get the embeddings of each label.
        col_embeds = label_df[label_df["Label"] == list_of_labels[i]]["sentence_embeds"]

        # Condition for non-empty embeddings.
        if len(col_embeds) > 0:

            # Get the average of each embedding and store this to a list of lists.
            average = [col_embeds.mean().tolist()]

            # Store label and list of lists to a dictionary for cosine.
            labels_dict[list_of_labels[i]] = average

    return labels_dict


def get_similarity(target: List[List], candidates: List[List]):
    """get_similarity.

    Method gets the sorted scores from cosine.

    # NOTE: When using from sklearn.metrics.pairwise import cosine_similarity it takes a list of lists.

    Parameters
    ----------
    target : List[List]
        The label to match.
    candidates : List[List]
        Labels you want to compare.

    Returns
    -------
    zip[tuple[np.int64, float]]

    Example
    -------
    >>> similarity = get_similarity(labels_dict[i], X_all_not_labeled)
    >>> similarity_scores = {}
    >>> for idx, sim in similarity:
    ...     similarity_scores[no_label_df.iloc[idx]["Sentence"]] = float(sim)
    ...     # similarity_scores.append(f"Similarity: {sim:.2f};", no_label_df.iloc[idx]["Sentence"])
    """
    # # Convert tensors into numpy arrays.
    # candidates = candidates.numpy()
    # target = target.numpy()

    # Run cosine similarity
    sim = cosine_similarity(target, candidates)

    # Convert into a list.
    sim = np.squeeze(sim).tolist()

    # Sort the numpy array (ascending by default).
    sort_index = np.argsort(sim)

    # Get associated score with each index.
    sort_score = [sim[i] for i in sort_index]
    similarity_scores = zip(sort_index, sort_score)

    return similarity_scores


# sim = cosine_similarity(labels_dict[list_of_labels[0]], X_all_not_labeled)
# temp = {}
# for i in range(len(sim[0])):
#     temp[no_label_df.iloc[i]["Sentence"]] = float(sim[0][1])
