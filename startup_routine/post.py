import netifaces
import smbus2
import os
import requests

def get_own_ip(interface):
    '''
    Returns provided interface IP Address, False if fails.
    '''
    try:
        return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
    except Exception as e:
        print(e) #TODO make this log
        return False

# Scan for I2C devices
def check_i2c():
    bus = smbus2.SMBus(1)
    for i in range(0, 128):
        try:
            bus.read_byte(i)
            print(f"I2C device found at address 0x{i:02x}") #TODO make this log
            return f"0x{i:02x}"
        except:
            pass

def check_server(HOSTADDR):
    resp = os.system("ping -c 1 " + HOSTADDR)
    if not resp:
        return "ONLINE"
    return "OFFLINE"

def check_jenkins(HOSTADDR):
    try:
        if requests.get(f'http://{HOSTADDR}:8080/login?from=%2F').status_code == 200:
            return "Running"
        return "Degraded"
    except requests.exceptions.InvalidSchema:
        return "Unavailable"

