import pandas as pd
from sqlalchemy import create_engine


class SQLConnector(object):
    """
    A wrapper class to connect to any SQL database using SQLAlchemy and
    read/write data in pandas DataFrame.
    """

    def __init__(self, dialect, user='', passwd='', host='', port='', db='', **kwargs):
        db_url = {
            'mysql': 'mysql+mysqlconnector://{}:{}@{}:{}/{}',
            'hive': 'hive://{}:{}@{}:{}/{}',
        }
        db_url = db_url[dialect].format(user, passwd, host, port, db)
        self.engine = create_engine(db_url)

    def execute(self, sql_statement):
        """ A function to execute sql directly """
        with self.engine.connect() as con:
            result = con.execute(sql_statement)
        try:
            result = [item for item in result]
        except:
            pass
        return result

    def find(self, query, **kwargs):
        """Returns a pandas DataFrame as a result of the SQL query"""
        return pd.read_sql(query, self.engine, **kwargs)
