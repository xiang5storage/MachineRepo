#!/bin/python

import sys
import readline
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

def helpmenu(): #need to further beautify the help menu
    message = ""
    message = message + "==== Database ====" + "\n"
    message = message + "connect - connect to database" + "\n"
    message = message + "disconnect database" + "\n"
    message = message + "==== Hosts ====" + "\n"
    message = message + "hosts - List all hosts in the database" + "\n"
    message = message + "search - Search the current project for keyword" + "\n"
    message = message + "remove - Remove hosts"
    return message

def completer(text, state):
    cmdoptions = ['help', 'hosts', 'connect', 'disconnect', "search"]
    options = [x for x in cmdoptions if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

def main():
    banner()

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

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

