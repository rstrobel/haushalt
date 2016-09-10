#
# haushalt_functions.py
#

#########################################################
#
# Presentation Layer
#
#########################################################

def input_operation_record():
    # Collect the inputs of a operation. return the input in the list l_operation_record

def input_operation_report_parameters():
    # Collect the parameters


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


#########################################################
#
# Data Access Layer
#
#########################################################
def insert_operation (l_operation_record):

def delete_operation (opr_id):

def update_operation (opr_id, l_operation_record):
