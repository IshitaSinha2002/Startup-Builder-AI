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