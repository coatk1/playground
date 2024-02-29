from collections import ChainMap

A_URLS = {
    "a": "https:",
}

B_URLS = {
    "b": "https:",
}

C_URLS = {
    "c": "https:",
}

merged_dict = {}

merged_dict = {**A_URLS, **B_URLS, **C_URLS}

list(merged_dict.values())
