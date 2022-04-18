
import sqlite3

import moyu_engine_ver_si.config.config as C

class Data:
    def __init__(self):
        pass

    def decorator_database_connect_and_close(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            self.database = sqlite3.connect('moyu_engine_ver_si/config/config.db')
            self.db = self.database.cursor()
            func(*args, **kwargs)
            self.database.commit()
            self.database.close()
        return wrapper

    @decorator_database_connect_and_close
    def load(self,database_tablename):
        C.config[str(database_tablename)] = {}
        for data in self.db.execute('select * from {}'.format(database_tablename)):
            C.config[str(database_tablename)][data[0]] = data[1]

        return C.config

    @decorator_database_connect_and_close
    def updata(self):
        for table in C.config:
            for data in C.config[table]:
                self.db.execute('update {} set info = "{}" where name = "{}"'.format(table,config[table][data],data))

if __name__ == '__main__':
    pass