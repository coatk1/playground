# Useful for preserving datatypes when storing to a database (i.e. sqlite)

# Standard Libraries
import marshal  # Used to serialize lists
from io import BytesIO  # Used to serialize numpy arrays

# Third-party Libraries
import numpy as np


def load_numpy_bytes(x):
    """load_numpy_bytes.

    Source(s): https://stackoverflow.com/questions/53376786/convert-byte-array-back-to-numpy-array

    Load nd.array into bytes for db storage.

    Parameters
    ----------
    x : np.array
        Numpy array.

    Returns
    -------
    BytesIO
        BytesIO values.

    Examples
    --------
    >>> df["bytes_list"] = df["list"].apply(lambda x: marshal.dumps([x]))  # Store original datatype to bytes.
    >>> df["bytes_arrays"] = df["arrays"].apply(lambda x: load_numpy_bytes(np.array([x])))  # Store numpy array to bytes.
    """
    np_bytes = BytesIO()
    np.save(np_bytes, x, allow_pickle=True)
    np_bytes = np_bytes.getvalue()
    return np_bytes


def unload_numpy_bytes(x):
    """unload_numpy_bytes.

    Source(s): https://stackoverflow.com/questions/53376786/convert-byte-array-back-to-numpy-array

    Unload nd.array into bytes from db storage.

    Parameters
    ----------
    x : BytesIO
        BytesIO values.

    Returns
    -------
    np.array
        Numpy array.

    Examples
    --------
    >>> df["list"] = df["bytes_list"].apply(lambda x: marshal.loads(x))  # Convert bytes to original datatype.
    >>> df["arrays"] = df["bytes_arrays"].apply(lambda x: unload_numpy_bytes(x))  # Convert bytes to numpy array.
    """
    load_bytes = BytesIO(x)
    loaded_np = np.load(load_bytes, allow_pickle=True)
    return loaded_np
