# Network Display Package
# Library for CI/CD Event display on a 16X2 I2C on RPi
from config import Config


class NetDisplay:
    def __init__(self) -> None:

        self.config = Config()
    
    def init_display(self):
        self.config.load_config()
