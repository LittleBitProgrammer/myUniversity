# This file contain an utility class for our DB

####################################################################
#                             import
####################################################################
import mysql.connector  # to use the connector of mySQL


####################################################################
#                              class
####################################################################
# this class was created to avoid repeated connection in our main file, so with this we can simply
# call, in our REST request, for example: db.insert_student
class DatabaseConnector(object):
    ####################################################################
    #                             constructor
    ####################################################################
    # The constructor accept:
    # 1 - The host with a default value equal to 'localhost'
    # 2 - The database with a default value equal to None
    # 3 - The user with a default value equal to root
    # 4 - The database with a default value equal to ''
    # In the constructor is also initialized the connection to the database and the cursor
    def __init__(self, host='localhost', port=8080, database=None, user='root', password=''):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__user = user
        self.__password = password

    def get_connection(self):
        database = mysql.connector.connect(host=self.__host, port=self.__port, database=self.__database, user=self.__user, password=self.__password)
        return database
