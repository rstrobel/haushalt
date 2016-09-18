#!/usr/bin/env python3
__version__ = "0.01"
__name__ = "__main__"

# from user_mgmt.lib_user_dl import *
from common.lib_common_db import *
from common.lib_common_log import *
from common.lib_common_par import *
import psycopg2
import sys
import json
import logging
import datetime




################# Initialization tasks... #################

# Get command line parameters
running_env, log_level = get_command_line_parameters(sys.argv)

# Start logging
open_log (log_level, running_env)

# Open db connection
db_con= stablish_db_connection (running_env)



# Close db connection
close_db_connection (db_con)
