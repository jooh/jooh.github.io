---
Title: The pi coding harness is minimalistic but its extensions sure aren't
Date: 2026-11-08
Status: draft
Tags: ai, pi, agents, vibe coding
Summary: Exploring the tension between a minimalistic harness and the feature-creeped extensions that popped up to fill the gap
---

Pi is an amazing coding harness. It is delightfully [minimalistic](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/). Instead of implementing common harness features like plan mode, subagents, or even web search it provides an extension system and a skill (CODEX: LINK TO THIS SKILL ON EG PI'S GH) that makes it incredibly easy to vibe up your own.

There is however a delightful irony in all this. Pi's minimalist philosophy is thoroughly trampled by the most popular extensions on the marketplace (CODEX: LINK TO THE PI EXTENSION MARKETPLACE THING HERE AND MAKE SURE I USE THE RIGHT TERM FOR IT), which tend to be feature creeped beyond all recognition. Load up Pi with a few of these and suddenly your lightweight harness is full off bells and whistles, many of which are not well conceived or engineered. There is a useful lesson here about how to checkity check yourself before you wreck yourself with agentic development, so let's explore two popular examples from the marketplace.

## Disclaimer

I want to state at the outset that I have a lot of respect for the developers of these extensions that I'm about to lay into. They are popular for a reason. They work well and fill a real need in the community. But at the same time, they are examples of the kind of feature creep that agentic coding invites.

## So you want to search the web in pi

Pi's stubborn refusal to add web search (CODEX: LINK TO RELEVANT GH ISSUE ON PI REPO) is frustrating but understandable. Web search is a really useful way to enable your agent to work with code that is too new or obscure to feature in the training data. But there are many search providers and the whole Pi philosophy is to avoid making decisions for the user.

So what do you get if you instead install the by-far most popular extension for this, [pi-web-access](https://github.com/nicobailon/pi-web-access)? Well, you add 88 MiB to your pi install and 211 npm packages. For this, you get X search providers (CODEX: GIVE ME THE EXACT UP TO DATE NUMBER), with a complex set of built-in fallback behaviours if one is unavailable. You get custom behaviour for github (repos get checked out and searched over locally), PDF content extraction, YouTube video content analysis, and so on.

This is arguably insane. 99% of the use case is solved by standard text search through an external provider like Exa (CODEX: LINK), or by just wiring searches through the Responses API for providers that support this like OpenAI (CODEX: LINK TO SOURCE FOR THIS WAY OF SEARCHING). The only search extension I would recommend (CODEX: FIND THE EXTENSION, IT'S ONE I HAVE FORKED TO MY PERSONAL GITHUB) implements only the provider-native search route.

But in fact, with the recent addition of MCP as a native tool (CODEX: LINK TO BLOG POST ON THIS FROM EARENDIL), you don't need any extensions at all. Just install Exa MCP and you have search.

## So you want subagents in pi

Subagents is another popular feature the pi developers have refused to implement so far (CODEX: LINK TO GH ISSUE FOR THIS). I'm less sympathetic to this call. With the recent addition of codemode (CODEX: FIND LINK TO THIS FROM DEVELOPER BLOG OR RELEASE NOTES), you can now orchestrate tool calls like MCP in blocks of typescript. That puts us tantalisingly close to having a capable subagent implementation if the developers would just add that tool as well...

Anyway, subagents is a somewhat complicated extension to DIY so you probably reach for [pi-subagents](https://github.com/nicobailon/pi-subagents) instead. It looks reasonably lightweight at 23 MiB extra size and a merge 7 npm packages. But the feature set is anything but, because you end up with a full-on software factory. You get

* Several pre-defined agents with somewhat nebulous roles
* Several workflows (basically skills that instruct the agent to run sub agents in a particular pattern)
* A watchdog (basically a sub agent that reviews each change by the main agent)
* Missions, runs and records (basically attempts to manage overall project state natively within in the extension)
* Scheduling of runs

In fairness, not all of this is enabled by default, but enough of it is added to the agent's prompt that you will see some exciting dynamic behaviors if you so much as utter the word "sub agents" in one of your prompts.

I don't want to be negative! A lot of these features sound cool and might be really useful! But did they all need to get bundled in the same extension?

So what should you use for subagents instead? Honestly I'm not sure. If anyone has found a well-designed yet minimalistic extension for this let me know! I live in hope that the pi maintainers eventually will provide a basic ˋsubagentˋ tool with a native TUI.

## What have we learned about agentic engineering today

The point of all this isn't to pick on these specific developers. It's just that these extensions show so clearly what can happen to a codebase when the next feature is a prompt away. People talk a lot about a comprehension gap that results when the developer loses grip on the code, but if you take this far enough you also end up with products that have so many features that the *end user* struggles to reason effectively about what the program's behaviour and capabilities are. I struggle with this myself constantly at ˋ$day_jobˋ and I wish I could talk more about those experiences here.

Agents are not good at designing modular solutions with loose coupling between the components. Agents are not good at creating new functionality as the combination of a set of modular tools. Agents are never going to respond to your latest prompt with a YAGNI (CODEX: LINK WIKI HERE). The only way to stave off full agentic psychosis is to build tastefully. That might mean coding a lot less and researching and thinking a lot more than we're used to as developers.
