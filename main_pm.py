import sys
import datetime as dt
import struct
from serial import Serial
import serial
from crccheck.crc import Crc16Modbus as crc_modbus
from time import sleep
sys.path.append('\Desktop\Power meter')
import data_proccessor
import sqliteservices


port=Serial(port='COM7',baudrate=9600,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)
address=11

def data_dict(address=11):
    data= {}
    data['device_address'] = 11
    data['read_at'] = data_proccessor.voltage_data(port,address)[1]
    data['voltage'] = data_proccessor.voltage_data(port,address)[0]
    data['current'] = data_proccessor.current_data(port,address)[0]
    data['pf'] = data_proccessor.pf_data(port,address)[0]
    data['frequency'] = data_proccessor.frequency_data(port,address)[0]
    data['energy'] = data_proccessor.energy_data(port,address)[0]
    data['active_power'] = data_proccessor.active_power_data(port,address)[0]
    data['reactive_power'] = data_proccessor.reactive_power_data(port,address)[0]
    data['apparent_power'] = data_proccessor.apparent_power_data(port,address)[0]
    
    
    print(data)
    return(data)

def insert_db():
    data=data_dict()
    sqliteservices.pm_data(data)
    
#data_dict()



