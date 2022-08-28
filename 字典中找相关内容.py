# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:27:30 2021

@author: xzm20
"""
students=[{"name":"阿刁","age":20,"gender":True},{"name":"董","age":19,"gender":False},]
find_name="阿刁"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"]==find_name:
        print("找到了")
        break
else:
    print("没有找到")
print("循环结束")