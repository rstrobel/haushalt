#!/usr/bin/env python3
__version__ = "0.01"

import psycopg2
import sys
import json
import logging
import datetime

import config
from common.lib_common_log import *


# Connect to the database
def db_connect(running_env):
    connect= stablish_db_connection (get_db_connect_parameters (running_env) )
    return connect

# open a connection with the choosed database
def stablish_db_connection (db_par):
    log_entry ('DEBUG', 1004, __name__, ' db_connect= '+ str(db_par))
    try:
        log_entry ('DEBUG', 1005, __name__, 'Connecting to the database...')
        conn= psycopg2.connect(db_par)
    except:
        log_entry ('CRITICAL', 1006, __name__, 'Error conecting to the database.')
        logging.critical(detail)
        logging.info(db_par)
        sys.exit(1)
    return conn


# load the database configuration data from file
def get_db_connect_parameters (running_env):
    try:
        with open('common/db_connect.json', 'r') as conf_file:
            db_configs = json.load(conf_file)
    except OSError as err:
        log_entry ('CRITICAL', 1000, __name__, 'Error getting db connect parameters.')
        logging.critical (err)
        sys.exit(1)
    db_conf= db_configs[running_env]
    db_name= db_conf[0]
    db_user= db_conf[1]
    db_host= db_conf[2]
    db_port= db_conf[3]
    db_pass= db_conf[4]
    db_par=  "dbname='" + db_name + "' user='"+ db_user +"' host='" + db_host + "' "
    db_par+= "port='" + db_port + "' password='" + db_pass + "'"
    return db_par


def exec_query (db, query):
    try:
        cur= db.cursor()
        cur.execute(query)
        l_record= cur.fetchall()
        db.commit()
    except psycopg2.DatabaseError as detail:
        if db:
            db.rollback()
        log_entry ('CRITICAL', 2002, __name__, 'Error executing query')
        logging.debug (detail)
        logging.debug (query)
        sys.exit(1)
    log_entry('DEBUG', 2003, __name__, 'Query executed succesfully')
    logging.debug (query)
    return l_record

# close connection with the database
def close_db_connection (db):
    try:
        db.close()
    except psycopg2.OperationalError as err:
        log_entry ('CRITICAL', 1007, __name__, 'Error closing connection to the database.')
        logging.debug (err)
    log_entry ('DEBUG', 1008, __name__, 'Connection to database closed.')

# con= stablish_db_connection(db_par)
# print( "conectou...")
# l_record= exec_db_query(con, query)
# print( "rodou a query..")
# close_db_connection(con)
# print( "desconectou")
# return l_record

# Test db connection
def test_db_connection (db):
    dml= 'SELECT name FROM haushalt.haushalt_db;'
    l_record= exec_query (db, dml)
    db_version= str(l_record[0])

    dml= 'SELECT version() FROM haushalt.haushalt_db;'
    l_record= exec_query (db, dml)
    version= str(l_record[0])

    log_entry('INFO', 1002, __name__, 'Connected to Database: ' + db_version)
    log_entry('DEBUG', 1003, __name__, 'DB version is: ' + version)

# Module initialization
#config.db= db_connect(running_env)
