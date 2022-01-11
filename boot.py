
# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

#if you set static ip for the module,the code is written in connectwifi.py,so you want to use that file you can uncomment the below two lines
#import Connectwifi
#Connectwifi.connect()
#if you uncomment the above two lines,comment all the lines below without the last line

ssid = 'type the ssid that you want to set for this module'
password = 'type your password that you want to set for this module'

#below commands for use your module as a web server purpose

#default ip that generates from this module is 192.168.4.1
#after write this code to module first you connect the wifi generate from this module that the ssid and password you wrote above
#after that you can open a browser and type the ip 192.168.4.1 and its opens a html page that we code in main.py

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

#uncomment the below codes that you are connecting your own wifi or network available

#station = network.WLAN(network.STA_IF)

#station.active(True)
#station.connect(ssid, password)

#while station.isconnected() == False:
 # pass

#print('Connection successful')
#print(station.ifconfig())

#here we are using D1 pin(GPIO5) in esp8266
led = Pin(5, Pin.OUT)  #the pin that you are connecting your bell






