import time
import pycom
from network import LoRa
import socket
import machine
import dht
import struct
import ubinascii

# the LoRa-MAC will be used as identificator for sending (it's reduced to last 4 chars to reduce payload)
devID = ubinascii.hexlify(LoRa().mac())
devID = devID[12:16]
print("DeviceID: {}".format(devID))

# initiate LoRa for EU-frequency
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# initiate the sensor with pin P9 on the LoPy4
dhtPin = machine.Pin('P9', machine.Pin.OPEN_DRAIN)
sensor = dht.DHT(dhtPin,1)

# read all values and possibly errors from sensor
result = sensor.read()
time.sleep_ms(200)

print('Temperature / Humidity: {:3.2f} / {:3.2f}'.format(result.temperature/1.0, result.humidity/1.0))

# switch off the sensor for deep sleep
dhtPin.mode(dhtPin.OUT)
dhtPin(0)

# prepare data for sending as in-values for payload reasons
dataTemp = int(result.temperature*100)
dataHum  = int(result.humidity*100)

# pack the data for lower payload
datatosend = struct.pack('<4shh', devID, dataTemp,  dataHum)
print('LoRa send: {}'.format(datatosend))
print('Size: {}'.format(len(datatosend)))

# unpack it for validation reasons only
dataDevID, datatemp, datahum = struct.unpack('<4shh', datatosend)
print('decoded to: {} - {} / {}'.format(dataDevID.decode(), datatemp, datahum))

# send the data via Raw LoRa
s.setblocking(True)
s.send(datatosend)
s.setblocking(False)

# enter deep sleep for 60 seconds
print("Entering sleep mode for 60 sec now ... Good night!")
machine.deepsleep(60000)