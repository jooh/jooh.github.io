---
Title: Vibing this blog back to life
Date: 2026-01-21 17:18
Status: published
Tags: ai, codex, pelican
Summary: Codex Web is clunky yet strangely addictive, as I learned when vibing a blog refresh from a sun lounger over the holidays
---

I’ve been rebooting this blog. What started as a vague intention to clean things up a bit turned into a more interesting experiment in agentic development, vibe coding, and finding the strengths and limitations of Codex Web, ChatGPT's browser-based tool for vibing code.

## What’s changed so far

Using Codex Web (formerly Codex Cloud) I’ve managed to modernise the blog quite a bit, without touching a computer keyboard. Pretty much all this work got done on my phone from a sun lounger in Mexico, whenever I had 5 minutes to myself. Here's what changed:

- Replaced a handcrafted dev/build environment on my old laptop with a proper CI/CD pipeline
- Updated all dependencies to current versions
- Added a version tag to the footer so I can see which version is live
- Introduced a CMS setup using Svelte

This was an interesting exercise. Codex Web is addictive, even with its limitations.

## Codex Web and its constraints

The first major insight is that Codex Web is meaningfully more constrained than a full agent experience like the Codex CLI application.

### Closing the agentic feedback loop

I haven't seen Codex Web successfully deliver large, sweeping changes in a single task. At no point did it [port a library to a new language](https://lucumr.pocoo.org/2026/1/14/minijinja-go-port/) or anything in that vein. Instead, each task tends to result in a pull request that is borderline too small. If you look at the commit history, which you can find via the GitHub link on [johancarlin.com](https://johancarlin.com), you will see a long series of small pull requests that collectively make up the refresh. I think we are somewhere around 20 pull requests at this point, rather than a single big one.

A big part of why Codex Web tops out at small changes is the lack of a closed feedback loop. Codex can run tests inside its sandboxed environment, but what it does not do is continuously observe the external system it is modifying. I couldn't get it to push to GitHub, so I couldn't get it into a loop where it inspects the rendered output, and then refines its solution based on what it sees.

Similarly, Codex Web has no way to access GitHub Actions output, so when it broke the build I was stuck copying and pasting logs into tasks.

### Handling upstream changes

When you create a task, Codex Web spins up a sandboxed remote environment, checks out the current default branch of your repository, and creates a detached working copy from that snapshot. All edits happen against that initial state.

The important limitation is that this working copy does not stay in sync with upstream changes. If new commits land on the default branch while the task is running, Codex Web does not appear to have a way to pull those changes in and rebase or merge them as part of the same session.

In practice, this means merge conflicts can arise quite easily if you are iterating quickly or running multiple tasks in parallel. When that happens, there is no obvious way for Codex Web to resolve those conflicts inside the existing task.

At that point you have two options:

1. Check out the branch locally and resolve the conflicts yourself, or
2. Start a new Codex task with the same prompt, letting it run again against the updated default branch

I mostly just used the second approach since I was on a sun lounger, and it worked quite well since the tasks were small overall.

This limitation is unfortunate though because a big benefit over native CLI tools is that you can easily spawn off any number of tasks in parallell sessions. I learned not to run too many tasks in parallel to avoid these merge conflicts, and that limits productivity.

## And yet, it’s still addictive

Despite all of that, I keep coming back to it.

There isn't even an Android app for Codex Web yet (it isn't integrated into ChatGPT on Android). I have been using it through a fairly clunky mobile web interface with noticeable lag. Still, over the holidays, I found myself using it constantly.

There is something extremely compelling about being able to fire off a task from your phone in between everyday life and just have it execute. That experience is hard to beat, and it makes you surprisingly tolerant of rough edges.

In a way, the small-task model that Codex Web steers you toward helps. You get an idea for something minor, you send it off to Codex, and when you come back later it is usually done. That cadence fits well into real life.

## Where this is heading next

Now that the blog is set up with a CMS, the next focus is on making it easier to actually write and publish posts.

With the Sveltia-based CMS in place, I no longer need to manually write a Markdown file and commit it to the repository. I can just type directly into the CMS. And I'm hoping to do less typing overall in fact.

The plan is to lean heavily on dictation. This very post was drafted using ChatGPT’s dictation feature. I record posts by rambling away, have ChatGPT clean up and generate the corresponding Markdown, and then copy-paste that straight into the CMS for final manual editing.

Overall, this has been a lot of fun and I think it's going to mean more updates here! Famous last words.
