import requests
from time import time as timelib

class Program:
    def Main():
        time = round(timelib())
        startTime = time - 2 * 24 * 60 * 60
        endTime = time
        params = {
            "fromdate": startTime,
            "todate": endTime,
            "order": "desc",
            "sort": "creation",
            "tagged": "python",
            "site": "stackoverflow"
        }
        print(requests.get("https://api.stackexchange.com/2.3/questions", params=params).json())
        

if (__name__ == "__main__"):
    Program.Main()