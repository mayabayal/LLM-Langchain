from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables
open_api_key = os.getenv("OPEN_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Check if the keys are set
if not open_api_key:
    raise ValueError("OPEN_API_KEY environment variable is not set")
if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY environment variable is not set")

os.environ['OPEN_API_KEY'] = open_api_key
os.environ['LANGCHAIN_TRACKING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = langchain_api_key
os.environ['OPENAI_API_KEY'] = open_api_key

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

st.title("LangChain Demo with OpenAI")
input_text = st.text_input("Search the topic you want")

# OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
