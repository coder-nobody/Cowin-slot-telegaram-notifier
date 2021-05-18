#Add the pincode in the pincode field in user data
# in the user field enter telegram registered mobile number 
# or the telegram group invite link in which you wish to send the message
# or the username of the recipient
# you can add more dictionary in the userdata dictionary with key as area pincode
# and value as another dictionary similar 
# eg.
# userData={
#   '202001': {
#        'user': ['+91001122334455',+915566778899],
#         'session': "keep it as it is"
#   }
# }

userData={
    'pincode':{
        'user': ['telegram registered mobile number of message recipent'],
        'session':"keep it as it is"
    }
}
# userData = {}
# def addUsers():
#     pass

# def loadUsers():
#     pass

# def addCredentials():
#     pass
# def addData():
#     pass

# do not change below this line
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept": "text/html,application/xhtml xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}

baseURL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="


#change the value of singleUserTime to increase or decrease the time interval between two api calls in seconds
# do not set it below 3 seconds or it will result in your ip blockage
singleUserTime = 30
sleepTime = max(3, singleUserTime/len(userData))
