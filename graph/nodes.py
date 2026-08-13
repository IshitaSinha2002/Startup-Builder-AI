import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from graph.state import (
    StartupState,
    StartupAnalysis,
    MVPStrategy,
    MilestonePlan,
    RoadmapPlan,
    HiringPlan,
    FinalStartupPlan
)
from prompts.prompt import (
    STARTUP_ANALYSIS_PROMPT,
    MVP_STRATEGY_PROMPT,
    MILESTONE_PLANNING_PROMPT,
    ROADMAP_PLANNING_PROMPT,
    HIRING_PLAN_PROMPT,
    FINAL_PLAN_PROMPT
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(StartupAnalysis)
mvp_llm = llm.with_structured_output(MVPStrategy)
milestone_llm = llm.with_structured_output(MilestonePlan)
roadmap_llm = llm.with_structured_output(RoadmapPlan)
hiring_llm = llm.with_structured_output(HiringPlan)
final_llm = llm.with_structured_output(FinalStartupPlan)

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

def plan_milestones(state: StartupState):
    startup_idea = state["startup_idea"]
    startup_analysis = state["startup_analysis"]
    mvp_strategy = state["mvp_strategy"]

    prompt = MILESTONE_PLANNING_PROMPT.format(
        startup_idea=startup_idea,
        startup_analysis=startup_analysis.model_dump(),
        mvp_strategy=mvp_strategy.model_dump()
    )

    response = milestone_llm.invoke(prompt)

    return {
        "milestones": response.milestones
    }

def plan_roadmap(state: StartupState):
    startup_idea = state["startup_idea"]
    startup_analysis = state["startup_analysis"]
    mvp_strategy = state["mvp_strategy"]
    milestones = state["milestones"]

    prompt = ROADMAP_PLANNING_PROMPT.format(
        startup_idea=startup_idea,
        startup_analysis=startup_analysis.model_dump(),
        mvp_strategy=mvp_strategy.model_dump(),
        milestones=[
            milestone.model_dump()
            for milestone in milestones
        ]
    )

    response = roadmap_llm.invoke(prompt)

    return {
        "roadmap": response.roadmap
    }

def plan_hiring(state: StartupState):
    startup_idea = state["startup_idea"]
    startup_analysis = state["startup_analysis"]
    mvp_strategy = state["mvp_strategy"]
    roadmap = state["roadmap"]

    prompt = HIRING_PLAN_PROMPT.format(
        startup_idea=startup_idea,
        startup_analysis=startup_analysis.model_dump(),
        mvp_strategy=mvp_strategy.model_dump(),
        roadmap=[
            item.model_dump()
            for item in roadmap
        ]
    )

    response = hiring_llm.invoke(prompt)

    return {
        "hiring_plan": response
    }

def build_final_plan(state: StartupState):
    startup_idea = state["startup_idea"]
    startup_analysis = state["startup_analysis"]
    mvp_strategy = state["mvp_strategy"]
    milestones = state["milestones"]
    roadmap = state["roadmap"]
    hiring_plan = state["hiring_plan"]

    prompt = FINAL_PLAN_PROMPT.format(
        startup_idea=startup_idea,
        startup_analysis=startup_analysis.model_dump(),
        mvp_strategy=mvp_strategy.model_dump(),
        milestones=[
            milestone.model_dump()
            for milestone in milestones
        ],
        roadmap=[
            item.model_dump()
            for item in roadmap
        ],
        hiring_plan=hiring_plan.model_dump()
    )

    response = final_llm.invoke(prompt)

    return {
        "final_plan": response
    }