from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from retriever import retriever
from langchain_core.prompts import ChatPromptTemplate
llm =ChatGroq(
    model="openai/gpt-oss-20b"
)
prompt = ChatPromptTemplate.from_template("""
You are a helpful College FAQ Assistant.

Answer the student's question using ONLY the information provided in the context.

If the answer cannot be found in the context, say:
"I don't have enough information in the college FAQ knowledge base to answer this. Please contact the relevant college department."

Do not make up information or assume college rules.

Context:
{context}

Student Question:
{input}

Answer:
""")
print("Rag system is created")
print("press 0 to exit")
while True:
    query = input("You: ")

    if query == "0":
        break

    docs = retriever.invoke(query)
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke({
        "context": context,
        "input": query
    })

    response = llm.invoke(final_prompt)

    print(f"\nAI: {response.content}")