import time
from errors import loggingData

class logData():
    def info(self,key,message=""):
        self.printData(f"[INFO] : {loggingData[key]} {message}")

    def error(self, key, message=""):
        self.printData(f"[ERROR] : {loggingData[key]} {message}")

    def warning(self, key, message=""):
        self.printData(f"[WARNING] : {loggingData[key]} {message}")

    def printData(self, message):
        Time,Date = getDateTime()
        print(f"[{Date} {Time}] " + message)

def getDateTime():
    TimeObj = time.localtime()
    return (time.strftime("%H:%M:%S", TimeObj), time.strftime("%d-%m-%Y", TimeObj))

logging = logData()
