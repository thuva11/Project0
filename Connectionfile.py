import mysql.connector as sql
from Function import *
from datetime import date
class Connect:
    @staticmethod
    def connection():
        try:
            connection = sql.connect(host="127.0.0.1",
                                     user="root",
                                     password="toor",
                                     db="bank"
                                     )

            cursor = connection.cursor()
            return [connection, cursor]
        except sql.Error as e:
            print(e)