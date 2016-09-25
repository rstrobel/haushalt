#!/usr/bin/env python3
__version__ = "0.01"

user='ronald'
#
# from common.lib_common_db import *
# from common.lib_common_log import *
# from common.lib_common_par import *
#
# from user_mgmt.lib_user_dl import *
from user_mgmt.lib_user_bl import *
# from user_mgmt.lib_user_pl import *


import psycopg2
import os
import sys
import getopt
import json
import logging
import datetime
import datetime


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
        ok= lib_user_bl.create_user(l_user_record)
        if (ok):
            print ("User " + user_name + " created")
        else:
            print ("User already exist.")
        x= input("Press Return to continue...")

# def interface_show_users():
#     user_role= ('administrator', 'user')
#     user_status= ('active', 'inactive')
#     while (True):
#         os.system('clear')
#         print ("****  Show Users ****")
#         print ("Username \t\tUser Role \t\tUser Status")
#         for l_user_record in ll_users:
#             print (l_user_record[1] + "\t\t" + user_role(l_user_record[2]) + "\t\t"+ user_status(l_user_record[3])
#         x= input("Press Return to continue...")
