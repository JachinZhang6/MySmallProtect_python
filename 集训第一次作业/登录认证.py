#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Jachin Zhang
import os
user_dic = {"admin":"root","jachin":"666666","abc":"123"}
# 黑名单
lock_state = ['fdsa']
count = 1
# 记第一次输入的账户名
first_input_user = None
# 标志位，用于判断三次输入的用户名是否相同
is_same_user = True

if os.path.isfile("lock_state.txt"):
    with open("lock_state.txt","r") as f:
        for line in f:
            lock_state.append(line.strip())
while count <= 3:
    user_name_input = input("please input user name: ")
    passwords_input = input("please input passwords: ")
    # 如果账户存在于黑名单，直接退出
    if user_name_input in lock_state:
        exit("Sorry,%s account has been locked" % user_name_input)
        # 如果为None，代表为第一次输入账户
    if not first_input_user:
        first_input_user = user_name_input
        # 代表本次输入的用户名和第一次用户名不一样
    if first_input_user != user_name_input:
        # 标志位设置为False，表示不再执行账户锁定操作
        is_same_user = False
    if user_name_input in user_dic and user_dic[user_name_input] == passwords_input:
        # 登陆成功
        print("Welcome!%s" % user_name_input)
        break
    else:
        # 失败错误少于三次，打印认证失败语句
        print("Authentication failure! Please input again.")
    count+=1
else:
    print("You have failed three times,the program is going to exit !!!")
    # 锁定用户
    if is_same_user:
        # 如果账户名存在于文件中，把账户名加入黑名单
        if user_name_input in user_dic:
            print("%s账户已经锁定" % user_name_input)
            with open("lock_state.txt","a") as f:
                f.write(user_name_input+'\n')
        else:
            # 如果账户名不在文件中，就算重复三次也不加入黑名单
            pass