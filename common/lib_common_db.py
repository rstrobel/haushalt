#!/usr/bin/env python3
import json
import sys
import psycopg2
import logging
import datetime
from common.lib_common_log import *


# GLOBAL VARIABLES
# get_command_line_parameters ()

# load the database connection data from file
def get_db_connect_parameters (runnig_env):
    try:
        with open('common/db_connect.json', 'r') as conf_file:
            dbconn = json.load(conf_file)
    except detail:
        log_entry ('CRITICAL', 1000, __name__, 'Error getting db connect parameters.')
        logging.critical (detail)
        sys.exit(1)
    db_conn_parameters= dbconn[runnig_env]
    return db_conn_parameters


# open a connection with the database
def stablish_db_connection (running_env):
    db_par= get_db_connect_parameters(running_env)
    pg_db_connector=  "dbname='" + db_par[0] + "' user='"+ db_par[1] +"' host='" + db_par[2] + "' "
    pg_db_connector+= "port='" + db_par[3] + "' password='" + db_par[4] + "'"
    print (pg_db_connector)
    try:
        con = psycopg2.connect(pg_db_connector)
    except psycopg2.OperationalError as detail:
        log_entry ('CRITICAL', 1001, __name__, 'Error conecting to the database.')
        logging.critical(detail)
        logging.info(pg_db_connector)
        sys.exit(1)
    return con
# close connection with the database
def close_db_connection (con):
    try:
        con.close()
    except detail:
        log_entry ('CRITICAL', 1002, __name__, 'Error closing connection to the database.')
        logging.debug (detail)
