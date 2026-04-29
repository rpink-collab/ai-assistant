import os
from py_compile import main
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="AI Order Assistant", page_icon="🤖")
st.title("🤖 Order Data Assistant")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY was not found. Check your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

