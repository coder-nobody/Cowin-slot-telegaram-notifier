from user import *
from telethon import TelegramClient
import asyncio
import requests
import json
from LogData import logging, getDateTime

#function to send the telegram messages
async def sendMessage(data,message,district):   
    userData[district]['session'] = message
    print(message)
    for user in data['user']:
        try:   
            await client.send_message(user, message)
            logging.info('SlotSuccess', f"to {user} at: PINCODE {district}")
        except Exception as e:
            logging.error('SendFail', f"at PINCODE: {district}\n\nUSER: {user} \nEXCEPTION: {' , '.join(e.args)}")

#function to process the data
def processData( session, age ):
    message = ""
    for center in session["centers"]:
        slot = ""
        for day in center['sessions']:
            if day['available_capacity'] and day['min_age_limit'] == age:
                slot += f"{day['date']}: {day['available_capacity']}\n"
            
        if(len(slot)):
            msg = f"center:{center['name']}\nSlot:\n{slot}"
            message += msg + '\n'
    return message

#Telegram Authorization and login function
async def login():
    logging.info('acqCred')
    creds = open("credentials.json","r")
    account = json.load(creds)
    logging.info('credAcq')
    global client
    client = TelegramClient( account['Name'], account['Id'], account['Hash'] )
    logging.info('CliStrt')
    creds.close()
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
        t,date =getDateTime()
        for district,data in userData.items():
            url = f"{baseURL}{district}&date={date}"
            response = requests.get(url, headers=headers)
            msg = f"at PINCODE: {district}"

            #check if the request was processed successfully.
            if response.ok :
                session= response.json()               
                message = processData(session,18) #process the data and get relevant data

                #check if the message is not empty. else do not send any message on group
                if(len(message)):
                    #check if the message is same as that sent before to avoid repetition of multiple same messages
                    if data['session'] != message:
                        await sendMessage(data,message,district)
                    else:
                        logging.warning('SlotSame', msg)
                else:
                    logging.info('SlotFail', msg)
            else:
                logging.error('ApiFail', f"{msg} status code: {str(response.status_code)} REASON: {response.reason}")
            
            await asyncio.sleep(sleepTime)
             

asyncio.run(main())
