import pitch
import sounddevice as recorder
from scipy.io.wavfile import write
from playsound import playsound
from utils import encodeBase64, getDateAndTime, stringGenerator, storeData, asString, createLogFile


audioName = "sound_sample.wav"


def audioAnalyse():
    p = pitch.find_pitch(audioName)
    print('pitch =', p)


def voiceRecord():
    rate = 44100
    duration = 5

    targetAudio = recorder.rec(
        int(duration * rate),
        samplerate=rate,
        channels=2
    )

    recorder.wait()

    write(audioName, rate, targetAudio)
    encodedAudioString = encodeBase64(audioName)

    # audioAnalyse()

    log = "[ Date: " + getDateAndTime("date") \
        + ", Time: " + getDateAndTime("time") \
        + ", ID: " + stringGenerator(9) \
        + ", EncodedAudioString: " + asString(encodedAudioString, "double") \
        + " ]"

    logTitle = "audio_analyse_" + getDateAndTime("date") + "_" + getDateAndTime("time") + ".log"

    return createLogFile("audio_analyse_logs", logTitle, log)
