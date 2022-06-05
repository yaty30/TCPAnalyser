from fileinput import filename
import threading
import csv
import re
import time
import socket
import string
import base64
import random
from datetime import datetime


count = 0


def counter():
    return count


def addCount():
    global count
    count = count + 1
    return count


def alterCSV(targetFile, header, data):
    f = open("path/to/csv_file", "w")

    with open(targetFile, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerow(data)

    return "done"


def stringGenerator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def getDateAndTime(type):
    now = datetime.now()

    if type.lower() == "date":
        return str(now.date())
    else:
        return str(now.time())


def getHostIPaddress():
    return socket.gethostbyname(socket.gethostname())


def encodeBase64(file):
    return base64.b64encode(open(file, "rb").read())


def storeData(path, body):
    ogContent = ""
    lineCount = 0

    with open(path) as logCount:
        count = sum(1 for _ in logCount)
        lineCount = count

    og = open(path, "r")
    ogContent = og.read()
    og.close()

    f = open(path, "w")

    f.write(ogContent + f",\n{body}" if lineCount > 0 else body)

    f.close()

    return body


def createLogFile(path, file_name, body):
    full_path = path + "/" + file_name
    file = open(full_path, "a")
    file.write(body)
    file.close()

    return f"log created at path -> {full_path}."


def asString(string, colon):
    result = ""

    if colon == "double":
        result = '"' + str(string) + '"'
    else:
        result = "'" + str(string) + "'"

    return result


def patch_say(x):
    return "__defv__/" + x + ".wav"


def storeHistory(data):
    result = open("stored_points.json", "w")
    result.write(data)
    result.close()

    openResult = open("stored_points.json", "r")
    return openResult.read()
