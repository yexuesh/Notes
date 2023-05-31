#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time: 2023/2/8 23:48
# @Author: XIN

import win32gui

handle_list = []


def getdcCallbake(hwnd, extra):
    print("hwnd", hwnd)
    extra.append(hwnd)
    print("-"*20)

    return True


win32gui.EnumWindows(getdcCallbake, handle_list)
print(len(handle_list))
print(handle_list)

a = win32gui.GetDC(0x380a68)
print(a)
win32gui.Rectangle(a, 0, 0, 100, 100)
win32gui.ReleaseDC(0x380a68, a)
