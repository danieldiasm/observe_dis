from rpi_lcd import LCD
import signal

lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    signal.signal(signal.SIGTERM, safe_exit)
    signal.signal(signal.SIGHUP, safe_exit)
    lcd.text("First Line", 1)
    lcd.text("Second Line", 2)
    print("Press Ctrl+C to exit!")
    input()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()