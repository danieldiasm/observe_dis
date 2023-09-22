from rpi_lcd import LCD
from time import sleep


class Display:
    def __init__(self) -> None:
        self.lcd = LCD

    def print_and_clear(self, line1="", line2="", delay=2) -> None:
        self.lcd.text(line1, 1)
        self.lcd.text(line2, 2)
        sleep(delay)
        self.lcd.clear()

    def print(self, line1, line2) -> None:
        self.lcd.clear()
        self.lcd.text(line1, 1)
        self.lcd.text(line2, 2)

    def clear(self):
        self.lcd.clear()
