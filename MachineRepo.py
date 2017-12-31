#!/bin/python

import sys
import readline
from terminaltables import AsciiTable
from pyfiglet import figlet_format
from common import sqlite,nmapxml


def banner():
    print ""
    print(figlet_format('MachineRepo', font='banner'))

def connectdb():
    #sqlite.sqliteconnect("dbfile")
    return "connectDB"

def disconnectdb():
    return "disconnectDB"

def listhosts():
    return "listHosts"

def search():
    return "search"

def remove():
    return "remove"

def importnmap():
    #nmapxml.importnmaptodatabase(xmlfile)
    return "nmap xml files imported successfully"

def helpmenu():
    message = []
    message.append(["command","Description"])
    message.append(["connect","Connect to database"])
    message.append(["disconnect","Disconnect with database"])
    message.append(["hosts","List all hosts in the database"])
    message.append(["search","Search the current project for keyword"])
    message.append(["remove","Remove host(s)"])
    message.append(["import","Import nmap XML to database"])
    message.append(["exit","Exit the program"])

    helptable = AsciiTable(message)
    helptable.inner_row_border = False
    helptable.outer_border = False

    return helptable.table + "\n"

def completer(text, state):
    cmdoptions = ['help','hosts','connect','disconnect',"search","import","exit"]
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
            "remove":remove(),
            "import":importnmap()
        }
        print ""
        print switcher.get(userinput,"")

main()

