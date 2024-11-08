from finbot import FinBotCreator
from config import *
import streamlit as st
from streamlit_chat import message
st.session_state.clicked=True
@st.cache_resource(show_spinner=True)
def create_finbot():
    finbotcreator=FinBotCreator()
    finbot=finbotcreator.create_finbot()
    return finbot
finbot=create_finbot()

def infer_finbot(prompt):
    if isinstance(prompt, str) and len(prompt.split()) > 512:
        prompt = ' '.join(prompt.split()[:512])
    model_out = finbot(prompt)
    answer = model_out['result']
    return answer


def display_conversation(history):
    for i in range(len(history['assistant'])):
        message(history['user'][i],is_user=True,key=str(i)+"_user")
        message(history['assistant'][i],key=str(i))

def main():
    st.title("Medical Assistant : Your Doctor")
    st.subheader("A bot created using Langchain to run on cpu answering  your your medical queries")

    user_input = st.text_input("Enter Your query")

    if "assistant" not in st.session_state:
        st.session_state["assistant"]=["I am ready to help you"]
    if "user" not  in st.session_state:
        st.session_state["user"] =["Hey there!"]
    
    if st.session_state.clicked:
        if st.button("Answer"):

            answer = infer_finbot({'query':user_input})
            st.session_state['user'].append(user_input)
            st.session_state["assistant"].append(answer)

            if st.session_state['assistant']:
                display_conversation(st.session_state)
    
if __name__ == "__main__":
    main()