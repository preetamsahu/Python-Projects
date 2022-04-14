import win32com.client
speakr=win32com.client.Dispatch("SAPI.SpVoice")
speakr.Speak("Hello, My name is Preetam sahu")

exit()
#or 
from win32com.client import Dispatch

def speak(str):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

speak("My name is Preetam Sahu")
