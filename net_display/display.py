from rpi_lcd import LCD

def print_and_clear(line1, line2, delay):
    lcd.text(line1, 1)
    lcd.text(line2, 2)
    time.sleep(delay)
    lcd.clear()

def print_only(line1, line2):
    lcd.clear()
    lcd.text(line1, 1)
    lcd.text(line2, 2)