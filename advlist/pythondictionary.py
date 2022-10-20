#!/usr/bin/env python3
""" Docstring"""

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

# displaty parts of the dictionary
print(switch["hostname"] )
print(switch["ip"] ) 

## request a 'fake key'

print("First test - .get()" )
print(switch.get("lynx") )

print("Second test - .get()" )  
print(switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!")) 

print("Third test - .get()" )
print(switch.get("version") )

print("fourth test - .key()" )
print(switch.keys() )

print("fifth test - .values()" )
print(switch.values() )
