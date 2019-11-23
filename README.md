# LoRaSensorSender
First project using micropython on Pycom LoPy4 to transmit sensor-data via LoRa

## Overview
That project consists of two components, the sender and a [receiver](https://github.com/worstcasebc/LoRaSensorReceiver). Both are running on LoPy4 and communicate via Raw-LoRa. Both components can be found in my Git-repositories. I use VSCode, but feel free to use an IDE of your choice.

## Sender
That component sends the temperature and humidity data via Raw-LoRa and adds the own device-ID (last 4 chars) for possibly identification reasons.

<img src="https://user-images.githubusercontent.com/58089458/69477069-0d972280-0de2-11ea-8d02-de4a6a5f4bb0.jpg" width="600" height="400" />

### Hardware used
* [Pycom LoPy4](https://pycom.io/product/lopy4/) (LoRa-antenna is necessary to not destroy your board)
* [Pycom Expansion Board 2.0](https://pycom.io/product/expansion-board-3-0/)
* [Sharp Memory Display](https://www.exp-tech.de/displays/lcd/5090/sharp-memory-display-breakout-1.3-96x96-silver-monochrome)
* [DHT22 Temperature and Humidity sensor6](https://www.exp-tech.de/sensoren/temperatur/7784/dht22-am2302-feuchtigkeits-und-temperatursensor)
* a few jumper cables and a breadboard

### Wiring receiver
|LoPy4          |Sensor         |Description                            |
| ------------- | ------------- | ------------------------------------- |
| 3.3V          | VCC           | works with 3.3V                       |
| GND           | GND           |                                       |
| P9  (G16)     | OUT           |                                       |


### Used libraries
I googled for an existing DHT-library for micropython and [found that one](https://github.com/JurassicPork/DHT_PyCom), that I could use without a change. 

### Code
The code is simple enough: Read LoRa-Mac for identification (last 4 chars will be send with the transmission), create a LoRa-socket, pack the data in a struct and send it. Then fall into sleep for 60 seconds.
The data are packed as followed:
```python
datatosend = struct.pack('<4shh', devID, dataTemp,  dataHum)
```
DevID is sent as string with length 4. Temperature and humidity were read from the sensor as float-values but were multiplied by 100 and converted to int for payload reasons.