from serial import Serial
import serial
from crccheck.crc import Crc16Modbus as crc_modbus
from time import sleep
import json
import time
import datetime as dt
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import sys
import serial
from serial import Serial
import struct

port=Serial(port='COM7',baudrate=9600,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)



def get_crc(data_byte):
    tester=0xff
    crc_byte=bytearray([])
    crc_int=crc_modbus.calc(data_byte)
    temp=crc_int&tester
    print(hex(temp),temp)
    crc_byte.append(temp)
    temp=(crc_int&(tester<<8))>>8
    print(hex(temp),temp)
    print('My crc temp is {}',temp)
    crc_byte.append(temp)
    print('My crc byte is {}',crc_byte)
    return crc_byte


def write_data(client,combined_command):
    received_data=''
    
    try:
        crc=get_crc(combined_command)
        print(crc.hex())
        combined_command+=crc
        
        print('command sent is {}',combined_command)
        print('command sent in hex is {}',combined_command.hex())
        for _ in range(2):
            client.write(combined_command)
            print( "write successful")
            sleep(0.1)
            received_data=client.read(1)
            print('received_data is: {}'.format(received_data))
            while(client.inWaiting()):
                received_data+=client.read()
            print(received_data.hex())
            print('timi', bytearray(received_data))
    except Exception as e:
        print(e)
    received_datas=received_data.hex()    
    return received_datas
#combined_command=[0x00]
command=bytearray([0x0b,0x03,0x20,0x00,0x00,0x02])
#command=bytearray([11,0x03,0x01,0x5C,0x00,0x10])
voltage =write_data(port,command)
voltage_reading=voltage[6:14]
print(voltage_reading)
#first_byte= voltage[12:14]
voltage_byte= ['3',0 ]
print(voltage_byte)
first_byte= '0x'+voltage[12:14]
print(type(first_byte))
voltage_byte=[].append(first_byte)
second_byte= '0x'+voltage[10:12]
voltage_byte=[].append(second_byte)
third_byte= '0x'+voltage[8:10]
voltage_byte=[].append(third_byte)
fourth_byte= '0x'+voltage[6:8]
voltage_byte=[].append(fourth_byte)

print('my  first,second,third and fourth byte voltage are :{} {} {} {}'.format(first_byte,second_byte,third_byte,fourth_byte))
print('my voltage byte is :{}'.format(voltage_byte))
print('my voltage is :{}'.format(voltage[6:14]))

'''
voltage_struct= bytearray(voltage_byte)

struct.pack('f',voltage_struct)
'''
'''
def reverse_byte(bytes_data):
    #print('normal bytes is: {}'.format(bytes(bytes_data).hex()))
    #data=
    reversed_data=[]
    
    _data= bytes_data[16:18]
    #reversed_data[1]= bytes_data[6:8]
    reversed_data.append(_data)
    #reversed_data.append(bytes_data[x+1])
    #print('reversed bytes is: {}'.format(reversed_data))
    return bytearray(reversed_data)
#print(reverse_byte(voltage))
#print('my voltage byte is {}',voltage)

'''
#print('my voltage byte is {}',voltage[14:16])

#voltagea= struct.unpack('f',reverse_byte(voltage))
#voltagea= struct.unpack('>f',voltage)
#print('voltage reading from the device is {}',voltagea)




