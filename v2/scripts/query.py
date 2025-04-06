from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load vectorstore
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

# Load TinyLlama via transformers
model_path = "./Tinyllama"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

# Ask question
def ask_question_with_context(question, retriever, top_k=4):
    docs = retriever.invoke(question)

    context = ""
    for doc in docs[:top_k]:
        if len(context) + len(doc.page_content) < 3000:
            context += "\n\n" + doc.page_content
        else:
            break

    prompt = f"""You are a secure code review assistant. Use the following context to answer the question. Be factual and concise.

Context:
{context}

Question: {question}
Answer:"""

    result = pipe(prompt, max_new_tokens=256)
    return result[0]['generated_text'], docs

# Interactive loop
while True:
    question = input("\n Ask your question (or type 'exit'): ")
    if question.lower() == "exit":
        break
    answer, _ = ask_question_with_context(question, vectorstore.as_retriever())
    print("\n Answer:\n", answer)