#token by token response ko print krna isse user ka experience acha hota h


import streamlit as st

from backend import flow
from langchain_core.messages import HumanMessage


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
        
    #st.session_state['message_history'].append({'role':"assistant",'content':user_input})    
    with st.chat_message("assistant"):
        config={"configurable": {'thread_id':thread_id}}
       
        res=st.write_stream(
            message_chunk.content for message_chunk,metadata in flow.stream(
                {'message':HumanMessage(content=user_input)},
                config=config,
                stream_mode="messages"
            )
        )
       
       
       
    st.session_state['message_history'].append({'role':"assistant",'content':res}) 