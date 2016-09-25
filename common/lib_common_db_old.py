#!/usr/bin/env python3
__version__ = "0.01"

#from user_mgmt.lib_user_dl import *
from common.lib_common_log import *
from common.lib_common_par import *
import psycopg2
import sys
import json
import logging
import datetime



# load the database connection data from file
def get_db_connect_parameters (runnig_env):
    try:
        with open('common/db_connect.json', 'r') as conf_file:
            dbconn = json.load(conf_file)
    except OSError as err:
        log_entry ('CRITICAL', 1000, __name__, 'Error getting db connect parameters.')
        logging.critical (err)
        sys.exit(1)
    db_par= dbconn[runnig_env]
    return db_par


# Test db connection
def test_db_connection (con):
    try:
        cur = con.cursor()
        dml= 'SELECT version()'
        cur.execute(dml)
        db_version= cur.fetchone()
        db_version= str(db_version[0])

        dml= 'SELECT name FROM haushalt.haushalt_db;'
        cur.execute(dml)
        result= cur.fetchone()
        result= str(result[0])
        con.commit()
    except psycopg2.DatabaseError as detail:
        if con:
            con.rollback()
        log_entry ('CRITICAL', 1001, __name__, 'Error while testing db connection!')
        logging.debug (detail)
        sys.exit(1)
    log_entry('INFO', 1002, __name__, 'Connected to DB. Database is: ' + result)
    log_entry('DEBUG', 1003, __name__, 'DB version is: ' + db_version)

# open a connection with the database
def stablish_db_connection (running_env):
    db_par= get_db_connect_parameters(running_env)
    db_name= db_par[0]
    db_user= db_par[1]
    db_host= db_par[2]
    db_port= db_par[3]
    db_pass= db_par[4]
    pg_db_connector=  "dbname='" + db_name + "' user='"+ db_user +"' host='" + db_host + "' "
    pg_db_connector+= "port='" + db_port + "' password='" + db_pass + "'"
    log_entry ('DEBUG', 1004, __name__, ' Db_connect= '+ pg_db_connector)
    try:
        log_entry ('DEBUG', 1005, __name__, 'Connecting to the database...')
        con = psycopg2.connect(pg_db_connector)
    except psycopg2.OperationalError as detail:
        log_entry ('CRITICAL', 1006, __name__, 'Error conecting to the database.')
        logging.critical(detail)
        logging.info(pg_db_connector)
        sys.exit(1)
    # Test connection to the database
    test_db_connection (con)
    return con


# close connection with the database
def close_db_connection (con):
    try:
        con.close()
    except psycopg2.OperationalError as err:
        log_entry ('CRITICAL', 1007, __name__, 'Error closing connection to the database.')
        logging.debug (err)
    log_entry ('INFO', 1008, __name__, 'Connection to database closed. Goodbye!')
