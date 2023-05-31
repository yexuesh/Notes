NUlL: s3399430649@gmail.com

# 命令

# langch文件

# 简单执行步骤

## vscode step(步骤)

```shell
mkdir -p <dirName>/src
cd <dirName>
catkin_make
code .
```

### vscode compile & Config File

快捷键 ctrl + shift + B 调用编译，选择:`catkin_make:build`

可以点击配置设置为默认，修改.vscode/tasks.json 文件

```json
{
    // 有关 tasks.json 格式的文档，请参见
    // https://go.microsoft.com/fwlink/?LinkId=733558
    "version": "2.0.0",
    "tasks": [
        {
            // 代表提示的描述性信息
            "label": "catkin_make:debug", 
            
            // 可以选择shell或者process,如果是shell代码是在shell里面运行一个命令，
            // 如果是process代表作为一个进程来运行
            "type": "shell",  

            // 这个是我们需要运行的命令
            "command": "catkin_make",
            
             // 如果需要在命令后面加一些后缀，可以写在这里，比如-DCATKIN_WHITELIST_PACKAGES=“pac1;pac2”
            "args": [],
            "group": {"kind":"build","isDefault":true},
            "presentation": {
                // 可选always或者silence，代表是否输出信息
                "reveal": "always"
            },
            "problemMatcher": "$msCompile"
        }
    ]
}
```

### Test code (C++)

```cpp
#include "ros/ros.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    //执行节点初始化
    ros::init(argc,argv,"HelloVSCode");

    //输出日志
    ROS_INFO("Hello VSCode!!!哈哈哈哈哈哈哈哈哈哈");
    return 0;
}
```

### Test code (Python)

```python
#! /usr/bin/env python
"""
    Python 版本的 HelloVScode，执行在控制台输出 HelloVScode
    实现:
    1.导包
    2.初始化 ROS 节点
    3.日志输出 HelloWorld
"""

import rospy

if __name__ == "__main__":
    rospy.init_node("Hello_Vscode_p")  # 2.初始化 ROS 节点
    rospy.loginfo("Hello VScode, 我是 Python ....")  #3.日志输出 HelloWorld

```

### CMakeLists.txt ( C++ ) 

```cmake
add_executable(节点名称
  src/C++源文件名.cpp
)
target_link_libraries(节点名称
  ${catkin_LIBRARIES}
)
```

CMakeLists.txt(python)

```cmake
catkin_install_python(PROGRAMS scripts/自定义文件名.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

