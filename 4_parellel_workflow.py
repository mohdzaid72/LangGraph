#upsc essay marks work flow
#marks based on COA(clearity of thoughts)(LLM), DOA(depth of analysis)(LLM) , Language(LLM)
#these LLMs return two info: feedback and score(0-10)
#in the final step we generate summarized feedback and agerage score of the llm to show as output


from langgraph.graph import StateGraph
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict,Annotated
import operator
from pydantic import BaseModel,Field
from langchain.output_parsers import PydanticOutputParser 
from langchain.prompts import PromptTemplate

load_dotenv()

#defining the state
class EsState(TypedDict):
    essey:str
    
    cot_feed:str
    dot_feed:str
    lang_feed:str
    
    """cot_score:int
    dot_score:int
    lanf_score:int"""
    indv_score:Annotated[list[int], operator.add] #operator is used to add instead of repleace.
    
    sum_feed:str
    sum_score:float
    
llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)


#structure output parser
class Schema(BaseModel):
    feedback:str=Field(des="detail feedback for essay")
    Score:int = Field(des="score it out of 10",ge=0,le=10)
    
    # create parser
parser = PydanticOutputParser(pydantic_object=Schema)

# build prompt with format instructions
prompt_template = PromptTemplate(
    template=(
        "Evaluate the language quality of the following essay and provide JSON output.\n\n"
        "Essay:\n{essay}\n\n"
        "{format_instructions}"
    ),
    input_variables=["essay"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


essay = """India in the Age of AI
As the world enters a transformative era defined by artificial intelligence (AI), India stands at a critical juncture — one where it can either emerge as a global leader in AI innovation or risk falling behind in the technology race. The age of AI brings with it immense promise as well as unprecedented challenges, and how India navigates this landscape will shape its socio-economic and geopolitical future.

India's strengths in the AI domain are rooted in its vast pool of skilled engineers, a thriving IT industry, and a growing startup ecosystem. With over 5 million STEM graduates annually and a burgeoning base of AI researchers, India possesses the intellectual capital required to build cutting-edge AI systems. Institutions like IITs, IIITs, and IISc have begun fostering AI research, while private players such as TCS, Infosys, and Wipro are integrating AI into their global services. In 2020, the government launched the National AI Strategy (AI for All) with a focus on inclusive growth, aiming to leverage AI in healthcare, agriculture, education, and smart mobility.

One of the most promising applications of AI in India lies in agriculture, where predictive analytics can guide farmers on optimal sowing times, weather forecasts, and pest control. In healthcare, AI-powered diagnostics can help address India’s doctor-patient ratio crisis, particularly in rural areas. Educational platforms are increasingly using AI to personalize learning paths, while smart governance tools are helping improve public service delivery and fraud detection.

However, the path to AI-led growth is riddled with challenges. Chief among them is the digital divide. While metropolitan cities may embrace AI-driven solutions, rural India continues to struggle with basic internet access and digital literacy. The risk of job displacement due to automation also looms large, especially for low-skilled workers. Without effective skilling and re-skilling programs, AI could exacerbate existing socio-economic inequalities.

Another pressing concern is data privacy and ethics. As AI systems rely heavily on vast datasets, ensuring that personal data is used transparently and responsibly becomes vital. India is still shaping its data protection laws, and in the absence of a strong regulatory framework, AI systems may risk misuse or bias.

To harness AI responsibly, India must adopt a multi-stakeholder approach involving the government, academia, industry, and civil society. Policies should promote open datasets, encourage responsible innovation, and ensure ethical AI practices. There is also a need for international collaboration, particularly with countries leading in AI research, to gain strategic advantage and ensure interoperability in global systems.

India’s demographic dividend, when paired with responsible AI adoption, can unlock massive economic growth, improve governance, and uplift marginalized communities. But this vision will only materialize if AI is seen not merely as a tool for automation, but as an enabler of human-centered development.

In conclusion, India in the age of AI is a story in the making — one of opportunity, responsibility, and transformation. The decisions we make today will not just determine India’s AI trajectory, but also its future as an inclusive, equitable, and innovation-driven society."""
    
chain = prompt_template | model | parser

# run
result = chain.invoke({"essay": essay})
print(result)