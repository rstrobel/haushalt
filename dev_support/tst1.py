import json

# input = '''
# [
#     { "dbname" : "db_dev",
#       "user" : "haushalt",
#       "host" : "rastafari.net",
#       "password" : "dagget03"
#     } ,
#     { "dbname" : "db_prd",
#       "user" : "haushalt2",
#       "host" : "rastafari.net",
#       "password" : "dagget06"
#     }
# ]'''

input = '''
{
    "prd" : [
        "db_prd",
        "haushalt",
        "rastafari.net",
        "dagget03"
    ],
    "dev": [
        "db_dev",
        "haushalt",
        "rastafari.net",
        "dagget03"
    ]
}'''
with open('data.json', 'r') as fp:
    data = json.load(fp)
    
db_connectors = json.loads (input)

print ("all_db_connectors:")
print (db_connectors)
print (db_connectors['prd'])

with open('data.json', 'w') as fp:
#    json.dump(db_connectors, fp)
    json.dump(db_connectors, fp, indent=4)

# for item in all_db_configs:
#     if (item['dbname'] == 'db_prd'):
#         print ('Db name: ', item['dbname'])
#         print ('use: ', item['user'])
#
# print ("-------------------")
# print ("all_db_configs.db_prd:")
# print (all_db_configs[1].dbname)
