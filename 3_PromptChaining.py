"""Prompt chaining :
            Using LLM multiple times in the workflow"""

#i this we are trying to create Blog

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from typing import TypedDict

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation"
)
model=ChatHuggingFace(llm=llm)
# definne State

class BlogState(TypedDict):
    topic:str
    outline:str
    blog:str


#function
def llm_outline(state:BlogState)->BlogState:
    topic=state['topic']
    prompt=f"create a best outline on the {topic}"
    outline=model.invoke(prompt).content
    state['outline']=outline
    return state

def llm_blog(state:BlogState)->BlogState:
    outline=state['outline']
    prompt=f"write a perfect blog,where outline is {outline}"
    state['blog']=model.invoke(prompt).content
    return state
#define graph
graph=StateGraph(BlogState)

#add node
graph.add_node('llm_outline',llm_outline)
graph.add_node("llm_blog",llm_blog)

#add edges
graph.add_edge(START,"llm_outline")
graph.add_edge("llm_outline","llm_blog")
graph.add_edge("llm_blog",END)

#compile
flow=graph.compile()

#execute
output=flow.invoke({"topic":"Family"})
print(output)