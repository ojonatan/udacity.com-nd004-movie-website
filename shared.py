#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Shared module for common tasks not directly related to any other module involved"""

import os
path = ""
if os.path.dirname(__file__):
    path = os.path.dirname(__file__) + "/"
    
if not os.path.isfile(path + "settings.py"):
    if os.path.isfile(path + "settings.py-example"):
        settings = open(path + "settings.py", "w+")
        settings.write(open(path + "settings.py-example").read())
        settings.close()
    else:
        print "File settings.py could not be found."
        exit(99)
        
