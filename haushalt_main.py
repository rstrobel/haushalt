#!/usr/bin/env python3
from user_mgmt.lib_user_dl import *
from common.lib_common_db import *
from common.lib_common_log import *
import psycopg2

# get parameter prd or dev




print ("Executing main code...")

################# Initialization tasks... #################

# Set global variables
running_env = 'dev'
log_level = 'DEBUG'     # 0 = DEBUG,  1 = INFO, 2 = WARNING
version="1.0"

# Open log file
open_log (log_level, running_env, version)

# Connect to the database
db_con= stablish_db_connection (running_env)


# open_log(log_level, running_env,version)
# logging.info ('some message');
# logging.debug ('some debug message')
