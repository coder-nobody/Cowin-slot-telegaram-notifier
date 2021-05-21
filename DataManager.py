from time import sleep
from LogData import logging
import json

filename = "Database.json"
#Data base class to load and modify data
class DB():
    userData = {}
    telegramCredentials = {}
    singleUserTime = 30

    def __init__(self):
        logging.info("default","STARTING App...")
        self.loadData()
        if not DB.userData and not DB.telegramCredentials:
            self.firstRun()
        if not DB.userData:
            self.acquireUserData()
        if not DB.telegramCredentials:
            logging.error('default','No Telegram credentials found... Enter the Credentials...')
            DB.telegramCredentials = self.inputCreds()
        
        logging.info('default', 'Data Acquired successfully...')

        self.saveData()
    #function to save data.
    def saveData(self):
        success = False
        data = {
            'userData':DB.userData ,
            'telegramCredentials': DB.telegramCredentials,
            'singleUserTime':DB.singleUserTime,
        }
        while not success:
            try:
                logging.info('default', f'Attempting to save in {filename}')
                file = open(filename, "w")
                json.dump(data, file, indent=6)
                file.close()
                logging.info('default', f'{filename} saved successfully :)')
                success = True
            except:
                logging.error(
                    'default', f" Some error occured... Close {filename} if open .. Retrying again in 20 seconds...")
                sleep(20)
    #function to load data
    def loadData(self):
        try:
            logging.info('default', f'Loading data from {filename}...')
            ud = open(filename, "r")
            Data = json.load(ud)
            ud.close()
            DB.userData = Data.get('userData',{})
            DB.telegramCredentials = Data.get('telegramCredentials',{})
            DB.singleUserTime = Data.get('singleUserTime',30)
            logging.info('default', 'Data loaded successfully..')
        except:
            logging.warning('default', 'Error parsing the User data file New file is created.')
    #function to input telegram credentials
    def inputCreds(self):
        Name=""
        while Name == "":
            Name = input("\nEnter any name of your choice: ").strip()
            if not Name:
                logging.error('invalidData', 'Name cannot be empty..')
        id = ""
        while id =="":
            id = input("\nEnter Your Unique Telegram API Id: ").strip()
            try:
                id = int(id)
            except:
                logging.error('invalidData','Id should be numeric.')
                id = ""
        hash = ""
        while hash == "":
            hash = input("\nEnter Your Telegram API Hash: ").strip()
            if not Name:
                logging.error('invalidData', 'Telegram Hash cannot be empty..')
        print("\nThe details entered by you are:")
        print(f'Name: {Name}\nId:   {id}\nHash: {hash}\n')
        choice = input('\nDo you confirm your changes? (Y/N)')
        if choice == 'Y' or choice == 'y':
            return {
                'Name': Name,
                'Id': id,
                'Hash': hash
            }
        else:
            return self.inputCreds()
    #function to input user data
    def addData(self):
        failed = True
        while failed:
            pincode = input("Enter the Pincode of your area:").strip()
            if len(pincode) != 6:
                logging.error('invalidData', 'Pincode must be of length 6.')
                continue
            try:
                tmp = int(pincode)
            except:
                logging.error('invalidData', 'Pincode must be numeric.')
                continue
            failed = False
        failed = True
        while failed:
            age = input(
                "\nEnter the age group for which the vaccine is to be notified\nEnter  18 (for 18 - 44 Yrs) or 45 (for 45+) :").strip()
            if age not in ['18', '45']:
                logging.error(
                    'invalidData', 'Age must be entered either 18 (for 18 - 44 Yrs) or 45 (for 45+):')
                continue
            failed = False

        failed = True
        while failed:
            print("\nEnter the recipent info, it can be one of the following: ")
            telegramid = input("Username of telegram user  OR  Telegram registered mobile number, Add country code(eg. +91)  OR  Invite link of telegram Group (You must me member of that.) : ").strip()
            if(telegramid == ''):
                logging.error(
                    'invalidData', 'You must enter contact info to revieve notification on telegram.')
                continue
            failed = False

        print('You have entered this data:')
        print(f'Pincode:     {pincode}\nAge:         {age} \nTelegram id: {telegramid}')
        choice = input("Do Confirm your changes....(Y/N)").strip()
        if choice == 'Y' or choice == 'y':
            self.addUsers(pincode, age, telegramid)
        else:
            self.addData()
            return

    def addUsers(self,pincode, age, telegramid):
        if pincode not in DB.userData:
            DB.userData[pincode] = {
                '18': {
                    'user': [],
                    'session': ''
                },
                '45': {
                    'user': [],
                    'session': ''
                }
            }

        DB.userData[pincode][age]['user'].append(telegramid)
    #Function that runs when db is empty
    def firstRun(self):
        logging.info('default', 'Initialising First run...')
        sleep(1)
        self.acquireTelegramCredentials()
        self.acquireUserData()

    def acquireTelegramCredentials(self):
        logging.info('default', 'In the following Instructions enter your Telegram Credentials')
        DB.telegramCredentials = self.inputCreds()
        logging.info('default', 'Telegram Credentials Entered Successfully. Saving them....')
        self.saveData()
    
    def acquireUserData(self):
        if not DB.userData:
            logging.info('default', 'Setting up user data..')
            print('Now follow the onscreen instructions and Enter valid data..   :)  ')
            self.addData()
        ch = True
        while ch:
            choice = input("Do you want to add some more user data ..(Y/N)").strip()
            if choice == 'Y' or choice == 'y':
                self.addData()
            else:
                ch = False
        logging.info('default', 'Users Data Added successfully...')
        self.saveData()
    #getter for telegram credentials
    def getTelegramCredentials(self):
        return DB.telegramCredentials
    #getter for User Data
    def getUserData(self):
        return DB.userData

    def getSleepTime(self):
        return max(3, DB.singleUserTime/len(DB.userData))

dataBase = DB()
