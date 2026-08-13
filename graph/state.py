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

class Milestone(BaseModel):
    name: str
    objective: str
    key_tasks: list[str]
    success_criteria: list[str]

class MilestonePlan(BaseModel):
    milestones: list[Milestone]

class RoadmapItem(BaseModel):
    phase: str
    timeline: str
    priority: str
    objectives: list[str]
    dependencies: list[str]

class RoadmapPlan(BaseModel):
    roadmap: list[RoadmapItem]

class HiringRole(BaseModel):
    role: str
    responsibilities: list[str]
    hiring_stage: str
    reason: str

class HiringPlan(BaseModel):
    roles: list[HiringRole]

class FinalStartupPlan(BaseModel):
    executive_summary: str
    startup_direction: str
    immediate_priorities: list[str]
    key_risks: list[str]
    next_steps: list[str]

class StartupState(TypedDict, total=False):
    startup_idea: str
    startup_analysis: StartupAnalysis
    mvp_strategy: MVPStrategy
    milestones: list[Milestone]
    roadmap: list[RoadmapItem]
    hiring_plan: HiringPlan
    final_plan: FinalStartupPlan