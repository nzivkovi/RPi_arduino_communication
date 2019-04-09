import wiringpi
import time

SPI_channel = 0
SPI_speed = 50000
wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSPISetup(SPI_channel, SPI_speed)


def long_to_bytes(num):
    bytes_array = [bytes([num >> i & 0xff]) for i in (24, 16, 8, 0)]
    print(bytes_array)
    return bytes_array


def send_data(data):
    byte_data = long_to_bytes(data)
    for byte in byte_data:
        wiringpi.wiringPiSPIDataRW(SPI_channel, byte)


def start_send_data():
    wiringpi.wiringPiSPIDataRW(SPI_channel, bytes([1 & 0xff]))


if __name__ == '__main__':
    #start_send_data()
    for i in range(100):
        send_data(i)
        time.sleep(0.5)
