# Cowin-Slot-Telegram-Notifier
This console app can ease up your vaccine hunt by sending Vaccine availability information on your Telegram app as soon as the vaccine is availabe in your pincode.

## Features
 * Search Vaccine in your area by Pincode.
 * Can fetch the information for multiple Pincodes.
 * Vaccine information is updated every 30 seconds per pincode.
 * Get the updated information on Telegram.
 * Information can be sent to any number of users and groups on Telegram.

## Installation
 * For windows clone or download this repo and run ```runscript.bat```
 * For other operating system install the dependencies in ```requirements.txt``` and run ```main.py``` from your console on python version >3.7

For installing the requirements.txt use this command:  
```pip install -r requirements.txt```

## Initial setup
Now to send messages using telegram you must have Telegram account and you should have your Telegram API Id and Api Hash

If you do not have that Don't worry, in the next section it is described how to get that.

Now on starting the app, follow the on screen instructions and Enter the Telegram API credentials.

After that add valid Recipient data. It consists of Pincode, Age group (18 of 45) and his telegram credentials.

Telegram recipient credentials can be:
* Recipient mobile number with country code eg.(+91xxxxxxxxxx)
* Recipient Telegram Username.
* A Telegram group invite link (<b>You must be a member of that group and have messaging rights</b>)

You can add more users also.
If you later wish to add users You can do so by running ```manageUsers.bat```

Alternatively you can also edit the entries in Database.json file.

After successfully completing these steps, your credentials will be validated and an OTP will be sent from telegram.
Enter the OTP and the setup is complete. :clap::clap:

After that it will never ask for OTP and you will start receiving vaccine messages on your registered recipient accounts.

## Getting Telegram API ID and HASH

In order to obtain an API id you need to do the following:

* If you do not have Telegram account then create one.
* Log in to your Telegram Account here: ```https://my.telegram.org.```
* Go to 'API development tools' and fill out the form
* You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.

You can also refer offficial documentation at https://core.telegram.org/api/obtaining_api_id

