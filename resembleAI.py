import requests

host = "https://628caf353df57e983ed3fee2.mockapi.io/ResembleAI/API/"


class ResembleAI:
    class voices:
        def build(uuid):
            url = host + 'build_voice'
            data = {
                "id": uuid
            }

            requests.post(url, data=data)

            return "done"


        def create(data):
            url = host + 'create_voice'
            data = {
                "id": data["id"],
                "samples": data["file"]
            }

            requests.post(url, data=data)

            return "done"
