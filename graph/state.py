from typing import TypedDict

from pydantic import BaseModel

class StartupAnalysis(BaseModel):
    problem: str
    target_customers: str
    proposed_solution: str
    value_proposition: str
    business_model: str
    assumptions_to_validate: list[str]
    risks: list[str]

class MVPStrategy(BaseModel):
    mvp_goal: str
    core_features: list[str]
    deferred_features: list[str]
    target_users: str
    validation_strategy: list[str]

class StartupState(TypedDict, total=False):
    startup_idea: str
    startup_analysis: StartupAnalysis
    mvp_strategy: MVPStrategy
    milestones: list
    roadmap: list
    hiring_plan: list
    final_plan: dict