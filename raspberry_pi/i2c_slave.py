import time
import pigpio
import struct
import threading

pi = pigpio.pi()
e = None

I2C_ADDR=0x13

def i2c(id, tick):
    global pi
    s, b, d = pi.bsc_i2c(I2C_ADDR)
    print(b)
    if b:
        if len(d)==6:
            print("IR sensors data")
            print(struct.unpack('H', d[0:2])[0])
            print(struct.unpack('H', d[2:4])[0])
            print(struct.unpack('H', d[4:6])[0])
        elif len(d)==8:
            print("Wheel encoders data")
            print(bytesToLong2(d[0:4]))
            print(bytesToLong2(d[4:8]))
        else:
            print("error")

def bytesToLong(bytesArray):
    return bytesArray[3] | (bytesArray[2] | (bytesArray[1] | bytesArray[0] << 8) << 8) << 8

def bytesToLong2(bytesArray):
    return bytesArray[0] | (bytesArray[1] | (bytesArray[2] | bytesArray[3] << 8) << 8) << 8

def init_i2c():
    global e
    print("start")
    if not pi.connected:
        print('exit')
        exit()
    e = pi.event_callback(pigpio.EVENT_BSC, i2c)
    pi.bsc_i2c(I2C_ADDR) 


def close_i2c():
    global e
    e.cancel()
    pi.bsc_i2c(0)
    pi.stop()

def watch_params():
    while True:
        i = 0

if __name__ == '__main__':
    t1 = threading.Thread(target=init_i2c)
    t1.start()
    t2 = threading.Thread(target=watch_params)
    t2.start()
    close_i2c()
