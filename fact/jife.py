#!/usr/bin/env python3
""" Docstring """

import csv

with open("csv_users.txt", "r") as csvfile:
    i = 0
    for row in csv.reader(csvfile):
        i += 1
        # i = i +1
        filename = f"admin.rc{i}"

        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL" + row[0], file=rcfile)
