from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant. Please response to user queries'),
        ('user','Question: {question}')
    ]
)

# streamlit framework
st.title("Langchain demo with Ollama")
input_text = st.text_input("Search the topic you want to ?")


# Ollama Llama 2 llms
llm = OllamaLLM(model="gemma3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))
    