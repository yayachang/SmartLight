# SmartLight
Use Android to control lights at your home (ESP8266) 

Hardware, firmware:

1. ESP8266 ESP-01

2. USB to TTL

3. 5V to 3.3V converter

4. LED

Run micropython on your ESP8266

You can see: https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/
  
It's a good tutorial, including setup up building firmaware enviroment, flash firmware.

Software:

Home Server:

1. Connecting to internet so that you can use App to control your device outside home.

2. Receive command form App, and then send command to ESP8266(then ESP8266 send signal to your device).

3. Can do scheduling.

App:

Connect to your home server, get/set device stasus from home server


