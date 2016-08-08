#coding: utf-8

userName = raw_input("What is your name ?\n")
message = raw_input("Enter a message: ")

while message != "exit":
    print (userName + ": " + message)
    message = raw_input("Enter a message: ")

