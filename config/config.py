import json

dbconfig = {}

with open('config/dbconfig.json') as configfile:
    dbconfig = json.load(configfile)
    #print(dbconfig)
    #print(dbconfig['salesdbmysql'])
