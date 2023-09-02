from rpi_lcd import LCD
import time

import post

# Instances
lcd = LCD()

# CONSTANTS
NETWORK_INTERFACE='wlan0'
IP_ADDR = "0.0.0.0"
SERVER_ADDR="0.0.0.0"
SRV_UP=""
JENKINS_UP=""


def print_and_clear(line1, line2, delay):
    lcd.text(line1, 1)
    lcd.text(line2, 2)
    time.sleep(delay)
    lcd.clear()

def print_only(line1, line2):
    lcd.clear()
    lcd.text(line1, 1)
    lcd.text(line2, 2)

def run_post():
    global IP_ADDR, SRV_UP, JENKINS_UP
    # Check Own IP
    IP_ADDR = post.get_own_ip(NETWORK_INTERFACE)
    print(IP_ADDR)

    # Check if LCD is present
    _ = post.check_i2c()

    # Check if Build Server is online
    SRV_UP = post.check_server(SERVER_ADDR)

    # Check if Jenkins Service is Available
    JENKINS_UP = post.check_jenkins(SERVER_ADDR)

lcd.backlight(True)
show_only("    P.O.S.T.    ", " Please Wait... ")
time.sleep(0.5)

run_post()
DISPLAY_TIME=2
show_and_clear(" Welcome ", " DevOps Display ", DISPLAY_TIME)
show_and_clear("IP Addr wlan0 ", f"{IP_ADDR} ", DISPLAY_TIME)
show_and_clear("Build Server", f"{SERVER_ADDR} ", DISPLAY_TIME)
show_and_clear("Build Server", f"{SRV_UP} ", DISPLAY_TIME)
show_and_clear("Jenkins Service", f"{JENKINS_UP} ", DISPLAY_TIME)
lcd.backlight(False)

