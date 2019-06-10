import sys,os
import requests
import json

# hide the spark token
sys.path.append(os.path.join(os.path.dirname(__file__), "config"))
try:
    from spark_config import AUTH, ROOMID
except ModuleNotFoundError:
    from dummy_spark_config import AUTH, ROOMID

url = "https://api.ciscospark.com/v1/messages"

def post_message(message):

    if AUTH == "Bearer XXXX":
        print("No WebexTeams Token")
        return
    payload = {"roomId" : ROOMID,"text" : "ALERT: " + message}
    headers = {
    'authorization': AUTH,
    'content-type': "application/json"
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

