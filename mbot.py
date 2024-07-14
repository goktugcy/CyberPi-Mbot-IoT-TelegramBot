import network
import time
import usocket as socket
import json
import cyberpi
import mbuild

# Set the brightness of all LEDs to maximum (values range from 0 to 100)
cyberpi.ultrasonic2.led_show([10, 10, 10, 10, 10, 10, 10, 10])

# Wi-Fi and API info
ssid = "Airties_Airxxxxxx"
password = "xxxxxx"
cyberpi._cloud_tts.TTS_URL = "http://msapi.mblock.cc/baidu/voice/text2audio"
cyberpi.cloud.setkey = "3bc4b741c2854446bcxxxxxxxxxx"
webhook_url = "http://webhook.adress"

def send_post_request(url, data):
    try:
        _, _, host, path = url.split('/', 3)
        addr = socket.getaddrinfo(host, 80)[0][-1]
        s = socket.socket()
        s.connect(addr)

        # Build HTTP request
        request = 'POST /{} HTTP/1.1\r\nHost: {}\r\nContent-Type: application/json\r\nContent-Length: {}\r\n\r\n{}'.format(
            path, host, len(data), data)
        
        s.send(bytes(request, 'utf8'))
        
        response = s.recv(1024)
        cyberpi.console.println("Response received: " + response.decode('utf8'))
        
        s.close()
    except Exception as e:
        cyberpi.console.println("Bir hata oluştu: " + str(e))

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        cyberpi.console.println("Connecting to network...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    cyberpi.console.println("Connected to WiFi")

def check_sound(threshold=10):
    loudness = cyberpi.get_loudness()
    cyberpi.console.println("Current loudness: " + str(loudness))
    return loudness > threshold

def check_motion():
    distance1 = mbuild.ultrasonic2.get(1)  # Assuming the sensor is connected to port 1
    cyberpi.console.println("Initial distance: " + str(distance1))
    time.sleep(0.1)
    distance2 = mbuild.ultrasonic2.get(1)  # Measure again after a short delay
    cyberpi.console.println("Second distance: " + str(distance2))
    return abs(distance1 - distance2) > 5  # Threshold difference to detect motion

# Connect to WiFi
connect_to_wifi(ssid, password)

# Main loop
while True:
    if check_sound():
        cyberpi.console.println("Sound detected! Preparing to send message...")
        data = json.dumps({"message": "Bir ses algilandi!"})
        send_post_request(webhook_url, data)
        cyberpi.console.println("Message sent!")
        time.sleep(1)  # Prevent multiple rapid messages
  
    if check_motion():
        cyberpi.console.println("Motion detected! Preparing to send message...")
        data = json.dumps({"message": "Hareket algilandi!"})
        send_post_request(webhook_url, data)
        cyberpi.console.println("Message sent!")
        time.sleep(1)  # Prevent multiple rapid messages

    time.sleep(0.5)  # Short sleep to prevent busy-waiting
