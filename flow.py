# Here we only Learn the flow of langGraph
from langgraph.graph import StateGraph, START,END
from typing import TypedDict

#define state
class BMIState(TypedDict):
    weight: float
    height: float
    bmi: float
    category: str


def bmi(state: BMIState) -> BMIState:
    weight= state["weight"]
    hight=state["height"]
    bmi=weight/(hight*hight)
    state["bmi"]=bmi
    
    return state
    
    
# define graph

graph= StateGraph(BMIState)


# add node to your graph
graph.add_node("bmi",bmi)




# add edge to your graph
graph.add_edge(START,"bmi")
graph.add_edge("bmi",END)
# compile your graph
flow=graph.compile()

# execute your graph
result=flow.invoke({"weight":70,"height":1.75})
print(result)