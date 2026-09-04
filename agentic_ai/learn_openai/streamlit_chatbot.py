import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_response(messages):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages
    )
    return response.choices[0].message.content

st.title("chatbot with OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Whats on your mind?")

if prompt:
    st.session_state.messages.append({"role":"user", "content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    messages = [{"role":"user",
                "content":prompt
    }]
    response = get_response(messages)

    st.session_state.messages.append({"role":"assistant", "content":response})

    with st.chat_message("assistant"):
        st.markdown(response)
