#!/usr/bin/python3
""" Docstrings"""

import os
import paramiko

# os.walk() -- a 3-Tuple, root, dirs, files
# sshsession.exec_command(command_to_issue) -- a 3-Tuple: stdIn, stdOut, stdErr
# ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_Issue)
#   1 - T      2 - T        3 -T

def commandissue(command_to_issue, sshsession):

    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    our_commands = ["touch sshworded.txt", "touch create.txt", "touch file3.txt", "ls"]
 
    for x in our_commands:
        print(commandissue(x, sshsession).decode('utf-8').strip(), end='')
    print()
    sshsession.close()

main()
