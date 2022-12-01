#!/usr/bin/python3
# Global variable
gbl_name = "Sally" 
def change_name():
    global gbl_name
    gbl_name = "Mark"

change_name()

print(gbl_name)
