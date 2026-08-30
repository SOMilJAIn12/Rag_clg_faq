from dotenv import load_dotenv
load_dotenv()
from loader import documents
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)