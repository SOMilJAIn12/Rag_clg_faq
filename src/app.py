import streamlit as st

from rag import llm, prompt
from retriever import retriever


st.set_page_config(
    page_title="College FAQ Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title(" College FAQ Assistant")
st.caption("Ask questions about college academics, exams, fees, hostel, placements and more.")


if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
query = st.chat_input("Ask your college question...")


if query:

    # Display user message
    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.messages.append({
        "role": "user",
        "content": query
    })


    # Retrieve relevant documents
    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )


    # Create prompt
    final_prompt = prompt.invoke({
        "context": context,
        "input": query
    })


    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Finding answer..."):
            response = llm.invoke(final_prompt)

        st.markdown(response.content)


    st.session_state.messages.append({
        "role": "assistant",
        "content": response.content
    })