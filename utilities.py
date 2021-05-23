#function to process the data
def processData(session, age):
    message = f"Vaccine Availability for {age}+:\n"
    for center in session["centers"]:
        slot = ""
        vaccine = ""
        for day in center['sessions']:
            if day['available_capacity'] and day['min_age_limit'] == age:
                slot += f"{day['date']}: {day['available_capacity']}\n"
                vaccine = day['vaccine']

        if(len(slot)):
            msg = f"Center: {center['name']}\nSlots for {vaccine} :\n{slot}"
            message += msg + '\n'
    if message == f"Vaccine Availability for {age}+:\n":
        return ""
    else:
        return message


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

