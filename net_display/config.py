import configparser


class Config:
    def __init__(self, config_file="config.ini") -> None:
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config_item_list = {}

    def load_config(self):
        self.config.read(self.config_file)
        self.generate_item_objects()

    def generate_item_objects(self) -> None:
        for key in self.config.sections():
            self.config_item_list[key] = {}

            for j in self.config[key]:
                self.config_item_list[key][j] = self.config[key][j]

            self.config_item_list[key]["status"] = "unknown"

    def describe_items(self):
        for i, v in self.config_item_list.items():
            print(f"\033[1mSECTION: {i}\033[0m")
            print(v)
            print()
