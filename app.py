from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from tts_core import TTS, setSpeechRate, DefaultTTS, getVoices
from utils import storeData, getDateAndTime, stringGenerator, getHostIPaddress, asString
import json
import datetime
import random
from resemble_api import Resemble

app = Flask(__name__)
CORS(app)


@app.route("/postWord", methods=["POST"])
def PostWord():
    datas = request.json
    data = datas[0]

    # get word
    targetWord = str(data["word"])
    # get voice
    voice = data["currentVoice"]

    if voice == "0":
        DefaultTTS(data)
    else:
        TTS(targetWord)

    space = "    "

    # save log
    log = "[\n" + space + "Date: " + asString(getDateAndTime("date"), "double") \
        + ", \n" + space + "Time: " + asString(getDateAndTime("time"), "double") \
        + ", \n" + space + "IPAddress: " + getHostIPaddress() \
        + ", \n" + space + "ID: " + asString(stringGenerator(9), "double") \
        + ", \n" + space + "ServerHost: " + asString(request.host, "double") \
        + ", \n" + space + "RequestedAPI: " + asString(request.path, "double") \
        + ", \n" + space + "RequestMethod: " + asString(request.method, "double") \
        + ", \n" + space + "Origin: " + asString(request.origin, "double") \
        + ", \n" + space + "TargetMessage: " + asString(targetWord, "double") \
        + ", \n" + space + "Voice: " + asString(voice, "double") \
        + "\n]"

    resp = jsonify(success=True)
    StoreHistory(targetWord)

    return str(resp.status_code) + ": " + storeData("api_request.log", log)


def StoreHistory(word):
    now = datetime.datetime.now()
    hr = ""
    min = ""
    if len(str(now.minute)) == 1:
        min = "0" + str(now.minute)
    else:
        min = str(now.minute)

    if len(str(now.hour)) == 1:
        hr = "0" + str(now.hour)
    else:
        hr = str(now.hour)

    historyData = '{' \
        + '"message": ' + '"' + word + '"' \
        + ', "date": ' + asString(getDateAndTime("date"), "double") \
        + ', "time": ' + '"' + str(hr) + ":" + str(min) + '"' \
        + '},'
    sh = open("history.log", "a")

    sh.write(historyData)
    sh.close()


@app.route("/getHistory", methods=["GET"])
def GetHistory():
    phf = open("history.log", "r")

    return "["+phf.read()[:-1]+"]"


@app.route("/logging", methods=["GET"])
def Logging():
    log = "[ Date: " + getDateAndTime("date") \
        + ", Time: " + getDateAndTime("time") \
        + ", IPAddress: " + getHostIPaddress() \
        + ", ID: " + stringGenerator(9) + " ]"

    return storeData("record.log", log)


@app.route("/getVoices", methods=["GET"])
def GetVoices():
    return json.dumps(getVoices(), indent=4)


@app.route("/calibrationData", methods=["POST"])
def CalibrationData():
    data = request.json
    print(data)

    open("stored_points.json", 'w').close()

    return storeData("stored_points.json", str(data))


@app.route("/getCalibrationData", methods=["GET"])
def GetCalibrationData():
    data = open("stored_points.json", "r")

    return str(data.read())


@app.route("/getTTSVoices")
def GetTTSVoices():
    file = open("voices.log", "r")

    return json.dumps("["+file.read()+"]")


@app.route("/createNewVoice", methods=["POST"])
def CreateNewVoice():
    data = request.json["body"]
    id = str(random.randint(3, 50))

    Resemble.build_voice(id)
    Resemble.create_voice({
        "id": id,
        "file": data["files"]
    })

    log = ', {' + ' "name" :' '"' + \
        data["name"] + '", "id" :' + '"' + \
        id + '", ' + '"available": false }'
    f = open("voices.log", "a")

    f.write(log)
    f.close()

    file = open("voices.log", "r")

    return "["+file.read()+"]"


if __name__ == "__main__":
    app.run()
