import streamlit as st
from llama_index.llms.ollama import Ollama

st.title("chat with llama")

llm = Ollama(model="llama3.2", request_timeout=60.0)
st.text_input("Your question")