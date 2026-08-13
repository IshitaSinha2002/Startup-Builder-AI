STARTUP_ANALYSIS_PROMPT = """
You are a startup strategy expert.

Analyze the following startup idea:
{startup_idea}

Identify:
1. The core problem being solved
2. The target customers
3. The proposed solution
4. The unique value proposition
5. The likely business model
6. The main assumptions that need validation
7. The biggest risks

Return your response as a structured analysis.
"""


MVP_STRATEGY_PROMPT = """
You are an experienced startup product strategist.

Based on the startup idea and startup analysis below, design a focused MVP.

Startup Idea: {startup_idea}
Startup Analysis: {startup_analysis}

Determine:
1. The primary goal of the MVP
2. The essential features required for the MVP
3. Features that should be deliberately postponed
4. The target users for the MVP
5. The best ways to validate whether the MVP solves the problem

Keep the MVP focused. Avoid adding features that are not necessary
to validate the core startup hypothesis.
"""


MILESTONE_PLANNING_PROMPT = """
You are an experienced startup execution strategist.

Create a set of practical milestones for the follwing startup.

Startup Idea: {startup_idea}
Startup Analysis: {startup_analysis}
MVP Strategy: {mvp_strategy}

Create milestones that take the startup from early validation
through MVP development and initial market launch.

For each milestone provide:
1. A concise milestone name
2. The primary objective
3. The key tasks required
4. Measurable success criteria

Make the milestones sequential and realistic.
Avoid vague milestones such as "work on the product"
"""


ROADMAP_PLANNING_PROMPT = """
You are an experienced startup operations and execution strategist.

Create a practical roadmap for the startup using the information below.

Startup Idea: {startup_idea}
Startup Analysis: {startup_analysis}
MVP Strategy: {mvp_strategy}
Milestones: {milestones}

Turn the milestones into a sequential roadmap.

For each roadmap phase provide:
1. Phase name
2. Estimated timeline
3. Priority
4. Main objectives
5. Dependencies on earlier phases

The roadmap should be realistic for an early-stage startup.
Prioritize validation and the MVP before expansion or scaling.
"""


HIRING_PLAN_PROMPT = """
You are an experienced startup hiring strategist.

Create a lean hiring plan based on the startup's strategy and roadmap.

Startup Idea: {startup_idea}
Startup Analysis: {startup_analysis}
MVP Strategy: {mvp_strategy}
Roadmap: {roadmap}

Determine the key roles the startup should hire.

For each role provide:
1. Role name
2. Main responsibilities
3. The startup stage when the role should be hired
4. Why the role is needed at that stage

Keep the team lean.

Do not recommend hiring roles that are unnecessary
for the current stage of the startup.
Prioritize roles that directly contribute to building,
launching, validating, and growing the product.
"""


FINAL_PLAN_PROMPT = """
You are a startup advisor creating the final execution plan for a founder.

Use all of the planning information below.

Startup Idea: {startup_idea}
Startup Analysis: {startup_analysis}
MVP Strategy: {mvp_strategy}
Milestones: {milestones} 
Roadmap: {roadmap}
Hiring Plan: {hiring_plan}

Create a concise but actionable final startup plan.

Include:
1. Executive summary of the startup
2. Recommended strategic direction
3. The most important immediate priorities
4. The key risks the founder should monitor
5. The concrete next steps to begin execution

Make sure the final recommendations are consistent with
the MVP strategy, milestones, roadmap, and hiring plan.
Do not introduce major ideas that were not supported by
the earlier analysis.
"""