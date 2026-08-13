import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from graph.state import StartupState
from prompts.prompts import STARTUP_ANALYSIS_PROMPT

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def analyze_startup(state: StartupState):
    startup_idea = state["startup_idea"]

    prompt = STARTUP_ANALYSIS_PROMPT.format(
        startup_idea=startup_idea
    )

    response = llm.invoke(prompt)

    return {
        "startup_analysis": response.content
    }