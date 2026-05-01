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

if "messages" not in st.session_state:
    st.session_state.messages = []

logs = load_logs("chat_logs.json")
for log in logs:
    st.session_state.messages.append({
        "role": "user",
        "content": log["user_message"]
    })
    st.session_state.messages.append({
        "role": "assistant",
        "content": log["assistant_message"]
    })

if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "ai-assistant",
        "content": "Hi! Ask me a question."
    })

if "messages" not in st.session_state:
    st.session_state.messages = []

    logs = logger.load_logs()
    for log in logs:
        st.session_state.messages.append(
            {"role": "user", "content": log["user_message"]}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": log["assistant_message"]}
        )

    if len(st.session_state.messages) == 0:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Hi! Ask me a question about the order data."
        })
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)
with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
        response_text = bot.get_ai_response(
            st.session_state.messages
        )
        st.markdown(response_text)

st.session_state.messages.append({
    "role": "assistant",
    "content": response_text
})

logs = logger.load_logs()
logs.append({"user_message": user_input, "assistant_message": response_text})
logger.save_logs(logs)