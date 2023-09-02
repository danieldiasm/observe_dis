import configparser


class Config:
    def __init__(self, configfile="config.ini") -> None:
        self.configfile = configfile
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.configfile)
        # Make an auto config generator
