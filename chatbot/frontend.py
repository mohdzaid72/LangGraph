import streamlit as st

from backend import flow
from langchain_core.messages import HumanMessage

#with st.chat_message("user"):
#    st.text("Hii!!")
#with st.chat_message("assistant"):
#    st.text("How can i help you today?")
thread_id="12"  
    #for maintain the memory we are creating the list of dict where {role:""...,contet:""...},{same}...
if "message_history" not in st.session_state:
    st.session_state['message_history']=[]
    
user_input=st.chat_input("type yor question?")

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
    
if user_input:
    
    st.session_state['message_history'].append({'role':"user",'content':user_input})
    with st.chat_message("user"):
        st.text(user_input)
        
    st.session_state['message_history'].append({'role':"assistant",'content':user_input})    
    with st.chat_message("assistant"):
        config={"configurable": {'thread_id':thread_id}}
        ans=flow.invoke({'message':HumanMessage(content=user_input)},config=config)
        res=ans['message'][-1].content
        st.text(res)
        st.session_state['message_history'].append({'role':"assistant",'content':res}) 