import speech_recognition as sr
import time
#return the spoken voice as string
def get_voice_as_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(1)
        print('speak now')
        audio=r.listen(source)
    try:
        audio_is=r.recognize_google(audio)
        return str(audio_is)
       # url = "https://www.google.com.tr/search?q={}".format(audio_is)
       # webbrowser.open(url)
    except:
        return 'Error in opening file!!'