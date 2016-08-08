#coding: utf-8

import time
import sys
shipName = "神州一号"
caption = "Chen"
location = "地球"
password = "love"


# access control
pAttempt = raw_input("输入控制密码: ")
while pAttempt != password:
    print "密码错误，再次输入，或输入exit退出"
    if pAttempt == "exit":
        pass
    pAttemp = raw_input("Enter the password again: ")
print "密码正确，欢迎来到" +'"'+ shipName+'"'

###############################
# Basic information of this crat
print "------------INFORMATION---------------"
print "我们的飞船"+'"'+shipName+'"'+"号目前位于"+location
# 提示信息
choice = ''
while choice != "exit":
    print caption+"舰长"+",请输入指令: "
    print ""
    print "a. 访问另一星球."
    print "b. 开火."
    print "c. 打开气锁."
    print "d. 启动自毁程序."
    print "输入exit退出."
    print "-----------------------------"
    choice = raw_input("输入选项：")
    if choice == "a":
        destination = raw_input("输入目的地: ")
        print "正在离开"+location + "..."
        time.sleep(1)
        print "正在前往"+destination + "..."
        time.sleep(5)
        print "已经抵达"+destination
        location = destination
        print "-----------------------------"
    elif choice == "b":
        print "准备开火"
        time.sleep(1)
        print "开火"
        print "-----------------------------"
    elif choice == "c":
        print "正在打开气锁"
        time.sleep(1)
        print "气锁已经打开"
        time.sleep(1)
        print "-----------------------------"
    elif choice == "d":
        confirm = raw_input("确定启动自毁程序？(Y/N)")
        if confirm == 'y' or confirm == 'Y':
            print "开启自毁程序"
            print '"'+shipName +'"' + "将在3秒后自毁"
            time.sleep(1)
            print '"'+shipName +'"' + "将在2秒后自毁"
            time.sleep(1)
            print '"'+shipName +'"' + "将在1秒后自毁"
            time.sleep(1)
            print "再见"
            print "BOOM"
            choice = "exit"
            print "-----------------------------"
    elif choice == "exit":
        print "已退出"
    else:
        print "输入无效，请重新输入a, b, c, d 或exit退出"
        print "-----------------------------"




###############################
