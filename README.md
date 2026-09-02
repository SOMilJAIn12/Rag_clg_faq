# College FAQ RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows students to ask questions about college-related information such as attendance, examinations, fees, hostel, library, placements, scholarships, academics, and student services.

The application retrieves relevant information from a college FAQ knowledge base and uses an LLM to generate a grounded answer.

## Features

* Semantic search over college FAQs
* Retrieval-Augmented Generation (RAG)
* Hugging Face embeddings
* Chroma vector database
* MMR-based document retrieval
* Groq LLM for answer generation
* Streamlit chat interface
* Reduced hallucination through context-grounded answers
* 190+ college FAQ entries
* Multiple FAQ categories

## Architecture

```text
                 college_faqs.json
                        |
                        v
                   JSONLoader
                        |
                        v
                   Documents
                        |
                        v
              Hugging Face Embeddings
                        |
                        v
                  Chroma Vector DB
                        |
                        v
                  MMR Retriever
                        |
                        v
                 Relevant FAQs
                        |
                        v
                  Prompt Template
                        |
                        v
                    Groq LLM
                        |
                        v
                 Generated Answer
                        |
                        v
                 Streamlit UI
```

## Project Structure

```text
Rag Project/
|
├── data_folder/
│   └── college_faqs.json
|
├── Chromadb/
|
├── src/
│   ├── loader.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   ├── rag.py
│   └── app.py
|
├── .env
├── requirements.txt
└── README.md
```

## Components

### loader.py

Loads the FAQ JSON file using LangChain's `JSONLoader` and converts each FAQ into a LangChain Document.

### embeddings.py

Uses the Hugging Face embedding model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

to convert FAQ text into numerical embeddings.

### vectorstore.py

Creates or loads the Chroma vector database and stores the document embeddings.

### retriever.py

Uses Chroma's MMR retrieval strategy to retrieve relevant FAQ documents.

Example:

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)
```

### rag.py

Contains the Groq LLM and prompt template used to generate answers from the retrieved context.

### app.py

Provides the Streamlit chat interface through which students interact with the RAG assistant.

## Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming language |
| LangChain    | RAG framework        |
| Hugging Face | Embedding model      |
| Chroma       | Vector database      |
| Groq         | LLM inference        |
| Streamlit    | Web interface        |
| JSON         | FAQ knowledge base   |

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd "Rag Project"
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit the `.env` file to GitHub.

Add the following to `.gitignore`:

```text
.env
.venv/
__pycache__/
Chromadb/
```

## Running the Project

First, create or populate the Chroma database:

```bash
python src/vectorstore.py
```

Then start the Streamlit application:

```bash
streamlit run src/app.py
```

The application will open in your browser.

## Example Questions

```text
What is the minimum attendance required?

How can I check my attendance?

How do I apply for hostel accommodation?

How do I fill the examination form?

How is SGPA calculated?

How can I apply for a scholarship?

How many books can I issue from the library?

Can students with backlogs participate in placements?
```

## Hallucination Handling

The assistant is instructed to answer using only information retrieved from the FAQ knowledge base.

If relevant information cannot be found, the assistant responds:

```text
I don't have enough information in the college FAQ knowledge base to answer this. Please contact the relevant college department.
```

This helps prevent the model from generating unsupported college policies or information.

## RAG Process

When a student asks a question:

1. The question is converted into an embedding.
2. Chroma searches for semantically relevant FAQs.
3. MMR selects relevant and diverse documents.
4. Retrieved FAQs are inserted into the prompt.
5. The Groq LLM generates an answer using the retrieved context.
6. The answer is displayed in the Streamlit interface.

## Future Improvements

* Add source citations for every answer
* Add more college-specific FAQs
* Add an admin panel for updating FAQs
* Add conversation memory
* Add FAQ category filtering
* Add multilingual support
* Add authentication
* Add answer feedback
* Add document upload support
* Deploy the application online

## Disclaimer

This application is an educational RAG project. Important academic, examination, fee, attendance, or administrative decisions should always be verified using the latest official college or university information.

## Author

Somil Jain

College FAQ RAG Assistant built using LangChain, Hugging Face, Chroma, Groq, and Streamlit.
