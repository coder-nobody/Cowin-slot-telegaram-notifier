import time
from errors import loggingData

class logger():
    def info(key,message=""):
        logger.printData(f"[INFO] : {loggingData[key]} {message}")

    def error( key, message=""):
        logger.printData(f"[ERROR] : {loggingData[key]} {message}")

    def warning( key, message=""):
        logger.printData(f"[WARNING] : {loggingData[key]} {message}")

    def printData( message):
        Time,Date = getDateTime()
        print(f"[{Date} {Time}] " + message)

def getDateTime():
    TimeObj = time.localtime()
    return (time.strftime("%H:%M:%S", TimeObj), time.strftime("%d-%m-%Y", TimeObj))

