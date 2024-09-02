import google.generativeai as genai
import os
import streamlit as st

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

st.title("Chat Application using Gemini 1.5 Flash")

user_quest = st.text_input("Ask a question:")
btn = st.button("Ask")

if btn and user_quest:
    result = LLM_Response(user_quest)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)