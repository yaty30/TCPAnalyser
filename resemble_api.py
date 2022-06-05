from resemble import Resemble
from resembleAI import ResembleAI

Resemble.api_key('AndQQwZr3QrIsCGc30dJUgtt')
project_uuid = '4e9a04d1'

page = 1
page_size = 10

voice_id = {
    "uuid": "a7229976",
    "name": "SGD",
    "status": "finished",
    "created_at": "2022-02-19T12:53:25.053Z",
    "updated_at": "2022-02-19T14:12:54.016Z"
}

# data structure:
# data = {
#     "project_uuid": project_uuid,
#     "voice_uuid": voice_id["uuid"],
#     "body": "Hello World"
# }


class Resemble:
    def get_all_voices():
        response = Resemble.v2.voices.all(page, page_size)
        voices = response['items']

        return voices


    def get_specific_voice(uuid):
        voice_uuid = uuid

        response = Resemble.v2.voices.get(voice_uuid)
        voice = response['item']

        return voice


    def create_voice(data):
        response = ResembleAI.voices.create(data)
        voice = response

        return voice


    def build_voice(uuid):
        response = ResembleAI.voices.build(uuid)
        return response


    def get_all_recordings(uuid):
        response = Resemble.v2.recordings.all(uuid, page, page_size)
        recordings = response['items']

        return recordings


    def get_recording(data):
        voice_uuid = data["voice_uuid"]
        recording_uuid = data["recording_uuid"]

        response = Resemble.v2.recordings.get(voice_uuid, recording_uuid)
        recording = response['item']

        return recording


    def create_recording(data):
        voice_uuid = data["uuid"]
        name = data["name"]
        text = data["text"]
        is_active = True
        # it requires membership to ulock other emotion
        emotion = "neutral"

        with open(data["path"], 'rb') as file:
            response = Resemble.v2.recordings.create(
                voice_uuid, file, name, text, is_active, emotion)
            recording = response['item']

        return recording


    def delete_recording(voice_uuid, recording_uuid):
        response = Resemble.v2.recordings.delete(voice_uuid, recording_uuid)

        return response


    def create_clip(data):
        project_uuid = data["project_uuid"]
        voice_uuid = data["voice_uuid"]
        body = data["body"]

        response = Resemble.v2.clips.create_sync(
            project_uuid,
            voice_uuid,
            body,
            title=None,
            sample_rate=None,
            output_format=None,
            precision=None,
            include_timestamps=None,
            is_public=None,
            is_archived=None,
            raw=None
        )

        clip = response['item']

        return clip


    def get_all_clips(data):
        project_uuid = data["project_uuid"]
        response = Resemble.v2.clips.all(project_uuid, page, page_size)
        clips = response['items']

        return clips
