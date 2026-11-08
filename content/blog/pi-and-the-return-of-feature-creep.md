---
Title: Pi and the return of feature creep
Date: 2026-11-08
Status: draft
Tags: ai, pi, agents, vibe coding
Summary: Minimalist foundations, maximalist extensions, and the measured weight of adding web search, subagents, and planning to Pi.
---

## Thesis: minimalism stops at the core

- [Pi's philosophy](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/): deliberate restraint.
- Subagents and planning: delegated to extensions.
- Minimalist foundation; maximalist additions.
- Vibe coding makes additions cheap.
- Restraint remains expensive.

## Example: "I just wanted web search"

### [pi-web-access](https://github.com/nicobailon/pi-web-access)

- Search becomes content-processing infrastructure.
- Multiple providers; elaborate fallback chains.
- GitHub cloning; PDF extraction.
- YouTube and local-video analysis.
- Browser-cookie authentication; curator UI.
- Optional ffmpeg, yt-dlp, Git, gh.
- **Adds 88 MiB; 211 npm packages.**

## Example: "I just wanted another agent"

### [pi-subagents](https://github.com/nicobailon/pi-subagents)

- Delegation becomes workflow orchestration.
- Saved workflows; repeated review loops.
- Fleet dashboard; transcript inspection.
- Watchdog reviews; acceptance gates.
- Durable missions; recurring schedules.
- An extension with extension APIs.
- **Adds 23 MiB; seven npm packages.**
- Broad scope; modest dependency footprint.

## Example: "I just wanted planning before editing"

### [Plannotator](https://github.com/backnotprop/plannotator/tree/main/apps/pi-extension)

- Planning becomes a review workspace.
- Plans, code, documents, agent messages.
- Live HTML annotation; inbox integration.
- Browser terminal stack; diagram rendering.
- **Adds 214 MiB; 71 npm packages.**
- More than doubles Pi's footprint.

### What arrives with planning?

- Native pseudoterminal addon: `node-pty`.
- Linux install requires native compilation.
- Python, make, C++ compiler.
- Windows binaries shipped on Linux.
- Icon-package files: **35 MiB**.
- Two browser interfaces: **40 MiB**.
- Bun needed only for source builds.

## Measuring the accumulated weight

Clean npm installations; Linux x86-64; Node 24.22.1; measured 8 November 2026.

| Installation | Total disk | Added disk | Added npm packages |
|---|---:|---:|---:|
| Pi 1.5.0 alone | 157.6 MiB | — | — |
| + Web access 0.47.0 | 245.8 MiB | 88.1 MiB | 211 |
| + Subagents 0.87.0 | 180.2 MiB | 22.6 MiB | 7 |
| + Plannotator 0.28.51 | 371.1 MiB | 213.5 MiB | 71 |
| + All three | 472.9 MiB | 315.3 MiB | 287 |

*Allocated disk space; excludes Node/npm, caches, and system tools. Package counts include each extension and transitive dependencies. Pi alone contains 123 packages; combined installation shares some dependencies.*

## The batteries-included impression

### [oh-my-pi](https://github.com/can1357/oh-my-pi)

- Separate fork; distinct product choices.
- LSP, debugger, browser, desktop control.
- Image generation; speech; memory systems.
- Easy to mistake the bundle for Pi.
- Attribute complexity to the installation.
- Comparative bug claims need evidence.

## Conclusions: minimalism requires continuing decisions

- Extension boundaries don't enforce restraint.
- Optional features still ship dependencies.
- Packaging overhead also matters.
- Disk size doesn't establish bad design.
- Feature scope doesn't predict package count.
- Cheap implementation; continuing maintenance costs.
- Pi preserves the choice to stay small.
- Installing everything defeats that advantage.
