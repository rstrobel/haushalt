#!/usr/bin/env python3
__version__ = "0.01"

import logging
import datetime

from common.lib_common_par import *
import config

def open_log (log_level, running_env):
    #logging.basicConfig(filename='/var/log/haushalt.log',level=logging.(log_severity[log_level]))
    filename= 'haushalt.log'
    log_format= '%(asctime)s: %(levelname)s: %(message)s'
    dtfmt= '%m/%d/%Y %H:%M:%S'
    if (log_level == 'debug'):
        logging.basicConfig(filename=filename, format=log_format, datefmt=dtfmt, level=logging.DEBUG)
    else:
        logging.basicConfig(filename=filename, format=log_format, datefmt=dtfmt, level=logging.INFO)
    logging.info("-------------- Starting Haushalt Kontrolle --------------")
    print("-------------- Starting Haushalt Kontrolle --------------")

    log_entry ('INFO', 1200, __name__, 'Version: ' + __version__)
    log_entry ('DEBUG', 1201, __name__, 'Running environment: ' + running_env)
    log_entry ('DEBUG', 1202, __name__, 'Log severity level: ' + log_level)
    pv= sys.version_info
    log_entry ('DEBUG', 1203, __name__, 'Python version: ' + str(pv.major) + '.' + str(pv.minor) + '.' + str(pv.micro))




def log_entry (msg_level, num, name, message):
    msg_level= msg_level.upper()
    log_entry= "\t" + str(num) + " [" + name + "] " ": "+ message
    if (msg_level == 'INFO'):
        logging.info(log_entry)
    elif (msg_level == 'WARNING'):
        logging.warning(log_entry)
    elif (msg_level == 'CRITICAL'):
        logging.critical(log_entry)
    else:
        logging.debug(log_entry)
