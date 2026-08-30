from langchain_community.document_loaders import JSONLoader
loader=JSONLoader(file_path="D:/GEN AI/Rag Project/data_folder/college_faqs.json",jq_schema=".[]",text_content=False)
documents = loader.load()
print(documents)