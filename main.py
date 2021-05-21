from DataManager import dataBase
from telethon import TelegramClient
import asyncio
import requests
from LogData import logging, getDateTime
from utilities import *

logging.info('default', 'Basic Startup complete!!')
userData = dataBase.getUserData()
#function to send the telegram messages
async def sendMessage(data,message):   
    data['session'] = message
    print(message)
    for user in data['user']:
        try:   
            await client.send_message(user, message)
            logging.info('SlotSuccess', f"to {user} {msg}")
        except Exception as e:
            logging.error('SendFail', f"{msg}\n\nUSER: {user} \nEXCEPTION: {' , '.join(e.args)}")

async def filterData(session, age, data):
    # process the data and get relevant data
    message = processData(session, age)
    #check if the message is not empty. else do not send any message on group
    if(len(message)):
        #check if the message is same as that sent before to avoid repetition of multiple same messages
        if data['session'] != message:
            await sendMessage(data, message)
        else:
            logging.warning('SlotSame', msg)
    else:
        logging.info('SlotFail', msg)

#Telegram Authorization and login function
async def login():
    account = dataBase.getTelegramCredentials()
    global client
    client = TelegramClient( account['Name'], account['Id'], account['Hash'] )
    logging.info('CliStrt')
    try:
        await client.start()
        logging.info('StartSuccess')
        return True
    except Exception as e:
        logging.error('StartFailed')
        return False
        
async def main():

    #try to login until successful
    while(not await login()):
        pass

    while(1):
        counter = 0
        userData = dataBase.getUserData()
        sleepTime = dataBase.getSleepTime()
        t,date =getDateTime()
        for district,data in userData.items():
            url = f"{baseURL}{district}&date={date}"
            response = requests.get(url, headers=headers)
            global msg
            msg = f"at PINCODE: {district}"

            #check if the request was processed successfully.
            if response.ok :
                session= response.json() 
                for age,value in data.items(): 
                    if len(value['user']):
                        await filterData(session,int(age),value)            
                
            else:
                logging.error('ApiFail', f"{msg} status code: {str(response.status_code)} REASON: {response.reason}")
            counter  += 1
            await asyncio.sleep(sleepTime)
            if(counter > 10):
                dataBase.loadData()
             

asyncio.run(main())
