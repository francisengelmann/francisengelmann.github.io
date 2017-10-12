---
layout: page
permalink: /guides/git/
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

![slurm]({{ site.url }}/guides/images/git_three_areas.png)


1. Working directory
2. Staging area
3. Repository

The working directory is basically what you have if you wouldn't use any version control at all.
I hope the repository is clear. In general we "commit" changes from the working directory into the repository.
The staging area is a nifty little concept that allows us to specify exactly which changes we want to add to a particular commit.

#### How to show the difference between these areas?
- git diff
- git diff --staged
- git featch, git diff origin/master

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

### Commands

`git remote add <name> <git-url>` : add remove repository  
`git remote -v` : list all remotes  
`git push -u <remote> <local-branch>` : push to specified remote

## Tools
`git mergetool` - merge files  
`git difftool` - show difference between files 

### Old
## Git (Draft)

A visual introduction explaining the three different areas and the commit graph.

### Three git stages

Git differs between three different states. A file is always in exactly one of these states:
- Working area: Currently editing the file. Changes on these files have to be added to the staging area first before commiting.
- Staging area: All files in this area will be part of the next commit. Imagin this stage as a temporary state for files to accumulate until the next commit.
- Commite area: All files in here were already commited and being tracked by the repository.

[Put figure with three rounded rectangles to illustrate stages.]

Commands to shift files between different areas:
- From working to staging: `git add`
- From staging to working: `git rm --cached`

- From staging to commit: `git commit`
- From commit to staging: ???

[Add commands to the figure]

### The git-graph
Each commit corresponds to exactly one node in the git-graph.
With `git checkout` you can quickly jump between the different nodes in the graph.
Here you have to be careful: depending on how you manipulate the graph you can end up with nodes that are no longer reachable!
[Put in example figure]

Branches are exactly what the name says: just another branch in the git-graph. Nothing new to learn here except for the commands.

### References
Inspiration for this guide came from the Udacity course "How to use Git and GitHub".
