import sys
import datetime as dt
import struct
from serial import Serial
import serial
from crccheck.crc import Crc16Modbus as crc_modbus
from time import sleep

def get_crc(data_byte):
    tester=0xff
    crc_byte=bytearray([])
    crc_int=crc_modbus.calc(data_byte)
    temp=crc_int&tester
    #print(hex(temp),temp)
    crc_byte.append(temp)
    temp=(crc_int&(tester<<8))>>8
    #print(hex(temp),temp)
    crc_byte.append(temp)
    #print(crc_byte)
    return crc_byte 


def write_data(client,combined_command):
    received_data=''
    
    try:
        crc=get_crc(combined_command)
        #print(crc.hex())
        combined_command+=crc
        
        print('command sent is {}',combined_command)
        #print('command sent in hex is {}',combined_command.hex())
        for _ in range(2):
            client.write(combined_command)
            print( "write successful")
            sleep(0.1)
            received_data=client.read(1)
            print('received_data is: {}'.format(received_data))
            while(client.inWaiting()):
                received_data+=client.read()
            print(received_data.hex())
            #print('timi', bytearray(received_data))
    except Exception as e:
        print(e)
    received_datas=received_data.hex()    
    return received_datas


def voltage_reading(port,address):
    command=bytearray([address,0x03,0x20,0x00,0x00,0x02])
    voltage_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(voltage_reading,current_time) 

def current_reading(port,address):
    command=bytearray([address,0x03,0x20,0x02,0x00,0x02])
    current_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(current_reading,current_time)

def power_reading(port,address):
    command=bytearray([address,0x03,0x20,0x00,0x00,0x02])
    voltage_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(power_reading,current_time) 

'''
def volta_reading(port,address):
    command=bytearray([address,0x03,0x20,0x00,0x00,0x02])
    voltage_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(voltage_reading,current_time)
''' 
def frequency_reading(port,address):
    command=bytearray([address,0x03,0x20,0x0E,0x00,0x02])
    frequency_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(frequency_reading,current_time)

def active_power_reading(port,address):
    command=bytearray([address,0x03,0x20,0x06,0x00,0x02])
    active_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(active_reading,current_time)

def reactive_power_reading(port,address):
    command=bytearray([address,0x03,0x20,0x04,0x00,0x02])
    reactive_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(reactive_reading,current_time)

def apparent_power_reading(port,address):
    command=bytearray([address,0x03,0x20,0x08,0x00,0x02])
    apparent_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(apparent_reading,current_time)

def energy_reading(port,address):
    command=bytearray([address,0x03,0x40,0x00,0x00,0x02])
    energy_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(energy_reading,current_time)

def pf(port,address):
    command=bytearray([address,0x03,0x20,0x04,0x00,0x02])
    pf_reading = write_data(port,command)
    ct=dt.datetime.now()
    current_time = ct.strftime('%Y-%m-%d %H:%M:%S')
    #print('date time is: {}'.format(current_time))
    return(pf_reading,current_time)
 






 
