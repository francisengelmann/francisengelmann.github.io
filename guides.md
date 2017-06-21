# Guides
This is a collection of short guides to setup and use software I find useful.
At this point all articles are drafts.

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

## PyCharm (Draft)
### Code-Completion
* Select correct virtualenv: ```File/Settings.../Project[...]/Proj.Interpreter/```
* Also in settings: ```Editor/General/Code Completion```
### Virtual environments
* Set a default virtual environment
### Running code
* Find a better way to run the current file
