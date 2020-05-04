# This file contain an utility class for our DB

####################################################################
#                             import
####################################################################
import mysql.connector  # to use the connector of mySQL
from mysql.connector import Error  # error handle mySQL errors


####################################################################
#                              class
####################################################################
# this class was created to avoid repeated connection in our main file, so with this we can simply
# call, in our REST request, for example: db.insert_student
class Db(object):
    ####################################################################
    #                             constructor
    ####################################################################
    # The constructor accept:
    # 1 - The host with a default value equal to 'localhost'
    # 2 - The database with a default value equal to None
    # 3 - The user with a default value equal to root
    # 4 - The database with a default value equal to ''
    # In the constructor is also initialized the connection to the database and the cursor
    def __init__(self, host='localhost', database=None, user='root', password=''):
        self.__host = host
        self.__database = database
        self.__user = user
        self.__password = password
        self.__connection = mysql.connector.connect(host=self.__host,
                                                    database=self.__database,
                                                    user=self.__user,
                                                    password=self.__password)
        self.__cursor = self.__connection.cursor()

    ####################################################################
    #                             decorators
    ####################################################################
    # with this decorator we avoid to write the function with every insert operation into database
    @classmethod
    def __connection(cls):
        # wrapper function
        def wrapper(self, *args, **kwargs):
            try:
                # return the query, the record of tuple we want to insert and the message to print in console
                db_query, db_record_tuple, message = cls(*args, **kwargs)
                # if the values of all variables are not Null execute the operation
                if db_query and db_record_tuple and message:
                    self.__cursor.execute(db_query, db_record_tuple[1])
                    self.__connection.commit()
                    print(message)
                # else raise an error
                else:
                    raise Error

            except Error as error:
                print(f"Failed to insert into MySQL table {error}")

            finally:
                # finally close the connection
                if self.__connection.is_connected():
                    self.__cursor.close()
                    self.__connection.close()
                    print("MySQL connection is closed")
        return wrapper

    ####################################################################
    #                             db methods
    ####################################################################
