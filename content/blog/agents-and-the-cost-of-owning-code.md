---
Title: Just because agents can build it doesn't mean you should own it
Date: 2026-11-07 22:00
Status: draft
Tags: agents, software engineering
Summary: Why cheap code makes composition more important, even when agents can build everything from the standard library.
---

Agents make it possible to build an entire application on the standard library. That doesn't make maintaining it a good use of your time.

## Code is still a liability

* Cheap implementation; ongoing maintenance debt.
* Standard libraries are useful; rebuilding mature infrastructure is a choice.
* More generated code; more to understand, debug, and secure.
* Own the missing functionality; reuse the rest.

## Composition instead of implementation

### Reuse substantial components

* Sound software engineering means composing existing components, not rebuilding everything.

* Delegate complexity to mature, specialized tools.

* Write only the integration code and genuinely missing functionality.

* Examples of components to reuse:

| Concern | Reusable components |
| --- | --- |
| Persistent execution | Temporal, DBOS |
| Worker execution | Dagger, Tekton Pipelines, existing CI/CD runners |
| Coding agent harness | Pi, other existing coding harnesses |
| Model routing and authentication | LiteLLM, Bifrost, other LLM gateways |
| Integration with the parent agent | MCP, potentially MCP Tasks |

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

## A software factory with very little custom software

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
