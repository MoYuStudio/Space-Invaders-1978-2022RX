
import sqlite3

class Data:
    '''
=== MoYu Engine === 
[ Data 数据模块 ]
数据库模块，用于读取数据库中的数据，并将数据存储在内存中。
变量：
    数据库路径 database_path = 'string'
    数据库列表 database_list = {'string': ['string','string'],...}
    数据库格式 database_format = {'string': ['string','string'],...}
    配置 config = {}
函数：
    加载数据库 load()
    更新数据库并提交 update()
    '''
    def __init__(self):
        # 数据库路径
        self.database_path = 'database/'
        # 数据库列表
        self.database_list = {'config': ['main','window','ship','alien','bullet','buff']}
        # 数据库格式
        self.database_format = {'config': ['config','data']}
        # 配置
        self.config = {}

    # 加载数据库
    def load(self):
        # 历遍数据库列表
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

    # 更新数据库并提交
    def update(self):
        # 历遍数据库列表
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
    print(Data.__doc__)
    # data = Data()
    # data.load()
    # C = data.config['config']
    # C['main']['test'] = 1
    # data.update()
    # print(data.config)



