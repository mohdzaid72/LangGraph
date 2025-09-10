from langgraph.graph import StateGraph, START, END
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage

from langgraph.checkpoint.memory import MemorySaver


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)


#define state

from langgraph.graph.message import add_messages
class ChatState(TypedDict):
    message:Annotated[list[BaseMessage],add_messages]
    
    
    
#nodes
def ChatModel(state:ChatState):
    prompt=state["message"]
    response=model.invoke(prompt)
    return {"message":response}

#define graph
checkpointer=MemorySaver()
graph=StateGraph(ChatState)

#define Node
graph.add_node("ChatModel",ChatModel)

#Define edges
graph.add_edge(START,"ChatModel")
graph.add_edge("ChatModel",END)


#compile

flow=graph.compile(checkpointer=checkpointer)

"""ans=flow.invoke({"message":HumanMessage(content="what is the capital of india?")})
print(ans['message'][-1].content)
"""


thread_id='1'
while True:
    user_input=input("type your question...")
    print("user :", user_input)
    
    if user_input.strip().lower() in ["bye","exit","quit","cancle"]:
        break
    else:
        config={"configurable": {'thread_id':thread_id}}
        ans=flow.invoke({"message":HumanMessage(content=user_input)},config=config,max_new_tokens=200)
        print("AI :",ans['message'][-1].content)
        