# already available "only for windows" platform
# here i using male voice
# available voice you may find at https://support.microsoft.com/en-in/help/22797/windows-10-narrator-tts-voices
import win32com.client as wincl
speak=wincl.Dispatch("SAPI.SpVoice")
to_bespoken=""
speak.Speak(to_bespoken)

