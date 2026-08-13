import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from graph.state import (
    StartupState,
    StartupAnalysis,
    MVPStrategy
)
from prompts.prompts import (
    STARTUP_ANALYSIS_PROMPT,
    MVP_STRATEGY_PROMPT
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(StartupAnalysis)
mvp_llm = llm.with_structured_output(MVPStrategy)

def analyze_startup(state: StartupState):
    startup_idea = state["startup_idea"]

    prompt = STARTUP_ANALYSIS_PROMPT.format(
        startup_idea=startup_idea
    )

    response = structured_llm.invoke(prompt)

    return {
        "startup_analysis": response.content
    }

def plan_mvp(state: StartupState):
    startup_idea = state["startup_idea"]
    startup_analysis = state["startup_analysis"]

    prompt = MVP_STRATEGY_PROMPT.format(
        startup_idea=startup_idea,
        startup_analysis=startup_analysis.model_dump()
    )

    response = mvp_llm.invoke(prompt)

    return {
        "mvp_strategy": response
    }