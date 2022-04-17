
import sqlite3
 
data = sqlite3.connect('data.db')
c = data.cursor()

data_name = 'window_widen'

cursor = c.execute('select * from main where name = "{}"'.format(str(data_name)))

dataline = 2
data_out = cursor.fetchone()
print(data_out[dataline])
print(type(data_out[dataline]))


data.close()