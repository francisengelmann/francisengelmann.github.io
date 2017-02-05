### pwdd
Copies result of ```pwd``` immediatly into clipboard:

```alias pwdd="pwd | tr -d '\n' | xclip -selection clipboard"```

### Virtualenv with python3

```virtualenv -p python3 envname``` 

### Matplotlib backend (mac)
```vim ~/.matplotlib/matplotlibrc```
```> backend : TKAgg```
