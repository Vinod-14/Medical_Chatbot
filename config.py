DATA_DIR_PATH = 'data/'
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
EMBEDDER = 'BAAI/bge-base-en-v1.5'
DEVICE = 'cpu'
PROMPT_TEMPLATE = '''
You are my medical assistant designed to provide accurate and informative responses for medical queries with your knowledge in the medical domain.
With the information being provided, try to answer the question.
If you can't answer the question based on the information, either say you can't find an answer or are unable to find an answer.
So try to understand in depth about the context and answer only based on the information provided. Don't generate irrelevant answers.

Context :{context}
Question: {question}
Do provide only helpful answers

Helpful answer:
'''
INP_VARS = ['context', 'question']
CHAIN_TYPE = "stuff"
SEARCH_KWARGS = {'k': 2}
MODEL_CKPT = r"C:\Users\lenovo\OneDrive\Desktop\Medical_Bot\res\mistral-7b-openorca.Q6_K.gguf"
MODEL_TYPE = 'llama'
MAX_NEW_TOKENS = 1000
TEMPERATURE = 0.3
