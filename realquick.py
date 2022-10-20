#!/usr/bin.env python3
""" Docstring """

import shutil
import os

# Establish a working directory

os.chdir("/home/student/mycode/")


# copy a file from point A to point B
shutil.copy("5g_research/sdn_network.txt","5g_research/sdn_network.txt.copy")

#copy a Directory to Backup
#shutil.copytree("5g_research/", "5g_research_backup/")

# Submit a standard linux command using 'os.system'
os.system("rm -rf /home/student/mycode/5g_research_backup/")
