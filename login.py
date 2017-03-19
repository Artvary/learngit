#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass

name = raw_input("Please input username：")
file = open('user-text.txt','r+')
user_dic = dict()
for line in file:
    line = line.strip().split(':')
    m = dict()
    m["password"] = line[1]
    m["lock_num"] = line[2]
    user_dic[line[0]] = m

if name in user_dic:
    if int(user_dic[name]["lock_num"]) >=3 :
        print "The user has be locked"
    else:
        n = 1
        while n < 4:
            passwd = getpass.getpass("Please input your password：")
            if passwd == user_dic[name]["password"]:
                print "Welcome  %s !" %name
                file.close
                exit()
            else:
                print "Password error！"
                n += 1
                if n == 3:
                    file.close()
                
else:
    print "No user !"
