import configparser

config = configparser.RawConfigParser()
filepath = "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#14 & 15\\OrangeHRM\\Configuration\\config.ini"
config.read(filepath)


class Readconfig:
    @staticmethod
    def getusername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password
