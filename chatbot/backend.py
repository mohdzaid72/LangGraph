from langgraph.graph import StateGraph, START, END
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage

from langgraph.checkpoint.memory import MemorySaver


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
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

