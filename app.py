import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage,HumanMessage,SystemMessage
import os
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(temperature=0.6)

st.set_page_config(page_title='AI Personal Assistant (PA)')
st.header('Chat with your Timetable Planning AI PA')

if 'messages' not in st.session_state:
    st.session_state['messages']=[
        AIMessage(content='You are a professional Personal Timetable planner')
    ]

def chatt(question):
    st.session_state['messages'].append(HumanMessage(content=question))
    answer=llm(st.session_state['messages'])
    st.session_state['messages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input('Your Question Here')
answer1=chatt(input)

button=st.button('SUBMIT')

if button:
    st.subheader('The Response is')
    st.write(answer1)