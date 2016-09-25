#!/usr/bin/env python3
__version__ = "0.01"
__name__ = "__main__"

import sys

import config
from common.lib_common_par import *
from common.lib_common_log import *
from common.lib_common_db import *

from user_mgmt.lib_user import *




def main(argv):
    print ("executing main. argv is:")
    ################# Initialization tasks... #################

    # Get command line parameters
    running_env, log_level = process_command_line_parameters(argv)
    print ("running env " + running_env)
    print ("log_level: " + log_level)
    # Start logging
    open_log (log_level, running_env)

    # Connect to database
    config.db= db_connect(running_env)
    print ("testing db...")
    test_db_connection(config.db)

    # Create new user
    #interface_create_user()
    #interface_show_users()
    interface_alter_user()

if __name__ == '__main__':
    main(sys.argv[1:])
