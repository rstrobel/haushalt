#!/usr/bin/env python3
__version__ = "0.01"

#from user_mgmt.lib_user_dl import *
from common.lib_common_db import *
from common.lib_common_log import *
import psycopg2
import sys
import json
import logging
import datetime

def get_command_line_parameters (argv):
    def show_help_msg():
        print (" ")
        print ("Usage: python3 haushalt.py --dsv|--prd    [--debug]")
        print (" ")
        print ("Options:")
        print (" --help             Show help.")
        print (" --prd | --dsv      Choose to run in the development (--dsv) or production (--prd) environment.")
        print (" --debug            Activate debug mode (debug messages shown in log).")
        print (" --version          Print Haushalt Kontrolle version number.")
        print (" ")
        print ("                    Example: python3 --dev --debug")
        print (" ")

    running_env=''
    running_env_already_set= False
    log_level= 'info'
    log_level_already_set= False
    qt_args= len(sys.argv)
    msg_help='Type: "python haushalt.py --help" for more help.'

    if (qt_args > 1):
        # p1
        p1= str(argv[1]).lower()
        if (p1 == "--help"):
            show_help_msg()
            sys.exit(0)
        elif (p1 == "--version"):
            print ("Haushalt Kontrolle " + __version__)
            sys.exit(0)
        elif (p1 in ('--prd', '--prod')):
            running_env= 'prd'
            running_env_already_set= True
        elif (p1 in ('--dsv','--dev')):
            running_env= 'dsv'
            running_env_already_set= True
        elif (p1 == '--debug'):
            log_level= 'debug'
            log_level_already_set= True
        else:
            print (str(p1) + " is not a valid parameter!")
            print (msg_help)
            sys.exit(1)
        # p2
        if (qt_args > 2 ):
            p2= str(argv[2]).lower()
            if (p2 == '--debug'):
                if (log_level_already_set):
                    print ("Missing environment parameter ( --dsv or --prd)!")
                    print (msg_help)
                    sys.exit(1)
                else:
                    log_level= 'debug'
                    log_level_already_set= True
            if (p2 in ('--prd', '--prod')):
                if(running_env_already_set):
                    print (p1 + " and " + p2 + " informed. Environment parameter can only be used once!")
                    print (msg_help)
                    sys.exit(1)
                else:
                    running_env= 'prd'
                    running_env_already_set= True
            if (p2 in ('--dsv','--dev')):
                if(running_env_already_set):
                    print (p1 + " and " + p2 + " informed. Environment parameter can only be used once!")
                    print (msg_help)
                    sys.exit(1)
                else:
                    running_env= 'dsv'
                    running_env_already_set= True
    else:
        print ("Invalid parameters!")
        print (msg_help)
        sys.exit(1)
        
    # Bonus: check python version (haushalt only works in python 3)
    print ("python version= " + str(sys.version_info))
    if (sys.version_info.major < 3):
        print ('Haushalt Kontrolle is only compatible with Python 3 and over. Use "python3 haushalt <parameters>"')
        print  (msg_help)
        sys.exit(1)
    return running_env, log_level
