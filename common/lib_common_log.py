#!/usr/bin/env python3
import json
import sys
import psycopg2
import logging
import datetime

# GLOBAL VARIABLES
# get_command_line_parameters ()

def open_log (log_level, running_env, version):
    #logging.basicConfig(filename='/var/log/haushalt.log',level=logging.(log_severity[log_level]))
    if (log_level == 'WARNING'):
        logging.basicConfig(filename='haushalt.log', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.WANING)

    elif (log_level == 'DEBUG'):
        logging.basicConfig(filename='haushalt.log', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
    else:
        logging.basicConfig(filename='haushalt.log',format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    now= datetime.datetime.now()
    logging.info("Starting Haushalt Kontrolle version " + version)
    logging.debug("Using " + running_env + " environment")


def log_entry (level, num, name, message):
    now= datetime.datetime.now()
    log_entry= str(now) + str(num) + " [" + name + "] " ": "+ message
    if (level == 'INFO'):
        logging.info(log_entry)
    elif (level == 'WARNING'):
        logging.warning(log_entry)
    elif (level == 'CRITICAL'):
        logging.critical(log_entry)
    else:
        logging.debug(log_entry)
