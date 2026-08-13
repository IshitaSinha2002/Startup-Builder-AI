from graph.workflow import graph


def main():
    startup_idea = input("Enter your startup idea: ").strip()

    if not startup_idea:
        print("Startup idea cannot be empty.")
        return

    initial_state = {
        "startup_idea": startup_idea
    }

    result = graph.invoke(initial_state)

    print("\n" + "=" * 60)
    print("STARTUP BUILDER")
    print("=" * 60)

    print("\nSTARTUP ANALYSIS")
    print(result["startup_analysis"].model_dump_json(indent=2))

    print("\nMVP STRATEGY")
    print(result["mvp_strategy"].model_dump_json(indent=2))

    print("\nMILESTONES")

    for milestone in result["milestones"]:
        print(f"\n{milestone.name}")
        print(f"Objective: {milestone.objective}")

        print("Key Tasks:")
        for task in milestone.key_tasks:
            print(f"- {task}")

        print("Success Criteria:")
        for criteria in milestone.success_criteria:
            print(f"- {criteria}")

    print("\nROADMAP")

    for item in result["roadmap"]:
        print(f"\n{item.phase}")
        print(f"Timeline: {item.timeline}")
        print(f"Priority: {item.priority}")

        print("Objectives:")
        for objective in item.objectives:
            print(f"- {objective}")

        print("Dependencies:")
        if item.dependencies:
            for dependency in item.dependencies:
                print(f"- {dependency}")
        else:
            print("- None")

    print("\nHIRING PLAN")

    for role in result["hiring_plan"].roles:
        print(f"\n{role.role}")
        print(f"Hiring Stage: {role.hiring_stage}")
        print(f"Reason: {role.reason}")

        print("Responsibilities:")
        for responsibility in role.responsibilities:
            print(f"- {responsibility}")

    print("\nFINAL STARTUP PLAN")

    final_plan = result["final_plan"]

    print(f"\nExecutive Summary:\n{final_plan.executive_summary}")

    print(f"\nStartup Direction:\n{final_plan.startup_direction}")

    print("\nImmediate Priorities:")
    for priority in final_plan.immediate_priorities:
        print(f"- {priority}")

    print("\nKey Risks:")
    for risk in final_plan.key_risks:
        print(f"- {risk}")

    print("\nNext Steps:")
    for step in final_plan.next_steps:
        print(f"- {step}")


if __name__ == "__main__":
    main()