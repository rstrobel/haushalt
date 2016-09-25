#!/usr/bin/env python3
__version__ = "0.01"

import sys
import logging
import datetime
import os

import config
from common.lib_common_db import *
from common.lib_common_log import *

#####################################################################################
#
# Data Access Layer
#
#####################################################################################
def insert_user_record (l_user_record):
    v_usr_name= l_user_record[1].title()
    v_usr_role_id= l_user_record[2]
    v_usr_status= l_user_record[3]
    dml= "INSERT INTO tb_users VALUES (DEFAULT,'" + v_usr_name + "'," +  str(v_usr_role_id) + ", '" + v_usr_status + "');"
    try:
        cur = config.db.cursor()
        cur.execute(dml)
        config.db.commit()
    except:
        config.db.rollback()
        log_entry ('CRITICAL', 2002, __name__, 'Error updating user.')
        #logging.debug (detail)
        sys.exit(1)
    log_entry('DEBUG', 2001, __name__, 'User ' + v_usr_name + ' created.')
    return True

def update_user_record (l_user_record):
    print ("executing DL...")
    v_usr_id= l_user_record[0]
    v_usr_name= l_user_record [1]
    v_usr_role_id= l_user_record[2]
    v_usr_status= l_user_record[3]
    dml=  "UPDATE tb_users SET usr_role_id = " + str(v_usr_role_id) + ", usr_status = '" + v_usr_status
    dml+= "' WHERE usr_id = " + str(v_usr_id) + ";"
    print (dml)
    try:
        cur = config.db.cursor()
        cur.execute(dml)
        config.db.commit()
    except:
        config.db.rollback()
        log_entry ('CRITICAL', 2002, __name__, 'Error updating user.')
        #logging.debug (detail)
        sys.exit(1)
    log_entry('DEBUG', 2003, __name__, 'User ' + v_usr_name + ' updated.')
    return True

def get_user_record (usr_name):
    dml=  "SELECT usr_id, usr_name, usr_role_id, usr_status FROM tb_users WHERE Upper(usr_name) = Upper('" + usr_name + ")';"
    try:
        cur = config.db.cursor()
        cur.execute(dml)
        config.db.commit()
    except:
        config.db.rollback()
        log_entry ('CRITICAL', 2006, __name__, 'Error selecting user.')
        #logging.debug (detail)
        exit(1)
    log_entry('DEBUG', 2007, __name__, 'User ' + v_usr_name + ' selected.')
    return l_user_record


def get_all_users():
    dml= "SELECT * FROM tb_users"
    tl_users= exec_query (config.db, dml)
#     try:
#         cur = config.db.cursor()
#         cur.execute(dml)
#         config.db.commit()
# #   except psycopg2.DatabaseError as detail:
#     except:
#         config.db.rollback()
#         log_entry ('CRITICAL', 2008, __name__, 'Error selecting user list.')
#         logging.debug (detail)
#         exit(1)
    log_entry('DEBUG', 2009, __name__, 'User list selected.')
    return tl_users


def user_exists (v_user):
#    global db
    dml= "SELECT usr_id FROM tb_users where Upper(usr_name) = Upper('" + str(v_user) + "');"
    v_user_id= exec_query(config.db, dml)
    log_entry('DEBUG', 2011, __name__, 'User existence checked')
    logging.debug(v_user_id)
    if (v_user_id):
        return True
    else:
        return False

#####################################################################################
#
# Business Access Layer
#
#####################################################################################

def create_user (l_user_record):
    v_user= l_user_record[1]
    if (user_exists (v_user)):
        log_entry ('WARNING', 2201, __name__, 'Not created! User already exist.')
        return False
    else:
        ok= insert_user_record (l_user_record)
        if (ok):
            return True
        else:
            return False


# def remove_user ():
#     # only the ones with 0 operations
#     pass

def modify_user (l_user_record):
    print ("executing BL...")
    ok= update_user_record(l_user_record)
    if (ok):
        return True
    else:
        return False


def get_user_list ():
    tl_users= get_all_users()
    # Convert list of tuples to list of lists
    ll_users = [list(elem) for elem in tl_users]
    return ll_users


#####################################################################################
#
# Presentation Access Layer
#
#####################################################################################

def interface_create_user():
    while (True):
        os.system('clear')
        print ("****  Create New User ****")
        user_name= str(input ("Name: "))
        user_role= int(input ("User_role: "))
        user_status= 'A'
        l_user_record= [0, user_name, user_role, user_status]
        print (l_user_record)

        # send to business layer
        ok= create_user(l_user_record)
        if (ok):
            print ("User " + user_name + " created")
        else:
            print ("User already exist.")
        x= input("Press Return to continue...")

def interface_show_users():
    while (True):
        ll_users= get_user_list()
        os.system('clear')
        print ("****  Show Users ****")
        print ("USER NAME \t\tUSER ROLE \t\t\tUSER STATUS")

        for l_user_record in ll_users:
            print (l_user_record[1] + "\t\t\t"+ config.user_role[l_user_record[2]] + "\t\t\t\t" + config.user_status [l_user_record[3]])
        x= input("Press Return to continue...")
    print ("Tchau!")

def interface_alter_user():
    while (True):
        # Selecting user to modify
        ll_users= get_user_list()
        os.system('clear')
        print ("****  Show Users ****")
        print ("ID\tUSER NAME \t\tUSER ROLE \t\t\tUSER STATUS")
        for i in range(len(ll_users)):
            l_user_record= ll_users[i]
            print (str(i) +"\t"+ l_user_record[1] +"\t\t"+ config.user_role[l_user_record[2]] +"\t\t\t\t"+ config.user_status [l_user_record[3]])

        # Modifying user
        id = int(input("Inform user ID to change.."))
        l_user_record = ll_users[id]
        print ("Username: " + l_user_record[1])
        new_role= input ("User role: " + str(l_user_record[2]) + "\tNew: ")
        new_status= input ("Status: " + l_user_record[3] + "\tNew: ")
        record_updated= False
        if (len(str(new_role)) > 0 and  new_role != l_user_record[2]):
            print ("alterou user_role...")
            l_user_record[2]= new_role
            record_updated= True
        if (len(str(new_status)) > 0 and new_status != l_user_record[3]):
            print ("alterou status...")
            l_user_record[3]= new_status
            record_updated= True
        if (record_updated):
            ok= modify_user(l_user_record)
        if (ok):
            print ("User " + user_name + " altered")
        else:
            print ("User not altered.")


        x= input("Press Return to continue...")
