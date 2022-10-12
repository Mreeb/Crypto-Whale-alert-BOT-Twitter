# Starting with the Name of Allah

import calendar  # includes operations related to Calendar
from datetime import datetime  # to work with date and time
import requests  # To send HTTP requests using Python.
import json  # To transfer data on the web and to store configuration settings.

now = datetime.utcnow()  # Construct a UTC DateTime
since = calendar.timegm(now.utctimetuple())  # To calculate Unix timestamp from GMT(Greenwich Mean Time).

apiKey = "jPgk7eCKyQ9IV1pW5BNUyuYKfDZ2F74E"
min_values = str(1000000)  # The Minimum Values
start_value = str(since - 60*10)  # fetches the datatime for the last transaction
url = 'https://api.whale-alert.io/v1/transactions?api_key='+apiKey+'&min_value='+min_values+'&start='+start_value

data = requests.get(url).json()  # returns a jason encoded content of a response
json_formatted_str = json.dumps(data, indent=2)  # Gives an Indent of two to the json file formate
print(json_formatted_str)