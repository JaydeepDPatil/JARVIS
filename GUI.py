#import all the files 
import wx
import wikipedia
from Speak import *
from NewsArticle import *
from FacebookLogin import *
from ToDolist import *
from LockingTheScreen import *
from CurrentTime import *
from Dictionary import *
from Music import *
from SearchingOnTheGoogle import *

#Important --> while downloading wx download wxPython instead of wx
#pip install -U wxPython
#or https://pypi.python.org/pypi/wxPython
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="JARVIS")
        panel = wx.Panel(self)

        ico = wx.Icon('boy.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Hello Sir. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,
                               size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        speak.Speak('''Welcome back Sir, Jarvis at your service.''')

    def OnEnter(self, event):
        put = self.txt.GetValue()
        put = put.lower()
        link = put.split()
		#if you hit enter without texting Microphone will be activated
        if put == '':
            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            try:
                put = r.recognize_google(audio)
                put = put.lower()
                link = put.split()
                self.txt.SetValue(put)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}"
                      .format(e))
            except:
                print("Unknown exception occurred!")
		#doing google search for your query
        elif put.startswith('open')or put.startswith('search') or put.startswith('google'):
            try:
                speak.Speak('Opening')
                url = "https://www.google.com.tr/search?q={}".format(link[1])
                webbrowser.open(url)
            except Exception as e:
                print(str(e))
		#reading live news
        elif put.startswith('news'):
            to_bespoken = "Sport News..............Times Of India ..........Science News...............CNN News............Google India News"
            speak.Speak(to_bespoken)
            print('Sport news\nTimes Of India\nScience News\nCNN News\nGoogle India News')
            speak.Speak('Which is your choice')
            time.sleep(3)
            usercommand = get_voice_as_input().lower()
            print(usercommand)
            if "times of india" in usercommand:
                info=times_of_india()
            elif "sport news" in usercommand:
                info=talk_sport()
            elif "science news" in usercommand:
                info=new_scientist()
            elif "cnn news" in usercommand:
                info=cnn()
            elif "google" in usercommand:
                info=google_india_news()
            print(info)
		#facebook login
        elif put.startswith('login fb') or put.startswith('open fb') or put.startswith('fb login') or put.startswith('log into fb') or put.startswith('facebook login'):
            speak.Speak('opening the facebook please wait')
			open_the_fb()
		#facebook logout
        elif put.startswith('logout from fb') or put.startswith('fb logout'):
            close_fb()
			speak.Speak('sucessfully logged out')
		#your task to perform list
        elif put.startswith('my to do list'):
			speak.Speak('here is your to do list')
            to_do_list()
		#locking the desktop screen
        elif put.startswith('shut down') or put.startswith('lock') or put.startswith('screen lock'):
			speak.Speak('Locking your desktop Screen')
			time.sleep(2)
            log_the_screen()
		#knowing the current date and time
        elif put.startswith('current time')or put.startswith('todays date') or put.startswith('time'):
            speak.Speak( 'Current Data and time is'+curr_time())
		#vocabulary
        elif put.startswith('meaning of') or put.startswith('synonyms of') or put.startswith('antonyms of'):
            dictionary_search(str(link[2]))
		#to play song in your system
        elif put.startswith('show me the song list') or put.startswith('play music')or put.startswith('music'):
			speak.Speak('Playing your favourite music')
            music_mood()
		#doing wikipedia search
        else:
                put = put.split()
                put = ' '.join(put[2:])
                print(wikipedia.summary(put))
                speak.Speak('Searched wikipedia for ' + put)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
