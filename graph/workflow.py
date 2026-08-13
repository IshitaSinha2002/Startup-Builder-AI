from langgraph.graph import StateGraph, START, END
from graph.state import StartupState

from graph.nodes import (
    analyze_startup,
    plan_mvp,
    plan_milestones,
    plan_roadmap,
    plan_hiring,
    build_final_plan
)

workflow = StateGraph(StartupState)

workflow.add_node("analyze_startup", analyze_startup)
workflow.add_node("plan_mvp", plan_mvp)
workflow.add_node("plan_milestones", plan_milestones)
workflow.add_node("plan_roadmap", plan_roadmap)
workflow.add_node("plan_hiring", plan_hiring)
workflow.add_node("build_final_plan", build_final_plan)

workflow.add_edge(START, "analyze_startup")
workflow.add_edge("analyze_startup", "plan_mvp")
workflow.add_edge("plan_mvp", "plan_milestones")
workflow.add_edge("plan_milestones", "plan_roadmap")
workflow.add_edge("plan_roadmap", "plan_hiring")
workflow.add_edge("plan_hiring", "build_final_plan")
workflow.add_edge("build_final_plan", END)

graph = workflow.compile()