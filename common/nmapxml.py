#!/bin/python

import untangle

def nmapxmltoobject(xmlfile):
    obj = untangle.parse(xmlfile)
    return obj


def importnmaptodatabase(xmlfile):
    obj = nmapxmltoobject(xmlfile)
    return