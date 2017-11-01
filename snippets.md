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

### Installing tensorflow from source
git clone git@github.com:tensorflow/tensorflow.git  
cd tensorflow  
git branch -av  
git checkout r1.2  (or whatever version you like)
pip3 install --upgrade {numpy,dev,pip,wheel}

### Same thing following this guide:
http://blog.xiangjiang.live/compile-tensorflow-from-source-with-swig-and-bazel-for-local-user/

#### Installing bazel
wget https://github.com/bazelbuild/bazel/releases/download/0.5.1/bazel-0.5.1-dist.zip  
unzip bazel-0.5.1-dist.zip -d bazel-0.5.1ls  

Needs JDK 1.8  
Download: http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html  
Install by unzipping.

It then crashes, fix is here:
https://github.com/bazelbuild/bazel/issues/1308

### Python 3
https://docs.python.org/3/tutorial/modules.html

```
import importlib
importlib.reload(utils)
utils.bla()
```

### Nvidia
Continuously monitor nvida gpu: ```watch -n 1 nvidia-smi```

### h5py
- dir like structure
- The h5py package is a Pythonic interface to the HDF5 binary data format.

### Timing
Print detailed execution timings```%%time```

### Jupyter Notebook
https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/

tensorboard --logdir=path

```gmonitor``` similar to ```watch -n0,1 nvidia-smi```

### tmux

###
Create new tmux session on remote: ```tmux new -s tf```  
Reconnect: ```tmux a -t tf```  
Start new jupyter session: ```jupyter notbeook --no-browser --port=1337```  
From local, connect to remote: ```ssh -N -f -L :8080:localhost:1337 tyskie```  
In local browser: ```http://localhost:8080/```  

#### tmux Links
- Cheatsheet: http://www.dayid.org/comp/tm.html
- Split windows etc: http://lukaszwrobel.pl/blog/tmux-tutorial-split-terminal-windows-easily
- https://gist.github.com/MohamedAlaa/2961058


### gh
print history from current dir

### rsync
rsync -av source destination

* ls -d : only list directories
* scp -r ./asd*asd : when : present in name

### VKT, python3 wrappers in virtualenv on mac using homebrew
* ``brew install vtk --with-python3 --without-python`` Install vtk with python3 bindings (and without python2, will complain otherwise)
* Next you need to copy or link the vtk site-packages into your virtualenv.
Homebrew installs it here: ``/usr/local/Cellar/vtk/8.0.1/lib/python3.6/site-packages/vtk``
So all you need to do in order to access vtk form your virtualenv is to link or copy vtk into your virtualenv site-package folder located here: 
``/Users/foo/.virtualenvs/tf_py3/lib/python3.6/site-packages/vtk``

