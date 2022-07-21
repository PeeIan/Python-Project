# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = []
c = []
de = True
while de:
    x = int(input("輸入科目成績: "))
    y = int(input("輸入科目學分數: "))
    a.append(x*y)
    c.append(y)
    b = True
    while b:
        d = int(input("輸入0結束1繼續: "))
        if d == 0:
            de = False
            break;
        elif d == 1:
            b = False
        else:
            print("無效，請重新輸入： ")
            continue
print("你的學期平均: ")
print(sum(a)/sum(c))