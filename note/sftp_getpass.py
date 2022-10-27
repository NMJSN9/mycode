#!/usr/bin/python3
""" Docstrings """

import paramiko
import os
import getpass

def main():
    t = paramiko.Transport("10.10.2.3", 22)
    t.connect(username="bender", password=getpass())
    
    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put("file_to_move.txt", "file_to_move.txt")

    sftp.close()
