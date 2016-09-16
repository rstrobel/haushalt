#!/usr/bin/python

import sys, getopt

def show_help_msg():
    print (" ")
    print ("Usage: python3 haushalt.py --env=[dev|prd] --log-level=[debug|info|warning]")
    print (" ")
    print ("Options:")
    print (" --help, -h         Show help.")
    print (" --env=, -e         Set the environment to run. Choose 'dev'for development or 'prd' from production.")
    print (" --log-level=, -l   Set log severity. Choose 'debug', 'info', or 'warning'. Default is info.")
    print ("                    All parameters are case insensitive")
    print (" ")
    print ("                    Example: python3 haushalt.py --env=prd log_level=debug")
    print (" ")
    sys.exit()


running_env= ''
log_level= ''
try:
    opts, args = getopt.getopt(argv,"-h-e:-l:",["--help", "--env","--log-level"])
except getopt.GetoptError:
    show_help_msg()

for opt, arg in opts:
    if opt in ("-h", "--help"):
        show_help_msg()
        sys.exit()
    elif opt in ("-e", "--env"):
        running_env= arg
    elif opt in ("-l", "--log-level"):
        log_level= arg
    else:
        running_env= 'prd'
        log_level= 'info'

print ("Environment is " + running_env)
print ("Log level is " + log_level)
