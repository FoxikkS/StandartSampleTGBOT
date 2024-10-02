from configparser import ConfigParser

class Config:
    SELECT = "DEFAULT"

    config = ConfigParser()
    config.read("data/config.ini")

    token = config.get(SELECT, 'TOKEN')