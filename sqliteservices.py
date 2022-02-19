import datetime
import os
import io
import sqlite3
from sqlite3 import Error

#db_path = '\Desktop\Power meter\chintsqlite.db'



def pm_data(data):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    conn = sqlite3.connect(dir_path+'/chintsqlite.db')
    cur = conn.cursor()

    #conn = sqlite3.connect(db_path)
    #cur = conn.cursor()
    
    done = cur.execute("INSERT INTO powermeter_logs (pm_Address, read_at,voltage,current,energy,active_power,reactive_power,apparent_power,pf,frequency,uploaded) values (?,?,?,?,?,?,?,?,?,?,?)",
    ( data['device_address'], data['read_at'],data['voltage'], data['current'],
    data['energy'],data['active_power'], data['reactive_power'], data['apparent_power'], data['pf'], data['frequency'], 0))
    
    conn.commit()
    conn.close()
    #return done
