from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Weaviate
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import * 
import weaviate
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from langchain.retrievers import BM25Retriever
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import *
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def retriever_creation():
    dir_loader = DirectoryLoader(
                            DATA_DIR_PATH,
                            glob='*.pdf',
                            loader_cls=PyPDFLoader
                        )
    docs = dir_loader.load()
    print("PDFs Loaded")
    
    txt_splitter = RecursiveCharacterTextSplitter(
                            chunk_size=CHUNK_SIZE, 
                            chunk_overlap=CHUNK_OVERLAP
                        )
    inp_txt = txt_splitter.split_documents(docs)
    print("Data Chunks Created")

    bm25_retriever = BM25Retriever.from_documents(inp_txt)
    print("BM25 Retriever Creation Completed")
    return bm25_retriever
