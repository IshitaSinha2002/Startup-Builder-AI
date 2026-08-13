from typing import TypedDict

class StartupState(TypedDict, total=False):
    startup_idea: str
    startup_analysis: dict
    mvp_strategy: dict
    milestones: list
    roadmap: list
    hiring_plan: list
    final_plan: dict