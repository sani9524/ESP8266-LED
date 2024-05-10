import requests as req
import time

#VARIABLES
esp_url = "http://192.168.100.16:6006"
reddelay = 5
greendelay = 5
testdelay = 0

#LED ON DEFINE
def Led0_On():
    req.get(esp_url+"/0/on")
    print("0 ON")

def Led1_On():
    req.get(esp_url+"/1/on")
    print("1 OM")

def Led2_On():
    req.get(esp_url+"/2/on")
    print("2 ON")

def Led3_On():
    req.get(esp_url+"/3/on")
    print("3 ON")

def Led4_On():
    req.get(esp_url+"/4/on")
    print("4 ON")

def Led5_On():
    req.get(esp_url+"/5/on")
    print("5 ON")

def Led6_On():
    req.get(esp_url+"/6/on")
    print("6 ON")

#LED OFF DEFINE
def Led0_Off():
    req.get(esp_url+"/0/off")
    print("0 OFF")

def Led1_Off():
    req.get(esp_url+"/1/off")
    print("1 OFF")

def Led2_Off():
    req.get(esp_url+"/2/off")
    print("2 OFF")

def Led3_Off():
    req.get(esp_url+"/3/off")
    print("3 OFF")

def Led4_Off():
    req.get(esp_url+"/4/off")
    print("4 OFF")

def Led5_Off():
    req.get(esp_url+"/5/off")
    print("5 OFF")

def Led6_Off():
    req.get(esp_url+"/6/off")
    print("6 OFF")

#more defines
def Red_On():
    Led6_On()
    print("---RED-ON---")

def Red_Off():
    Led6_Off()
    print("---RED-OFF---")

def Yellow_On():
    Led5_On()
    print("---YELLOW-ON---")

def Yellow_Off():
    Led5_Off()
    print("---YELLOW-OFF---")

def Green_On():
    Led4_On()
    print("---GREEN-ON---")

def Green_Off():
    Led4_Off()
    print("---GREEN-OFF---")

#Functions
def test():
    Led0_On()
    Led0_Off()
    time.sleep(testdelay)
    Led1_On()
    Led1_Off()
    time.sleep(testdelay)
    Led2_On()
    Led2_Off()
    time.sleep(testdelay)
    Led3_On()
    Led3_Off()
    time.sleep(testdelay)
    Led4_On()
    Led4_Off()
    time.sleep(testdelay)
    Led5_On()
    Led5_Off()
    time.sleep(testdelay)
    Led6_On()
    Led6_Off()
    time.sleep(testdelay)

def test2():
    Led0_On()
    time.sleep(testdelay)
    Led1_On()
    time.sleep(testdelay)
    Led2_On()
    time.sleep(testdelay)
    Led3_On()
    time.sleep(testdelay)
    Led4_On()
    time.sleep(testdelay)
    Led5_On()
    time.sleep(testdelay)
    Led6_On()
    time.sleep(testdelay)
    Led0_Off()
    time.sleep(testdelay)
    Led1_Off()
    time.sleep(testdelay)
    Led2_Off()
    time.sleep(testdelay)
    Led3_Off()
    time.sleep(testdelay)
    Led4_Off()
    time.sleep(testdelay)
    Led5_Off()
    time.sleep(testdelay)
    Led6_Off()
    time.sleep(testdelay)


def streetlight():
    Yellow_On()
    time.sleep(3.5)
    Yellow_Off()
    Red_Off()
    Green_On()
    time.sleep(greendelay)
    Green_On()
    time.sleep(1)
    Green_Off()
    time.sleep(1)
    Green_On()
    time.sleep(1)
    Green_Off()
    time.sleep(1)
    Green_On()
    time.sleep(1)
    Green_Off()
    Yellow_On()
    time.sleep(3.5)
    Yellow_Off()
    Red_On()
    time.sleep(reddelay)
    Red_Off
    streetlight()


#CODE STARTS HERE
print("STARTED")
print("Esp IP:"+esp_url)
print("Running Tests to clear out LEDs")
time.sleep(2)
test()
test2()
print("TEST FINISHED")
streetlight()
print("FINISHED")
