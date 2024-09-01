import streamlit as st
import openai
import requests

# Set your OpenAI API key here
openai.api_key = "your_openai_api_key_here"

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or any other GPT-3 model
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def get_mock_ticket_data():
    # This is a free API to mock ticket booking; you can use a different one if needed.
    response = requests.get("https://api.mocki.io/v1/ce5f60e2")  # Example API; replace with a suitable one
    return response.json()

def main():
    st.title("Ticket Booking Chatbot")
    
    user_input = st.text_input("Ask me anything about ticket booking:")
    
    if st.button("Send"):
        if user_input:
            # Get the response from OpenAI
            response = get_openai_response(user_input)
            
            # Mock ticket data example
            ticket_data = get_mock_ticket_data()
            
            st.write(f"Chatbot: {response}")
            st.write("Here's some example ticket data for your request:")
            st.json(ticket_data)

if __name__ == "__main__":
    main()
