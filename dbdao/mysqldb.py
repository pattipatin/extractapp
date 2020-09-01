import mysql.connector
from datetime import datetime
from mysql.connector import Error
from config.config import dbconfig
import csv
import time

class mysqldb:
    __conn = None
    __cursor = None

    def __init__(self):
      
       #Sales MySQL DB connection parameters from config/dbconfig.json 
       dbconf = dbconfig['salesdbmysql']

       self.__conn = mysql.connector.connect(host = dbconf['host'],
                                             user = dbconf['user'],
                                             password = dbconf['password'],
                                             db = dbconf['db'])
       self.__cursor = self.__conn.cursor()
    
 
    def execute(self, sql, params=None):
        self.__cursor.execute(sql, params or ())

    # TODO: Save file and move it to host machine 
    def save(self, file):
        pass

    def rowcount(self):
        return self.__cursor.rowcount

    def fetchrows(self, qname):

        #TODO: Get the file and dir from a config file
        outfile = "/data/extracts/" + qname + datetime.today().strftime('%Y-%m-%d-%H-%M-%S') + ".csv"

        # TODO: Handle errors opening files
        # TODO: Get column names from the query results and write to the file

        with open(outfile, "w") as f:
            row = self.__cursor.fetchone()

            while row is not None:
                w = csv.writer(f)
                w.writerow(row)
                print(row)
                row = self.__cursor.fetchone()

        f.close()
        time.sleep(2)

    def close(self):
        self.__conn.close();
        self.__cursor.close();
