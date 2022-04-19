
import sqlite3

class Data:
    def __init__(self):
        self.database_path = 'moyu_engine_ver_si/config/'
        self.database_list = {'config': ['main','window']}
        self.database_format = {'config': ['config','data']}
        self.config = {}

    def load(self):
        for database in self.database_list:
            database_connect = sqlite3.connect(self.database_path+database+'.db')
            db = database_connect.cursor()
            self.config[database] = {}
            for table in self.database_list[database]:
                self.config[database][table] = {}
                for data in db.execute('SELECT * FROM ' + table):
                    self.config[database][table][data[0]] = data[1]
            database_connect.commit()
            database_connect.close()
        
        return self.config

    def update(self):
        for database in self.database_list:
            database_connect = sqlite3.connect(self.database_path+database+'.db')
            db = database_connect.cursor()
            if database == 'config':
                for table in self.config[database]:
                    for data in self.config[database][table]:
                        execute = 'update ' + table + ' set ' + self.database_format[database][1] + ' = ? where ' + self.database_format[database][0] + ' = ?'
                        db.execute(execute, (str(self.config[database][table][data]), data))
            database_connect.commit()
            database_connect.close()

if __name__ == '__main__':
    data = Data()
    data.load()
    C = data.config['config']
    C['main']['test'] = 1
    data.update()
    print(data.config)



