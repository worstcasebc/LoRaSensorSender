# LoRaSensorSender
First project using micropython on Pycom LoPy4 to transmit sensor-data via LoRa

## Overview
That project consists of two components, the sender and a [receiver](https://github.com/worstcasebc/LoRaSensorReceiver). Both are running on LoPy4 and communicate via Raw-LoRa. Both components can be found in my Git-repositories. I use VSCode, but feel free to use an IDE of your choice.

## Sender
That component sends the temperature and humidity data via Raw-LoRa and adds the own device-ID (last 4 chars) for possibly identification reasons.

### Hardware used
* [Pycom LoPy4](https://pycom.io/product/lopy4/) (LoRa-antenna is necessary to not destroy your board)
* [Pycom Expansion Board 2.0](https://pycom.io/product/expansion-board-3-0/)
* [Sharp Memory Display](https://www.exp-tech.de/displays/lcd/5090/sharp-memory-display-breakout-1.3-96x96-silver-monochrome)
* [DHT22 Temperature and Humidity sensor6](https://www.exp-tech.de/sensoren/temperatur/7784/dht22-am2302-feuchtigkeits-und-temperatursensor)
* a few jumper cables and a breadboard

### Wiring Sender
|LoPy4          |Sensor         |Description                            |
| ------------- | ------------- | ------------------------------------- |
| 3.3V          | VCC           | works with 3.3V                       |
| GND           | GND           |                                       |
| P9  (G16)     | OUT           |                                       |


### Used libraries
to be described

### Code
to be described
