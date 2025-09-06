# Here we only Learn the flow of langGraph
from langgraph.graph import StateGraph, START,END
from typing import TypedDict

#define state
class BMIState(TypedDict):
    weight: float
    height: float
    bmi: float
    category: str

#used function for the nodes
def bmi(state: BMIState) -> BMIState:
    weight= state["weight"]
    hight=state["height"]
    bmi=weight/(hight*hight)
    state["bmi"]=bmi
    
    
    return state
def bmi_lebel(state: BMIState)-> BMIState:
    bmi=state['bmi']
    if bmi<18.5:
        state["category"]="underweight"
    elif bmi>=18.5 and bmi<25:
        state['category']="Normal"
    elif bmi>25:
        state['category']='Overweight'
    else:
        state['category']='obese'
    return state
    
# define graph

graph= StateGraph(BMIState)


# add node to your graph
graph.add_node("bmi",bmi)
graph.add_node("bmi_label",bmi_lebel)




# add edge to your graph
graph.add_edge(START,"bmi")
graph.add_edge("bmi","bmi_label")
graph.add_edge("bmi_label",END)

# compile your graph
flow=graph.compile()

# execute your graph
result=flow.invoke({"weight":70,"height":1.75})
print(result)