---
layout: page
permalink: /guides/guide_git/
title: Git
tags: [git]
comments: false
---
Git - the ultimative version control system.
(Actually it is the only one I ever bothered to grasp.)
This guide is probably best suited for people that already use git in their daily coding-life
but never really had a full understanding what 'exactly' is happening behind the scenes.

This guide tries to explain the basics of git in two a very simple steps.
Let's get started.

### Number 1: The three areas of git
1. Working directory
2. Staging area
3. Repository

The working directory is basically what you have if you wouldn't use any version control at all.
I hope the repository is clear. In general we "commit" changes from the working directory into the repository.
The staging area is a nifty little concept that allows us to specify exactly which changes we want to add to a particular commit.

#### How to show the difference between these areas?
- git diff
- git diff --staged

#### How to move changes from one area to another
Working dir --> Staging area: git add <file>
Staging area --> Repository:  git commit -m "<commit message>"

### Number 2: The Git Tree
- Directed graph.
- Nodes are commits.
- Edges allow to go back on a specific branch.
- A "branch" is really just a node/commit with a human-readable name instead of the cryptic commit-id.
  - Also a specific branch is just the name of the HEAD of that branch.

### Number 3: Remote Repositories
- Ok this is number 3 although I promised to keep it down to two. In fact, this section does not introduce any new concepts.
It's really just the three areas and the git tree.

git fetch
git merge master origin/master

same as
git pull

git push 
