import streamlit as st
from ai import get_response, query_engine

st.set_page_config(page_title="RAG AI", layout="centered")
st.sidebar.title("RAG AI")
# with st.sidebar:
#     messages = st.container()
#     if prompt := st.chat_input("Say something"):
#         messages.chat_message("human").write(prompt)
#         response = get_response(prompt)
#         messages.chat_message("assistant").write(response)

st.markdown("<h1 style='text-align: center; color: white;'>Welcome to ChatRAGI</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  

def process_query():
    """Processes the user query."""
    # response = query_engine.query(st.session_state.prompt)
    # return response
    response = get_response(st.session_state.prompt)
    st.session_state.chat_history.append(("human", st.session_state.prompt))
    st.session_state.chat_history.append(("assistant", response))

prompt = st.chat_input("Your message", key="prompt",on_submit=process_query)

messages = st.container()
for sender, message in st.session_state.chat_history:
    if sender == "human":
        messages.chat_message("human").markdown(message)
    else:
        messages.chat_message("assistant").markdown(message)
