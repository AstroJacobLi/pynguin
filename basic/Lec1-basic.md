

# Lecture 1: Setting up your computer -- Operating system (Linux) and Python

## Operating System

### Concepts
- Operating System: two categories -- Unix-based, and Windows
- Unix: operating files in a certain way. Linux, MacOS, etc.
- Shell: A Unix shell is a command-line interpreter or shell that provides a command line user interface for Unix-like operating systems.
- GUI (graphical user interface)
- Syntax and command line
- Terminal: Linux and Windows (e.g. [cmder](https://cmder.net)). Windows now supports bash. Convention: starting with ``$``.
- Bash: a Unix shell written for GNU project. (Bourne Again Shell = BASH). [Zsh v.s. Bash.](https://www.chenhuijing.com/blog/bash-to-zsh/#🎹) ``/bin/bash xxx``
- Directory: ``dir``

### Unix commands
- ``man ls``
- ``cd``: ``cd .``, ``cd ..``, ``cd ../..``, ``cd ~``, ``cd /``, ``cd ./xxx/xxxx``
- ``pwd``
- ``ls``: -lth, -S (size), -R (recursively), -d (list folders), -h (human-readable size), -t (time)
- ``mkdir``: never use empty space!
- ``mv``: rename file. -u (update), -v (verbose). ``mv file_name new_name new_location``.
- ``cp``: -R (recursively), -u (update), -i (interactive), -f (forced)
- ``rm``: -r (recursively), -f (forced). Be cautious with ``rm -rf xxx``.
- control + C, control + Z, command + K, command + L
- ``sudo`` (not Subo)
- Wildcard ``*``
- ``cat`` (concatenate): print out file content. ``cat file1 file2 > file3``.
- ``wc`` (word count): lines, words, characters. ``wc -l`` only prints out lines.
- ``ps`` (process): ``ps -aux``
- ``>``: ``ls -lht > directory.txt``

### 禁忌

- 不要有文件名不要有`.`
- 文件名不要有空格
- 文件管理
- `rm -rf ` 之前请三思！！！

### More on Bash
``~/.bash_rc`` or ``~/.bash_profile``: config file of bash. 
``~/.bash_history``: history of bash. 

#### Alias
Alias makes your life better!

``$ alias`` prints out all aliases defined. 

Write in ``.bash_profile``: ``alias show_pid='ps aux | grep ssh'``

No spaces around "="!!! Don't forget to validate changes by ``source ~/.bash_profile`` or ``. ~/.bash_profile``.

### ``vi`` and ``vim``
Steep learning curve. [Interactive learning vim](https://openvim.com)

Common usage: ``:q, :w, :wq, :q!, h, j, k, l, w, b, e, u, ctrl+R``

``vim`` [cheatsheet](https://vim.rtorr.com)



## Python
Pros: high level, open-source, widely used, countless third-party packages in various areas, large and active community, ML/DL.

Cons: Slow? (Cython)

![compile-process](https://github.com/AstroJacobLi/Python101.5/raw/master/Lecture1/compile-process.png)

#### Installation
Anaconda: https://www.anaconda.com; 清华镜像: https://mirrors.tuna.tsinghua.edu.cn.
Pip: https://pip.pypa.io/en/stable/.

#### Hello world：你的第一个python程序



#### IDEs and Jupyter
Editors: Atom (x, too heavy), Vi/Vim (cantankerous), sublime text (good, but expensive), Visual Studio Code (best so far).

IDEs: PyCharm (x), Spyder (could check variables, but in a "scriptive" way).

Best choice: **<u>VSCode</u>** + [Jupyter](https://jupyter.org)! Jupyter = julia + python + terminal.

``jupyter notebook``, ``jupyter lab``.

[Jupyter extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions), [Jupyter notebook viewer](https://nbviewer.jupyter.org), some shortcuts.


![The-Outsourcing-Learning-Curve](https://github.com/AstroJacobLi/pynguin/raw/master/basic/The-Outsourcing-Learning-Curve.png)

Life of a programmer:

![jakevdp](https://github.com/AstroJacobLi/pynguin/raw/master/basic/jakevdp.png)



## Homework
0. Register an GitHub account 

1. 数据可视化的重要性。每天两章，请做笔记：https://serialmentor.com/dataviz/

2. Jake VanderPlas: http://jakevdp.github.io; 

   **Python data science book**: https://github.com/jakevdp/PythonDataScienceHandbook

   
