from transformers import AutoTokenizer, AutoModel

TOKENIZER = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
MODEL = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
