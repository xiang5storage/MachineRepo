#!/bin/python

import sys

from pyfiglet import figlet_format

def banner():
    print ""
    print(figlet_format('MachineRepo', font='banner'))

def connectdb():
    return "connectDB"

def disconnectdb():
    return "disconnectDB"

def listhosts():
    return "listHosts"

def search():
    return "search"

def remove():
    return "remove"

def helpmenu():
    message = ""
    message = message + "==== Database ====" + "\n"
    message = message + "connect - connect to database" + "\n"
    message = message + "disconnect database" + "\n"
    message = message + "==== Hosts ====" + "\n"
    message = message + "hosts - List all hosts in the database" + "\n"
    message = message + "search - Search the current project for keyword" + "\n"
    message = message + "remove - Remove hosts"
    return message

def main():
    banner()
    while True:
        print "MachineRepo >",
        userinput = raw_input(" ",)

        if userinput.__contains__("exit"):
            break;

        switcher = {
            "help":helpmenu(),
            "connect":connectdb(),
            "disconnect":disconnectdb(),
            "hosts":listhosts(),
            "search":search(),
            "remove":remove()
        }

        print switcher.get(userinput,"invalid")

main()

