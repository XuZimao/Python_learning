# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:52:01 2021

@author: xzm20
"""

try:
    num=eval(input("请输入一个列表:"))
    num.reverse()
    print(num)
except:
    print("输入的不是列表")
    