#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time: 2023/2/8 17:25
# @Author: XIN

import os
import sys
sys.path.append(r"D:\HOME\ProgrammingLanguage\Object\Python")

from Translate.BaiDuTranslate.BaiDuFanYiAPI import *

import pytesseract
from PIL import Image
import pyautogui


path = "r1.png"
text = pytesseract.image_to_string(Image.open(path), lang='jpn')
a = BaiDuFanYi(text, "jp", "zh")
print(a.run())
