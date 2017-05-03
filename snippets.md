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

### Git submodule
* Adding git-repo inside other git-repo:
  * git submodule add [git-url]
  * git add .gitmodules + commit ..
  
* Cloning such a repo
  * git submodule init
  * git submodule update
