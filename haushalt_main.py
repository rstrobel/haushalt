#########################################################
#
# Presentation Layer
#
#########################################################


#########################################################
#
# Business Layer
#
#########################################################

def process_operation(l_operation_record):
    # Receive the input of an operation and process it

def transfer_money(acc_id_origin, acc_id_destination, money_value):
    # Transfer money from one account to another

def retrieve_operations(l_acc_id, dt_initial, dt_final):
    # create a dictionary with all the operations informed in l_acc_id
    # and in the period informed

def list_acc_operations(acc_id):

def list_balance(acc_id):

#########################################################
#
# Data Access Layer
#
#########################################################

def insert_operation (l_operation_record):

def delete_operation (opr_id):

def update_operation (opr_id, l_operation_record):

def insert_account (l_account_record):

def delete_account (l_account_record):

def update_account (l_account_record):

def insert_user (l_user_record):

def update_balance (acc_id, money_value):

#def update_account_payment_value (acc_id, money_value):
