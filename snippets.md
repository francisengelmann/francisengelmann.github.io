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
While in insert mode: <kbd>CTRL</kbd>-<kbd>X</kbd>, <kbd>CTRL</kbd>-<kbd>F</kbd>
