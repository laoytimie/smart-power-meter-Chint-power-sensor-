import sys
sys.path.append('\Desktop\Power meter')
import chint_data_paser
import sys
import datetime as dt
import struct
from serial import Serial
import serial
from crccheck.crc import Crc16Modbus as crc_modbus
from time import sleep
#port=Serial(port='COM7',baudrate=9600,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=1)
#address=11


def voltage_data(port,address):
    voltage,date_time= chint_data_paser.voltage_reading(port,address)
    #frequency_byte= bytes('0x00', 'utf-8')+ frequency[3:5]
    #print(len(frequency))
    reversed_data=[]
    for x in range(len(voltage)):
        reversed_data.append(voltage[x])
  
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    voltage_reading= struct.unpack('f',total_byte_array)[0]
    
    #print('my voltage is {} at {}'.format(voltage_reading,date_time))
    return(voltage_reading,date_time)
    
def current_data(port,address):
    current,date_time= chint_data_paser.current_reading(port,address)
    #frequency_byte= bytes('0x00', 'utf-8')+ frequency[3:5]
    #print(len(frequency))
    reversed_data=[]
    for x in range(len(current)):
        reversed_data.append(current[x])
  
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    current_reading= struct.unpack('f',total_byte_array)[0]
    
    #print('my current is {} at {}'.format(current_reading,date_time))
    return(current_reading,date_time)

def pf_data(port,address):
    pf,date_time= chint_data_paser.pf(port,address)
    reversed_data=[]
    for x in range(len(pf)):
        reversed_data.append(pf[x])
  
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    pf_reading= struct.unpack('f',total_byte_array)[0]
    #pf_readings=pf_reading[0]*100000
    
    #print('my pf is {} at {}'.format(pf_reading,date_time))
    
    return(pf_reading,date_time)

def frequency_data(port,address):
    frequency,date_time= chint_data_paser.frequency_reading(port,address)
    #frequency_byte= bytes('0x00', 'utf-8')+ frequency[3:5]
    #print(len(frequency))
    reversed_data=[]
    for x in range(len(frequency)):
        reversed_data.append(frequency[x])
        #reversed_data.append(frequency[x+1]) 
    #frequency_reading= struct.unpack('f',frequency_byte)
    #total_byte=[]
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    frequency_reading= struct.unpack('f',total_byte_array)[0]
    
    #print('my frequency is {} at {}'.format(frequency_reading,date_time))
    return(frequency_reading,date_time)
def active_power_data(port,address):
    active_power,date_time= chint_data_paser.active_power_reading(port,address)
    reversed_data=[]
    for x in range(len(active_power)):
        reversed_data.append(active_power[x])
  
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    active_power_reading= struct.unpack('f',total_byte_array)[0]
    #pf_readings=pf_reading[0]*100000
    
    #print('my active power reading is {} at {}'.format(active_power_reading,date_time))
    
    return(active_power_reading,date_time)
def reactive_power_data(port,address):
    reactive_power,date_time= chint_data_paser.reactive_power_reading(port,address)
    reversed_data=[]
    for x in range(len(reactive_power)):
        reversed_data.append(reactive_power[x])
  
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    reactive_power_reading= struct.unpack('f',total_byte_array)[0]
    #pf_readings=pf_reading[0]*100000
    
    #print('my reactive power reading is {} at {}'.format(reactive_power_reading,date_time))
    
    return(reactive_power_reading,date_time)

def apparent_power_data(port,address):
    apparent_power,date_time= chint_data_paser.apparent_power_reading(port,address)
    reversed_data=[]
    for x in range(len(apparent_power)):
        reversed_data.append(apparent_power[x])
  
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    apparent_power_reading= struct.unpack('f',total_byte_array)[0]
    #pf_readings=pf_reading[0]*100000
    
    #print('my apparent power reading is {} at {}'.format(apparent_power_reading,date_time))
    
    return(apparent_power_reading,date_time)

def energy_data(port,address):
    energy,date_time= chint_data_paser.energy_reading(port,address)
    reversed_data=[]
    for x in range(len(energy)):
        reversed_data.append(energy[x])
  
    first_byte= int('0x'+reversed_data[6]+reversed_data[7], base=16)
    second_byte= int('0x'+reversed_data[8]+reversed_data[9],base=16)
    third_byte= int('0x'+reversed_data[10]+reversed_data[11],base=16)
    fourth_byte= int('0x'+reversed_data[12]+reversed_data[13], base=16)
    total_byte=[fourth_byte,third_byte,second_byte,first_byte]
    
    
    total_byte_array=bytearray(total_byte)
    #print(total_byte)
    energy_reading= struct.unpack('f',total_byte_array)[0]
    #pf_readings=pf_reading[0]*100000
    
    #print('my exponential active power reading is {} at {}'.format(energy_reading,date_time))
    
    return(energy_reading,date_time)




#energy_data(11)

#pf_data(11)
#frequency_data(11)
#active_power_data(11)
#reactive_power_data(11)
#apparent_power_data(11)
#current_data(11)
#voltage_data(11)
    
    
     
    