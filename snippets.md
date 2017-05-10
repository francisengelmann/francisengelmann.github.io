### pwdd
Copies result of ```pwd``` immediatly into clipboard:

```alias pwdd="pwd | tr -d '\n' | xclip -selection clipboard"```

### Virtualenv with python3

- ```virtualenv -p python3 envname```
- Check this: https://virtualenvwrapper.readthedocs.io/en/latest/install.html

### Matplotlib backend (mac)
```vim ~/.matplotlib/matplotlibrc```
```> backend : TKAgg```

### Copy only certain files from remote machine while preserving dir tree
```rsync -av --include='*/' --include='log.txt' --exclude='*' ./ user@remote_host:/home/user/```

### Vim path completen
While in __INSERT__ mode: <kbd>ctrl</kbd>-<kbd>X</kbd>, <kbd>ctrl</kbd>-<kbd>F</kbd>

### Virtualenvwrapper, tensorflow, jupyter
- ```mkvirtualenv --python=/usr/bin/python3 tf```
- ```workon tf```
- ```pip3 install --upgrade pip```
- ```pip3 insatll --upgrade tensorflow-gpu```
- ```pip3 install --upgrade jupyter```

Source: https://hackercodex.com/guide/mac-development-configuration/

### Python 3
https://docs.python.org/3/tutorial/modules.html

```
import importlib
importlib.reload(utils)
utils.bla()
```
