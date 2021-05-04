import mysql.connector
import sys

class LLBOTdb():
    
    def __init__(self):
        self.__instance = None

    def get_connection(self):
        try:
            return  mysql.connector.connect(host="127.0.0.1",user="root",password="Br0qzzz!",database="llbot")#pymysql.connect(LOCATION, USERNAME, PASSWORD, SCHEMA)
        except Exception as e:
            print(e, file=sys.stderr)