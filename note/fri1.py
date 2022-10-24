#!/usr/bin/env python3
""" Docstring """


def loginFail():
    loginfail = 0 

    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")
    keystone_file_lines = keystone_file.readlines()

    for the line in keystone_file_lines:
        if "- - - - -] Authorization filed" in line:
            loginfail += 1
            print(line)
    print("The number of failed log in attemps is", loginfail)

    keystone_file.close()

#def loginBothwihWITH():
    #with open("/home/student/mycode/attemptlogin/keystone_common.wsgi") as kfile:
        #for line in kfile:

