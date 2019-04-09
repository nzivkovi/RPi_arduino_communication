import smbus
import struct
import time

arduino = smbus.SMBus(1)

address = 0x55

i2c_data = [0 for i in range(5)]

def read_sensor_data():
    global i2c_data
    d = arduino.read_i2c_block_data(address, 1)
    i2c_data = [struct.unpack('<f', ''.join(chr(i) for i in d[0:4]))[0],
                struct.unpack('<f', ''.join(chr(i) for i in d[4:8]))[0],
                struct.unpack('<H', ''.join(chr(i) for i in d[8:10]))[0],
                struct.unpack('<H', ''.join(chr(i) for i in d[10:12]))[0],
                struct.unpack('<H', ''.join(chr(i) for i in d[12:14]))[0]]
    print(i2c_data)

if __name__ == '__main__':
    for i in range(1000):
        try:
            read_sensor_data()
        except:
            print("Error")
        time.sleep(0.01)