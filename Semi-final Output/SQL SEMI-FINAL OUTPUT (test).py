import mysql.connector
from mysql.connector import errorcode
import os


class Pre_Enrollees_DB:
    def __init__(self, user: str, password: str, host: str, database: str):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        #self.cursor = self.conn.cursor()

    @property
    def get_user(self):
        return self.user
    
    @get_user.setter
    def set_user(self, user):
        self.user = user

    @property
    def get_password(self):
        return self.password

    @get_password.setter
    def set_password(self, password):
        self.password = password
    
    @property
    def get_host(self):
        return self.host
    
    @get_host.setter
    def set_host(self, host):
        self.host = host

    @property
    def get_database(self):
        return self.database
    
    @get_database.setter
    def set_database(self, database):
        self.database = database

    def connect(self):
        try:
            con = mysql.connector.connect(user=self.user, 
                                        password=self.password, 
                                        host=self.host, 
                                        database=self.database)
            print('Connection successful')
            return con
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def testlang(self):
        connected = self.connect()

        if connected:
            print('okay nagana')
        else:
            print('aguy')

SQL_Pre_Enrollees_DB = Pre_Enrollees_DB('root', 'CS2025EU', 'localhost', 'Pre_Enrollees')

SQL_Pre_Enrollees_DB.testlang()
