'''

  pip install PyP100
  pip install python-dotenv


  wifi 2G

'''
from PyP100 import PyP100
from dotenv import dotenv_values
from bottle import Bottle, request, response, run
import json

config = dotenv_values(".env")
print(config)

p100 = PyP100.P100(config["IP"], config["USER_EMAIL"], config["USER_PWD"])

p100.handshake() #Creates the cookies required for further methods
p100.login() #Sends credentials to the plug and creates AES Key and IV for further methods

app = Bottle()

@app.route('/p100/info', method='GET')
def p100_info():
    a = p100.getDeviceInfo()
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(a)


@app.route('/p100/name', method='GET')
def p100_name():
    a = p100.getDeviceName()
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(a)


@app.route('/p100/on', method='GET')
def p100_on():
    a = p100.turnOn()
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(a)


@app.route('/p100/off', method='GET')
def p100_off():
    a = p100.turnOff()
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(a)

@app.route('/p100/toggle', method='GET')
def p100_toggle_status():
    a = p100.toggleState()
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(a)

'''
p100.turnOn() #Turns the connected plug on
p100.turnOff() #Turns the connected plug off
p100.toggleState() #Toggles the state of the connected plug

p100.turnOnWithDelay(10) #Turns the connected plug on after 10 seconds
p100.turnOffWithDelay(10) #Turns the connected plug off after 10 seconds

p100.getDeviceInfo() #Returns dict with all the device info of the connected plug
p100.getDeviceName() #Returns the name of the connected plug set in the app
'''
a = p100.getDeviceInfo() #Returns dict with all the device info of the connected plug
print(a)
b = p100.getDeviceName() #Returns the name of the connected plug set in the app
print(b)
p100.toggleState() #Toggles the state of the connected plug

'''
{'error_code': 0, 'result': {'device_id': '8022ECFB2D9BFE1FDB0DAD680183DB9C1F50DEE4', 'fw_ver': '1.4.9 Build 20210621 Rel. 30941', 'hw_ver': '1.20.0', 'type': 'SMART.TAPOPLUG', 'model': 'P100', 'mac': 'B4-B0-24-32-4C-D4', 'hw_id': '9994A0A7D5B29645B8150C392284029D', 'fw_id': '1D18AD293A25ABDE41405B20C6F98816', 'oem_id': 'D7C5ADFD37188938BA82FD0FE208D1E7', 'specs': 'EU', 'device_on': True, 'on_time': 691, 'overheated': False, 'nickname': 'aG9tZTAx', 'location': '', 'avatar': 'fan', 'longitude': 1268787, 'latitude': 374831, 'has_set_location_info': True, 'ip': '172.30.1.33', 'ssid': 'S1RfR2lHQV8yR18wNEQw', 'signal_level': 3, 'rssi': -38, 'region': 'Asia/Seoul', 'time_diff': 540, 'lang': 'ko_KR', 'default_states': {'type': 'last_states', 'state': {}}}}
home01
'''
if __name__ == '__main__':
  run(app, host=config["API_HOST"], port=int(config["API_PORT"]))
