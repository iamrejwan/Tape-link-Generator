import requests
import re
import time


def generateDownloadTicket(VIDEO_ID: str):
    API_USER = "user_id"
    API_KEY = "user_key"

    token = requests.get(
        f'https://api.streamtape.com/file/dlticket?file={VIDEO_ID}&login={API_USER}&key={API_KEY}')

    if token.status_code == 200:

        return token.json()['result']['ticket']
    else:
        raise "Server Error. Try Again!"


def getDownlaodLink(url: str):
    filter = re.compile(r"https?://(www\.)?")
    url = filter.sub('', url).strip()
    VIDEO_ID = url.split("/")[2]

    token = generateDownloadTicket(VIDEO_ID)
    print("")
    print("Generating... Wait!")

    time.sleep(5)
    response = requests.get(
        f'https://api.streamtape.com/file/dl?file={VIDEO_ID}&ticket={token}')

    if response.status_code == 200:

        return response.json()['result']['url']
    else:
        raise "Server Error. Faild to generate downlaod link. Tray Again!"


def main():
    url = input("Enter Stream URL: ")
    dounload_link = getDownlaodLink(url)
    print("")
    print("")
    print("Your Downlaod Link: ", dounload_link)
    print("")
    print("")


if __name__ == '__main__':
    main()
