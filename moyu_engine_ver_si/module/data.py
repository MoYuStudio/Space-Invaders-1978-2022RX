
import sqlite3

from moyu_engine_ver_si.config import config as C

class Data:
    def __init__(self):
        self.database = sqlite3.connect('moyu_engine_ver_si/config/config.db')
        self.db = self.database.cursor()
        pass

    def load(self,database_tablename):
        C.config[str(database_tablename)] = {}
        for data in self.db.execute('select * from {}'.format(database_tablename)):
            C.config[str(database_tablename)][data[0]] = data[1]
        self.database.commit()
        self.database.close()

    def updata(self):
        for table in C.config:
            for data in C.config[table]:
                self.db.execute('update {} set info = "{}" where name = "{}"'.format(table,C.config[table][data],data))
        self.database.commit()
        self.database.close()

if __name__ == '__main__':
    pass