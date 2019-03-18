#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Jachin Zhang

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%sx%s=%s"%(i,j,j*i),end=",")
#     print()

for i in range(2,100):
    for j in range(2,i):
        if i % j == 0 :
            break
    else:
        print(i,"是素数")