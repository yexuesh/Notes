# Linux

1. `which -a python`：列出所有名为python的可执行文件的路径。
2. `whereis python`：列出二进制文件、man页和源代码的路径。
3. `find / -name "python*" -type f 2>/dev/null`：在整个系统中搜索所有名字以"python"开头的文件。
4. `ls /usr/bin/python*`：列出所有在`/usr/bin`目录下以`python`开头的文件。
5. `ls /usr/local/bin/python*`：列出所有在`/usr/local/bin`目录下以`python`开头的文件。
6. `locate python`：查找包含关键字"python"的所有文件。
7. `snap list`：列出所有已安装的snap软件包，包括Python解释器。
8. `dpkg -S $(which python)`：查找安装了python解释器的软件包。

# Windows

```bash
where python
```

```bash
dir /s/b python.exe
```