from langchain_community.document_loaders import JSONLoader
loader=JSONLoader(file_path="D:/GEN AI/Rag Project/data_folder/college_faqs.json",
                jq_schema=".[]",
                content_key="answer",
                metadata_func=lambda record, metadata: {
                    "question": record["question"],
                    "category": record["category"]
                })
documents = loader.load()
print(documents)