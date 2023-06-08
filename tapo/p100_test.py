'''

  pip install PyP100
  pip install python-dotenv

  wifi 2G

'''
from PyP100 import PyP100
from dotenv import dotenv_values
import json

config = dotenv_values(".env")
print(config)


def connect():
    success = False
    for n in range(1,250):
        try:
            ip = f'192.168.0.{n}'
            print(f'Try : {ip}')
            print("")
            p100 = PyP100.P100(ip, config["USER_EMAIL"], config["USER_PWD"])
            p100.handshake() #Creates the cookies required for further methods
            p100.login() #Sends credentials to the plug and creates AES Key and IV for further methods

            di = p100.getDeviceInfo()
            dn = p100.getDeviceName()
            print("-----------------")
            print(f'DeviceInfo : {di}')
            print(f'DeviceName : {dn}')
            break
        except Exception as err:
            print(err)
            continue


if __name__ == '__main__':
  connect()
