# Local Library Import
from globals.constants import MysqlConnect
import mysql.connector as mysql

class Database:
    def __init__(self, connectorDetail:MysqlConnect):
        self.con = 0
        self.cd = connectorDetail
    def __enter__(self):
        self.con = mysql.connect(host=self.cd.host, user=self.cd.user,
                            passwd=self.cd.passwd, database=self.cd.database)
        return self.con
    def __exit__(self,exc_type, exc_value, traceback):
        self.con.close()