from typing import Dict, List, Union


def get_leaves(item: Union[Dict, List], key: Dict = None) -> List:
    """get_leaves.

    Return all key: values recursively.

    Parameters
    ----------
    item : Union[Dict, List]
        The dictionary.
    key : Dict, optional
        The key., by default None

    Returns
    -------
    List
        Return key: values recursively.
    """
    try:
        if isinstance(item, dict):
            leaves = {}

            for i in item.keys():
                leaves.update(get_leaves(item[i], i))
            return leaves

        elif isinstance(item, list):
            leaves = {}

            for i in item:
                leaves.update(get_leaves(i, key))
            return leaves

        else:
            return {key: item}

    except Exception as e:
        print(e)
