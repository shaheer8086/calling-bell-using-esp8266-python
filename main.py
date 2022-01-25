
# Complete project details at https://RandomNerdTutorials.com

def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
    
    
 #uncomment below function for bottom section
#def web_page():
 # led.value(1)
  #time.sleep(0.5)
  #led.value(0)
    
    #add the below scipt in html code after <head> open tag,for to close automatically the web page in a time delay
    #<script>setTimeout(function()window.close() }, 100);</script>
  
  html = """<html><head> <title>Milestone Door Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #276ceb; border: none; 
  border-radius: 5px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>Milestone Door Server</h1><a href="/?led=on"><button class="button">OPEN</button></a></p></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)  
  led_on = request.find('/?led=on')

  #i adjust the on off button switch to just get pulse for a second for exact use of calling bell
  #replace the next line with this cammand for get switch on and of mode 'led_off = request.find('/?led=off')'
  led_off = request.find('/?led=on')
  if led_on == 6:
    print('LED ON')
    led.value(1)
    #a small delay in on and off mode of the switch
    time.sleep(.5)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

 #uncomment this section for just you want to call that function on top and then automatically close the connection after 3 sec the after waiting for connection from next device
  #while True:
  #try:
   # if gc.mem_free() < 102000:
      #gc.collect()
    #conn, addr = s.accept()
    #conn.settimeout(3.0)
    #print('Got a connection from %s' % str(addr))
    #request = conn.recv(1024)
    #conn.settimeout(None)
    #print('Content = %s' % str(request))
    #response = web_page()
    #conn.send('HTTP/1.1 200 OK\n')
    #conn.send('Content-Type: text/html\n')
    #conn.send('Connection: close\n\n')
    #conn.sendall(response)
    #conn.close()
  #except OSError as e:
    #conn.close()
    #print('Connection closed')





