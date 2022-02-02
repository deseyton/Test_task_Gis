import psycopg as pg
import pandas.io.sql as psql

class GetPG:
    def __init__(self, query, db='Gis', passw='password'):
        self.connection =pg.connect("dbname={0} user=postgres password={1}".format(db, passw))
        self.query = query
        self.getPGdf

    @property
    def getPGdf(self):
        try:
            self.df = psql.read_sql_query(self.query, self.connection)
        except Exception as err:
            print("\033[31m {}".format(err))
        finally:
            self.connection.close()
