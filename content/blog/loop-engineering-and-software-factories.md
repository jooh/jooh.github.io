---
Title: Loop Engineering and Software Factories
Date: 2026-10-17 13:57
Status: draft
---

### Introduction: The software factory trap

* Anecdote: Two vibe-coded software factory startups presented at an agentic AI meetup in Stockholm.

* Both emphasized how extensively they used AI to build their factories.

* Echoes Chris Yegge's observation that Gastown was primarily useful for developing Gastown itself.

* Many developers have followed a similar progression toward increasingly sophisticated agentic engineering.

* At the extreme, the factory becomes so complicated that it's mostly useful for developing itself.

* Central question: How do we progress through these levels, and how do we escape the trap?

### Level 1: Manual prompting

* Separate planning from implementation.

* Manually prompt each stage: Plan → Build → Review → Fix → PR → Fix CI → Merge.

* The developer orchestrates an otherwise predictable process.

### Level 2: Structured prompting and agentic loops

* Develop shorthand prompts that trigger larger workflows.

* Examples:

    * Planning: "Write a spec."

    * Documentation: "Use STE."

    * Building: Simon Willison's "Use Red-Green TDD."

    * Reviewing: "Use sub-agents to review, fix issues, repeat until no issues above P2 remain."

    * Delivery: "Babysit CI until green."

* Modern agents can execute substantial iterative workflows from brief instructions.

* The meat proxy problem: Once planning is complete, human intervention largely consists of repeating predictable instructions.

### Level 3: Skills as orchestration

* Combine recurring prompts into reusable skills.

* Example: `Orchestrate.md` describes the entire development lifecycle.

* Plan → Build with sub-agents → Review/fix loop → Draft PR → Fix CI → Publish/merge.

* Works reasonably well, but delegates orchestration to the LLM.

* Analogous to asking an LLM to perform calculations rather than giving it a calculator.

* Problems:

    * Nondeterministic execution and forgotten instructions.

    * Context-window exhaustion, sometimes from unnecessary file reads.

    * Requires powerful models; weaker models struggle.

    * Expensive token consumption from orchestrating sub-agents.

### Level 4: The software factory — here be dragons

### A qualitative leap in complexity

* Until now, loop engineering has primarily involved prompting and understanding agent capabilities.

* A software factory requires actual software engineering.

* Suddenly confronting difficult problems:

    * Persistent execution and recovery after restarts.

    * Parallel execution and coordination of workers.

    * Git worktree management and isolation.

    * Workflow state and progress tracking.

    * Idempotency and exactly-once execution.

* Even a simple pipeline triggered by committing `plan.md` raises difficult distributed computing questions.

* Prompting an agent to build this system is easy; obtaining something maintainable is not.

### My graveyard of failed software factories

* Four months experimenting with multiple proofs of concept, none entirely satisfactory.

* Attempt 1: Custom Python implementation

    * Agent builds worktree management, orchestration, lifecycle handling, etc.

    * Produces thousands of lines of code and extensive tests.

    * Effectively implements complex infrastructure from scratch.

* Attempt 2: Persistent execution frameworks

    * DBOS and Temporal offer existing orchestration and persistence capabilities.

    * But implementations become tightly coupled to one particular development workflow.

* Attempt 3: General-purpose workflow abstractions

    * Desire to support arbitrary agentic development loops.

    * Explore abstractions inspired by Dagster's software-defined assets, decorated functions, Temporal/DBOS primitives, DSLs, and YAML.

    * The abstraction itself becomes another substantial engineering problem.

* Each iteration reveals more complexity rather than producing a simple, satisfactory solution.

### The problem with off-the-shelf software factories

* Thousands of software factory projects now exist on GitHub.

* Many are themselves vibe-coded and architecturally questionable.

* Hard to find something materially better than simply prompting Claude directly.

* Recurring failure mode: Agents implement complex infrastructure ad hoc, often using standard libraries and large amounts of custom code.

* The resulting applications grow into sprawling, tightly coupled systems.

### The escape: Composition instead of implementation

### Reuse substantial components

* Sound software engineering means composing existing components, not rebuilding everything.

* Delegate complexity to mature, specialized tools.

* Write only the integration code and genuinely missing functionality.

* Examples of components to reuse:

| Concern                           | Reusable components                              |
| --------------------------------- | ------------------------------------------------ |
| Persistent execution              | Temporal, DBOS                                   |
| Worker execution                  | Dagger, Tekton Pipelines, existing CI/CD runners |
| Coding agent harness              | Pi, Pydantic AI                                  |
| Model routing and authentication  | LiteLLM, Bifrost, other LLM gateways             |
| Integration with the parent agent | MCP, potentially MCP Tasks                       |

### Decouple the coding harness from the model

* Many factories implement separate integrations for Claude Code, Codex, and numerous other harnesses.

* This creates unnecessary complexity and tight coupling.

* Models are not intrinsically tied to their vendors' coding harnesses.

* Minimal harnesses such as Pi perform strongly in agentic evaluations.

* Model providers need their models to work in arbitrary API-based applications.

* Prefer one general-purpose harness capable of running different models.

### Move model integration to an LLM gateway

* Avoid implementing provider-specific APIs, authentication, and model selection inside the factory.

* Standardize on an OpenAI-compatible API.

* Configure a gateway endpoint and authentication method.

* Delegate provider integration and model routing to the gateway.

* Keep these concerns entirely separate from development orchestration.

### The broader lesson: Vibe coding and software architecture

### The limits of personal software

* The early vibe-coding enthusiasm around personal software: simply prompt agents to build whatever tools you need.

* Pi partly embodies this philosophy.

* Works for smaller tools, but complex applications remain difficult to engineer.

* Agents cannot reliably one-shot a sophisticated distributed application with a maintainable architecture.

* The resulting custom code becomes substantial technical debt.

### Code is still a liability

* Lines of code should still be regarded as maintenance debt.

* Agents make it dangerously easy to generate thousands of lines of code.

* Large agent-generated codebases become difficult for both humans and agents to understand and maintain.

* Minimizing the amount of code you own is more important than ever.

* Modularity, loose coupling, and reusable components are essential counterweights to uncontrolled code generation.

### Architecture becomes the critical human contribution

* Sound software engineering principles haven't changed.

* Understand which components are required and which existing tools can provide them.

* Design clean interfaces and minimize coupling.

* Agentic coding is powerful at implementation, but does not independently guarantee good architecture.

* Human domain expertise remains essential at this higher level of abstraction.

* The central engineering challenge shifts toward choosing and composing the right components.

### The final level: A software factory that isn't a factory

* Emerging conclusion from repeated failed experiments: The ideal software factory contains very little custom software.

* Rather than building a monolithic application, assemble existing tools:

    * Expose agentic workflows through MCP, potentially using MCP Tasks.

    * Use existing CI/CD infrastructure for isolated worker execution.

    * Use a generic coding harness such as Pi.

    * Use established persistent execution infrastructure where needed.

    * Delegate model access to an LLM gateway.

* The factory becomes a collection of loosely coupled components with a small amount of glue code.

* Building this requires knowing the available tools and understanding how they should fit together.

* That architectural understanding cannot simply be replaced with a single prompt.

### Conclusion: Breaking out of the loop

* The progression from prompting to software factories exposes the limits of vibe coding.

* Each abstraction initially promises to eliminate repetitive human work, but can introduce new engineering complexity.

* Building a software factory can become an end in itself.

* The escape is not to build an increasingly sophisticated factory, but to avoid building most of it in the first place.

* Agentic engineering reinforces rather than replaces the fundamentals: clear architecture, modularity, reuse, loose coupling, and minimal custom code.
