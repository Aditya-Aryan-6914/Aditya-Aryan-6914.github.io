---
title: "Your First Open Source Contribution: The Fork, Branch and Pull Request Workflow"
date: 2026-09-28
category: Open Source
tags: [open-source, git, github, beginners]
description: "A practical guide to making your first open source contribution, from picking a documentation issue to opening a clean pull request that maintainers can merge."
---

Open source looks intimidating from the outside. Big projects, strangers reviewing your code, unfamiliar tooling. The good news is that the workflow is the same for almost every project, and your first contribution does not need to be code. Fixing documentation is a real, valuable and welcome way to start. This is the process I follow when contributing to projects.

## Why start with documentation

Maintainers rarely have time to polish docs, so typos, broken links, unclear steps and outdated commands pile up. Fixing them teaches you the whole contribution cycle with very little risk: finding an issue, forking, branching, committing, opening a pull request and responding to review. Once that loop feels natural, code contributions become much less scary.

## Step 1: Find a project and read the rules

Pick a project you actually use or are curious about. Before touching anything, read these files in the repository:

- `README.md` to understand what the project does.
- `CONTRIBUTING.md` for the rules about branches, commit messages and tests.
- `CODE_OF_CONDUCT.md` so you know the expected behaviour.

Then open the **Issues** tab and look for labels such as `good first issue`, `documentation` or `help wanted`.

## Step 2: Claim the issue

Comment on the issue before you start, for example: "I would like to work on this. Is it still open?" This avoids two people doing the same work and shows respect for the maintainers' time.

## Step 3: Fork and clone

Click **Fork** on GitHub to create your own copy, then clone *your fork*:

```bash
git clone https://github.com/your-username/project.git
cd project
git remote add upstream https://github.com/original-owner/project.git
```

The `upstream` remote points to the original repository so you can stay in sync with it.

## Step 4: Create a branch

Never work on `main`. Create a descriptive branch:

```bash
git checkout -b docs/fix-install-instructions
```

## Step 5: Make a small, focused change

Keep the change tiny and related to one issue. A pull request that fixes one thing is far easier to review than one that fixes ten. Build or preview the docs locally if the project allows it, and follow the existing style.

## Step 6: Commit with a clear message

```bash
git add .
git commit -m "docs: fix outdated install command in README"
```

Some projects require a sign-off on every commit (the Developer Certificate of Origin). If the contributing guide mentions it, add `-s` to your commit command.

## Step 7: Push and open the pull request

```bash
git push origin docs/fix-install-instructions
```

GitHub will show a button to **Compare & pull request**. In the description, explain what you changed and why, and link the issue with a line such as `Fixes #123`.

## Step 8: Handle review feedback

Reviewers may ask for changes. That is normal and not a rejection. Make the edits on the same branch, commit and push again, and the pull request updates automatically. Reply politely, and if you disagree, explain your reasoning calmly.

## Keeping your fork in sync

Before starting new work, update your fork:

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

## What I learned from contributing

Reading other people's code and reviews taught me more than many tutorials. Even a small documentation fix teaches you how real projects are organised, how maintainers think and how to communicate clearly in writing. Start small, be patient with slow replies and keep going. Your second pull request will feel far easier than your first.
