#!/usr/bin/env phyton3

import uuid

ticket = uuid.uuid1()

try:
    print('Type the name of the configuration file to load.')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileodj.read()
except: # If errors occur
    x = 'General error with obtaining configuration file!'
else: # if there were no errors
    x = 'Switch config file found.'
finally: # In all cases, write out what happened to a log file
    with  open("try04,log", "a") as zlog: # append not  overrite 'a'
        print('\n\nWritinh results of routine to log file')
        print(ticket, " - ", x, file=zlog)# write intozlog 
        
