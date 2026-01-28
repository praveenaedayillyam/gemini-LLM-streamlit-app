import google.generativeai as genai
import streamlit as st

key = key="AIzaSyCMWNHH8AyoDiLoBZQSxZECIt03mmWiqS4"   # API Key
genai.configure(api_key=key)

# Function to get response from Gemini
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro') 
        res = model.generate_content(prompt)
        return res.text
    except Exception as e:
        return f"Error: {e}"

# Initializing session state for storing chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Callback function for handling user input
def handle_user_input():
    user_input = st.session_state["user_input"]
    if user_input:
        # user's message
        st.session_state.messages.append(("user", user_input))

        # Get the chatbot's response
        response = get_gemini_response(user_input)
        st.session_state.messages.append(("bot ", response))

        # Clear the input field
        st.session_state["user_input"] = ""

st.title("Chatbot")
st.write("Ask your questions and get responses from the Gemini model.")
# Display chat history
for sender, message in st.session_state.messages:
    if sender == "user":
        # User
        st.markdown(f"<p style='color:red; font-weight:bold;'>You: {message}</p>", unsafe_allow_html=True)
    else:
        # Bot
        st.markdown(f"<p style='color:black;'>Gemini: {message}</p>", unsafe_allow_html=True)

# user input
st.text_area(
    "Type your message:",
    key="user_input",
    placeholder="Type here and press Enter...",
    on_change=handle_user_input,
    label_visibility="hidden"
)

# run by the command:   streamlit run "<filepath>"