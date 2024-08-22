import logging


class loger:
    @staticmethod
    def loggr():
        logIn = logging.getLogger()
        logpath = logging.FileHandler("C:\\Users\\pradi\\OneDrive\\Desktop\\python new file\\"
                                      "pythonProject1\\Logs\\logdata.log")
        logFormat = logging.Formatter("%(asctime)s,%(levelname)s,%(filename)s,%(funcName)s,%(name)s")
        logpath.setFormatter(logFormat)
        logIn.addHandler(logpath)
        logIn.setLevel(logging.INFO)
        return logIn

