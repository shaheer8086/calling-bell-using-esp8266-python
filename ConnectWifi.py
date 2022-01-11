#this file is for if you want to set a static ip for the module
def connect():
    import network
    
    #type below the ip that you want to reserve
    ip        = '192.168.1.10'
    subnet    = '255.255.255.0'
    gateway   = '192.168.1.1'
    dns       = '8.8.8.8'
    #username of your network
    ssid      = "yourSSID"
    #password of your network
    password  =  "yourPassword"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.ifconfig((ip,subnet,gateway,dns))
    station.connect()
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())

def disconnect():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)
