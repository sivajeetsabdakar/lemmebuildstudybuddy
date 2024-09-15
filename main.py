from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import requests

load_dotenv()

API_URL = "https://sad-sutherland-ecstatic.lemme.cloud/api/cca11833-2cbb-4840-a8b6-bf0b9f7137e2"

def get_lemmebuild_response(input):
    data = {
        "message": input,
    }

    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data['res']['reply']
    else:
        return f"Error: {response.status_code}, Response: {response.text}"

st.set_page_config(page_title="Smart Buddy")

st.header("I'm your study buddy, the smarter one 🧠")

if 'history' not in st.session_state:
    st.session_state['history'] = []

input = st.text_input("What's your doubt ?: ", key="input")

col1, col2 = st.columns([2, 2])  # Adjusted column width to make both columns equal

with col1:
    submit = st.button("Send")

with col2:
    with st.expander("Chat History"):
        if st.session_state['history']:
            for chat in st.session_state['history']:
                st.write(f"**You**: {chat['input']}")
                st.write(f"**StudyBuddy**: {chat['response']}")
    if st.button("Clear History"):  # This is placed inside col2 to ensure it shares the same width as the history expander
        st.session_state['history'] = []

if submit:
    response = get_lemmebuild_response(input)

    st.session_state['history'].append({
        'input': input,
        'response': response
    })

    st.subheader("The Response is")
    st.write(response)
