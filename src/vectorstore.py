from langchain_community.vectorstores import Chroma
from loader import documents
from embeddings import embedding
for doc in documents:
    doc.page_content = (
        f"Question: {doc.metadata['question']}\n"
        f"Answer: {doc.page_content}"
    )
vectorstore = Chroma(
    persist_directory="D:/GEN AI/Rag Project/Chromadb",
    embedding_function=embedding
)
vectorstore.add_documents(documents)
print(f"Added {len(documents)} documents")