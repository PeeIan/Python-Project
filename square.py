# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:08:55 2022

@author: yesyo
"""

from math import pow
de = True
while de:
    s = int(input("輸入要開平方的數字： "))
    a = int(input("輸入要開方幾次： "))
    t = pow(s,1/a)
    print(f"{s}開了{a}方為{t}")
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