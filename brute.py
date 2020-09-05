import requests
import json
import random
import string
import threading
## RANDOM LETTER STRING

userthreads = input("How much threads would you like to use: ")
def get_room_code(length):
    letters = string.ascii_uppercase
    
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

## GET REQUEST
def brute_jackbox():
    room = get_room_code(4)
    headers = {
            'host': 'ecast.jackboxgames.com',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Accept': '*/*',
            'Origin': 'https://jackbox.tv',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://jackbox.tv/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    url = "https://ecast.jackboxgames.com/api/v2/rooms/" + room

    response = requests.get(url, headers=headers)

    json_data = json.loads(response.text)

    if "appId" in response.text:
        print(">>>>>>>>>>>>>>>>>>>>>>>>> CODE: " + room + " WORKS! <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    brute_jackbox()

print("Script has started running at " + userthreads + " threads. Please wait and all valid codes will appear.")
userthreads = int(userthreads)

threads = []
for i in range(userthreads):
    t = threading.Thread(target=brute_jackbox)
    threads.append(t)
    t.start()
