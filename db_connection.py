import logging
from typing import List

import pyodbc


# server = "ip_address, port"
class DbConnection:
    def __init__(self, server, database, uid, pwd):
        self.server = server
        self.database = database
        self.uid = uid
        self.pwd = pwd
        # self.table = table
        self.cursor = None
        self.field_names: List = list()

    # STEP 1 GET CURSOR FROM CONNECTION
    def get_cursor(self):
        con = None
        try:
            con = pyodbc.connect(driver='SQL Server',
                                 server=self.server,
                                 database=self.database,
                                 uid=self.uid,
                                 pwd=self.pwd)
        except pyodbc.Error as e:
            logging.exception(e)
        self.cursor = con.cursor()

    # STEP 2 GET LIST OF ROWS
    def get_list_of_rows(self, query: str):
        with self.cursor.execute(query):
            # cursor.description is available ONLY after cursor.execute
            self.field_names = [i[0] for i in self.cursor.description]
            return self.cursor.fetchall()

    # def get_list_of_col_name(self):
    #     with self.
