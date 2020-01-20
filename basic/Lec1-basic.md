

# Lecture 1: Linux and Python

## Problem

摄影师小汪在日本旅游时控制不住激动的双手，咔咔咔拍摄了一万张照片，其中照片的格式包括`.jpg`, `.png` (视频快照格式), `.ARW` (索尼拍摄), `.CR2` (佳能拍摄).  可是小汪躺下之后发现她只想处理ARW文件（大约有3000张），而小汪的电脑很卡，无法通过访达进行文件操作。请问小汪如何才能：

1. 快速知道有多少张ARW文件？
2. 把其他的文件都移动到硬盘，只保留ARW文件在本地？
3. 只修昨天拍的图？



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
- Wildcard ``*``
- ``cat`` (concatenate): print out file content. ``cat file1 file2 > file3``.
- ``wc`` (word count): lines, words, characters. ``wc -l`` only prints out lines.
- ``>``: ``ls -lht > directory.txt``
- ``sudo`` (not Subo)

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

区分：``jupyter notebook``, ``jupyter lab``.

Jupyter的好帮手：[Jupyter extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions), [Jupyter notebook viewer](https://nbviewer.jupyter.org), some shortcuts.


![The-Outsourcing-Learning-Curve](https://github.com/AstroJacobLi/pynguin/raw/master/basic/The-Outsourcing-Learning-Curve.png)

Life of a programmer:

![jakevdp](https://github.com/AstroJacobLi/pynguin/raw/master/basic/jakevdp.png)



### Zen of Python

Beautiful is better than ugly. （优美比丑陋好）

 Explicit is better than implicit.（清晰比晦涩好） 

Simple is better than complex.（简单比复杂好） 

Complex is better than complicated.（复杂比错综复杂好） 

Flat is better than nested.（扁平比嵌套好）

Sparse is better than dense.（稀疏比密集好） 

Readability counts.（可读性很重要） 

Now is better than never.（现在开始做比不做好）  

Namespaces are one honking great idea -- let's do more of those!（命名空间非常有用，我们应当多加利用）



## Homework
2. Jake VanderPlas: http://jakevdp.github.io; 

   **Python data science book**: https://github.com/jakevdp/PythonDataScienceHandbook

3. 请用python模拟实验证明：服从正态分布的随机变量$X$的标准误为$\overline{X}/\sqrt{N}$. 
