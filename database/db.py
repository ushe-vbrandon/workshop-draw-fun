"""
Database

Database context manager
"""


import sqlite3



default_db = "drawfun.db"



class DatabaseContextManager():
    def __init__(self, db_file: str):
        self.db_file = db_file
        self._connection = None
        
    @property
    def connection(self):
        if self._connection is None:
            self._connection = sqlite3.connect(self.db_file)
        return self._connection
           
    def __enter__(self):
        return self.connection
       
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._connection.close()



def get_db(db_file: str = default_db):
    return DatabaseContextManager(db_file)


def query_db(query: str, db_file: str = default_db):
    if db_file is None:
        db_file = default_db
    with get_db(db_file) as conn:
        return conn.execute(query).fetchall()