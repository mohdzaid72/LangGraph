from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

"""work flow would be
    START->LLM->END
    """

#defining State
class QAState(TypedDict):
    Que:str
    Ans:str
    
    
    
#creating model
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation"
)
model=ChatHuggingFace(llm=llm)


#creation function for the Question Answer(creation node)

def LLM(state:QAState) ->QAState:
    result=model.invoke(state["Que"])
    state['Ans']=result.content
    return state

#define Graph
graph=StateGraph(QAState)

#add node to the graph
graph.add_node("LLM",LLM)

#add edges
graph.add_edge(START,"LLM")
graph.add_edge("LLM",END)
#compile
flow=graph.compile()

#execute
result=flow.invoke({"Que":"tell me the way how i can easily learn LangGraph to create agent at the industry level"})
print(result)