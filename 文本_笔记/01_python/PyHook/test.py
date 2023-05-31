#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time: 2023/2/8 22:34
# @Author: XIN

import PyHook3 as pyHook
import pythoncom


def onMouseEvent(event):
    # 监听鼠标事件
    print("MessageName:", event.MessageName)
    print("操作号", "Message:", event.Message)
    print("Time:", event.Time)
    print("编号的窗口", "Window:", event.Window)
    print("WindowName:", event.WindowName)
    print("Position:", event.Position)
    print("滚轮方向", "Wheel:", event.Wheel)
    print("Injected:", event.Injected)
    print("---")

    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True


def onKeyboardEvent(event):
    # 监听键盘事件
    print("MessageName:", event.MessageName)
    print("Message:", event.Message)
    print("Key:", event.Key)
    print("KeyID:", event.KeyID)
    print("Ascii:", event.Ascii, chr(event.Ascii))
    print("WindowName:", event.WindowName)
    print("Window:", event.Window)
    print("Time:", event.Time)
    print("Alt", event.Alt)

    print("ScanCode:", event.ScanCode)
    print("Extended:", event.Extended)
    print("Injected:", event.Injected)
    print("Transition", event.Transition)

    print("---")
    if event.Key == 'Q':
        event = quit()
    # 同鼠标事件监听函数的返回值
    return True


def main():
    """
    创建 "Hook" 管理对象: hm = PyHook3.HookManager()
    设置监听事件: hm.事件名称 = 函数名
    设置 键盘/鼠标 钩子: hm.HookKeyboard() / hm.HookMouse()
    :return:
    """
    print("starting...")
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()

    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()

    # 监听所有鼠标事件
    hm.MouseAll = onMouseEvent
    # 设置鼠标“钩子”
    hm.HookMouse()

    # 进入循环，如不手动关闭，程序将一直处于监听状态
    print("asdasd")
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
"""
除此之外，还有以下事件：
鼠标事件：
MouseAll             鼠标所有操作
MouseAllButtons      监测鼠标所有按键操作
MouseAllButtonsUp    监测鼠标所有按键抬起
MouseAllButtonsDown  监测鼠标所有按键按下
MouseAllButtonsDbl   监测鼠标所有按键双击
MouseWheel           滚轮
MouseMove            移动
MouseLeftUp          左击抬起
MouseLeftDown        左击按下
MouseLeftDbl         左键双击
MouseRightUp         右键抬起
MouseRightDown       右击按下
MouseRightDbl        右击双击
MouseMiddleUp        中键抬起
MouseMiddleDown      中键抬起
MouseMiddleDbl       中键双击
键盘事件：
KeyUp
KeyDown
KeyChar
KeyAll
因为都可以顾名思义，也就不再做注释。
"""