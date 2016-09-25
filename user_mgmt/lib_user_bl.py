#!/usr/bin/env python3
__version__ = "0.01"
#########################################################
#
# Business Layer
#
#########################################################

from common.lib_common_db import *
from common.lib_common_log import *
from common.lib_common_par import *

from user_mgmt.lib_user_dl import *
from user_mgmt.lib_user_bl import *
from user_mgmt.lib_user_pl import *

import psycopg2
import os
import sys
import getopt
import json
import logging
import datetime

def create_user (l_user_record):
    v_user= l_usr_record[1]
    if (user_exists (v_user)):
        log_entry ('WARNING', 2201, __name__, 'Not created! User already exist.')
        return False
    else:
        ok= insert_user_record (l_user_record)
        if (ok):
            return True
        else:
            return False


def remove_user ():
    # only the ones with 0 operations
    pass

def modify_user ():
    pass

def get_user_list ():
    l_users= get_all_user_id
