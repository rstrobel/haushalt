#!/usr/bin/env python3
__version__ = "0.01"
#########################################################
#
# Data Access Layer
#
#########################################################
from user_mgmt.lib_user_dl import *
from common.lib_common_db import *
from common.lib_common_log import *
from common.lib_common_par import *
import psycopg2
import sys
import getopt
import json
import logging
import datetime
import datetime


def insert_user_record (con, l_user_record):
    v_usr_name= l_user_record [0]
    v_usr_role_id= l_user_record[1]
    v_usr_status= l_user_record[2]
    dml= "INSERT INTO tb_users VALUES(DEFAULT,'" + v_usr_name + "'," +  str(v_usr_role_id) + ", '" + v_usr_status + "');"
    try:
        cur = con.cursor()
        cur.execute(dml)
        con.commit()
    except psycopg2.DatabaseError as detail:
        if con:
            con.rollback()
        log_entry ('CRITICAL', 2000, __name__, 'Error inserting user.')
        logging.debug (detail)
        sys.exit(1)
    log_entry('DEBUG', 2001, __name__, 'User ' + v_usr_name + ' created.')

def update_user_record (con, l_user_record):
    v_usr_name= l_user_record [1]
    v_usr_role_id= l_user_record[2]
    v_usr_status= l_user_record[3]
    dml=  "UPDATE tb_users SET usr_role_id = " + str(v_usr_role_id) + ", usr_status = " + v_usr_status
    dml+= " WHERE usr_name = " + v_usr_name + ";"
    try:
        cur = con.cursor()
        cur.execute(dml)
        con.commit()
    except psycopg2.DatabaseError as detail:
        if con:
            con.rollback()
        log_entry ('CRITICAL', 2002, __name__, 'Error updating user.')
        logging.debug (detail)
        sys.exit(1)
    log_entry('DEBUG', 2003, __name__, 'User ' + v_usr_name + ' updated.')

def delete_user_record (con, l_usr_record):
    v_usr_name= l_user_record [1]
    dml=  "DELETE FROM tb_users WHERE usr_name = " + v_usr_name + ";"
    try:
        cur = con.cursor()
        cur.execute(dml)
        con.commit()
    except psycopg2.DatabaseError as detail:
        if con:
            con.rollback()
        log_entry ('CRITICAL', 2004, __name__, 'Error deleting user.')
        logging.debug (detail)
        sys.exit(1)
    log_entry('DEBUG', 2005, __name__, 'User ' + v_usr_name + ' deleted.')


def get_user_record (con, usr_name):
    dml=  "SELECT usr_id, usr_name, usr_role, usr_status FROM tb_users WHERE usr_name = " + usr_name + ";"
    try:
        cur = con.cursor()
        cur.execute(dml)
        con.commit()
    except psycopg2.DatabaseError as detail:
        if con:
            con.rollback()
        log_entry ('CRITICAL', 2006, __name__, 'Error selecting user.')
        logging.debug (detail)
        exit(1)
    log_entry('DEBUG', 2007, __name__, 'User ' + v_usr_name + ' selected.')
