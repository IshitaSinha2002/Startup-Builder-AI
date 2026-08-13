<h1>Startup Builder</h1>

<p>
Startup Builder is a stateful LLM workflow built using LangChain and LangGraph that analyzes a startup idea and transforms it into a structured execution plan covering MVP strategy, milestones, roadmap, hiring, and next steps.
</p>

<h2>Overview</h2>

<p>
The system takes a startup idea as user input and processes it through a sequential planning workflow. Each stage enriches a shared LangGraph state, allowing subsequent stages to build on the reasoning and outputs generated earlier.
</p>

<p>
The workflow is designed as a planning system rather than a multi-agent system. Each node has a specific responsibility and executes in a defined sequence.
</p>

<h2>Workflow</h2>

<pre>
Startup Idea
     |
     v
Startup Analyzer
     |
     v
Startup Analysis
     |
     v
MVP Planner
     |
     v
MVP Strategy
     |
     v
Milestone Planner
     |
     v
Milestones
     |
     v
Roadmap Planner
     |
     v
Roadmap
     |
     v
Hiring Planner
     |
     v
Hiring Plan
     |
     v
Final Plan Builder
     |
     v
Final Startup Plan
</pre>

<h2>Features</h2>

<ul>
  <li>Analyzes a startup idea and identifies the core problem and target customers.</li>
  <li>Defines a focused MVP strategy.</li>
  <li>Generates sequential startup milestones.</li>
  <li>Creates a timeline-based product roadmap.</li>
  <li>Generates a stage-based hiring plan.</li>
  <li>Produces a consolidated final startup plan.</li>
  <li>Uses structured LLM outputs with Pydantic models.</li>
  <li>Maintains shared state across all workflow stages using LangGraph.</li>
  <li>Accepts startup ideas dynamically through user input.</li>
</ul>

<h2>Tech Stack</h2>

<ul>
  <li>Python 3.12</li>
  <li>LangChain</li>
  <li>LangGraph</li>
  <li>Groq</li>
  <li>Llama 3.3 70B Versatile</li>
  <li>Pydantic</li>
  <li>python-dotenv</li>
</ul>

<h2>Project Structure</h2>

<pre>
startup-builder/
|
├── main.py
├── requirements.txt
├── .env
├── .gitignore
|
├── graph/
│   ├── __init__.py
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
|
└── prompts/
    ├── __init__.py
    └── prompts.py
</pre>

<h2>Architecture</h2>

<h3>Shared State</h3>

<p>
The workflow uses a shared <code>StartupState</code> object to maintain information throughout the execution. Each node reads relevant information from the state and adds its own output.
</p>

<pre>
StartupState
|
├── startup_idea
├── startup_analysis
├── mvp_strategy
├── milestones
├── roadmap
├── hiring_plan
└── final_plan
</pre>

<h3>Workflow Nodes</h3>

<table>
  <tr>
    <th>Node</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td>Startup Analyzer</td>
    <td>Analyzes the startup problem, customers, solution, business model, assumptions, and risks.</td>
  </tr>
  <tr>
    <td>MVP Planner</td>
    <td>Defines the MVP goal, core features, deferred features, target users, and validation strategy.</td>
  </tr>
  <tr>
    <td>Milestone Planner</td>
    <td>Converts the startup strategy into sequential milestones with tasks and success criteria.</td>
  </tr>
  <tr>
    <td>Roadmap Planner</td>
    <td>Transforms milestones into a timeline-based roadmap with priorities and dependencies.</td>
  </tr>
  <tr>
    <td>Hiring Planner</td>
    <td>Determines which roles are needed and at which stage of the startup.</td>
  </tr>
  <tr>
    <td>Final Plan Builder</td>
    <td>Combines all generated information into a concise final startup execution plan.</td>
  </tr>
</table>

<h2>Structured Output</h2>

<p>
The workflow uses Pydantic models to constrain LLM responses into predictable structures. This allows information to be reliably passed between workflow nodes.
</p>

<p>
Examples of structured models include:
</p>

<ul>
  <li><code>StartupAnalysis</code></li>
  <li><code>MVPStrategy</code></li>
  <li><code>Milestone</code></li>
  <li><code>RoadmapItem</code></li>
  <li><code>HiringRole</code></li>
  <li><code>FinalStartupPlan</code></li>
</ul>

<h2>Setup</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone &lt;repository-url&gt;
cd startup-builder
</pre>

<h3>2. Create a Python 3.12 Virtual Environment</h3>

<pre>
py -3.12 -m venv .venv
</pre>

<h3>3. Activate the Virtual Environment</h3>

<p>Windows PowerShell:</p>

<pre>
.venv\Scripts\Activate.ps1
</pre>

<h3>4. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>5. Configure the Groq API Key</h3>

<p>
Create a <code>.env</code> file in the project root:
</p>

<pre>
GROQ_API_KEY=your_groq_api_key
</pre>

<h2>Running the Project</h2>

<p>Run:</p>

<pre>
python main.py
</pre>

<p>The application will ask:</p>

<pre>
Enter your startup idea:
</pre>

<p>Enter any startup idea and the workflow will generate:</p>

<ul>
  <li>Startup Analysis</li>
  <li>MVP Strategy</li>
  <li>Milestones</li>
  <li>Roadmap</li>
  <li>Hiring Plan</li>
  <li>Final Startup Plan</li>
</ul>

<h2>Example</h2>

<pre>
Enter your startup idea: AI-powered platform that helps small businesses automate customer support
</pre>

<p>The system analyzes the idea and generates a structured execution plan covering product validation, MVP development, launch milestones, roadmap phases, hiring requirements, risks, and immediate next steps.</p>

<h2>LangGraph Design</h2>

<p>
The workflow is implemented as a sequential LangGraph state graph:
</p>

<pre>
START
  |
  v
analyze_startup
  |
  v
plan_mvp
  |
  v
plan_milestones
  |
  v
plan_roadmap
  |
  v
plan_hiring
  |
  v
build_final_plan
  |
  v
END
</pre>

<p>
Each node updates the shared <code>StartupState</code>, allowing downstream nodes to access information generated by earlier stages.
</p>

<h2>Key Concepts Demonstrated</h2>

<ul>
  <li>Stateful LLM workflows</li>
  <li>LangGraph state management</li>
  <li>Sequential workflow orchestration</li>
  <li>LangChain LLM integration</li>
  <li>Groq model integration</li>
  <li>Structured LLM output</li>
  <li>Pydantic schemas</li>
  <li>Prompt-based reasoning</li>
  <li>Workflow node design</li>
  <li>Dependency-aware planning</li>
</ul>

<h2>Future Improvements</h2>

<ul>
  <li>Add conditional routing based on startup stage.</li>
  <li>Add budget and resource constraints.</li>
  <li>Improve roadmap estimation using team size and available resources.</li>
  <li>Add founder and existing-team inputs to improve hiring recommendations.</li>
  <li>Add LangGraph checkpointing for persistent workflows.</li>
  <li>Add a web interface for startup planning.</li>
  <li>Export the generated plan as PDF or Markdown.</li>
</ul>
