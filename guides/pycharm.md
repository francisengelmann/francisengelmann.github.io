---
layout: page
permalink: /guides/pycharm/
title: PyCharm
tags: [pycharm]
comments: false
---

### Code-Completion
* Select correct virtualenv: ```File/Settings.../Project[...]/Proj.Interpreter/```
* Also in settings: ```Editor/General/Code Completion```

### Add module path
Sometimes you need to change the PYTON_PATH to add your own modules.
For code completion to work, this path needs to be set.
```File/Settings/Project Structure/Add Content Root```

### Views
<key>Alt</key> <key>1</key>-<key>7</key>
View/Tool Windows...

### Virtual environments
* Set a default virtual environment. This is necessary for code completeion to work:   
```File/Default Settings.../Project Interpreter```

### Run code on remote machine
This only works in the professional edition of PyCharm which comes for free if you register as a student.
