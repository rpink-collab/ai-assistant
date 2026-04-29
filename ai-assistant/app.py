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

import json
from pathlib import Path

def get_orders_data(filepath: str) -> str:
    path = Path(filepath)
    if not path.exists():
        return "[]"

    with open(path, "r") as f:
        data = json.load(f)
        return json.dumps(data, indent=2)

orders_context = get_orders_data("orders.json")

def load_logs(filepath: str) -> list:
    json_path = Path(filepath)
    if json_path.exists():
        with open(json_path, "r") as f:
            return json.load(f)
    return []

def save_logs(filepath: str, logs: list) -> None:
    json_path = Path(filepath)
    with open(json_path, "w") as f:
        json.dump(logs, f, indent=2)