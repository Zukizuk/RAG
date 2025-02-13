import streamlit as st
from ai import get_streaming_response

st.set_page_config(page_title="RAG AI", layout="centered")
with st.sidebar:
    st.sidebar.markdown("<h2 style='text-align: center; color: white;'>ChatRAGI</h2>", unsafe_allow_html=True)
    history, settings, about = st.tabs(["📕 Chat History", "⚙️ Settings", "📝 About"])


st.markdown("<h1 style='text-align: center; color: white;'>Welcome to ChatRAGI</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Message ChatRAGI")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            streaming_response = get_streaming_response(prompt)
            
            for text in streaming_response.response_gen:
                full_response += text
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Error generating response: {e}")