import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import PySimpleGUI as ui

#functions-------------------------------------------------------------
def speak(text):
    tts = gTTS(text = text, lang="en")
    filename = "defaultfemale.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = " "

        try:
            said = r.recognize_google(audio)
            values['stt']= said
        except Exception as e:
            print ("Exception: " + str(e))
    return said


#window layout----------------------------------------------------------
layout = [
    [ui.Text("Type/paste desired speech here:"), ui.Multiline("Hello, welcome to Lazy Type, paste any text here for easy listening. ", enable_events = True, key = 'tts')],
    [ui.Button('Listen'), ui.Button('Cancel')],
    [ui.Text("Upload a PDF for conversion:"),ui.Input(),ui.FileBrowse()], 
    [ui.Button('Submit')]
    ]
layout2 = [
    [ui.Text("Speech to text conversion"), ui.Multiline(enable_events = True , key = ('stt'))],
    [ui.Button('Record', key = ('listenstt')), ui.Button('Cancel', key = ('cancelstt'))],
    [ui.T(" ")],
    [ui.T(" ")],
    [ui.T(" ")]
]
finalLayout=[[ui.Column(layout), ui.VSeperator(), ui.Column(layout2)]]

#initialize window and window content-------------------------------------
window = ui.Window('Lazy Type', finalLayout, resizable = True)

#event loop---------------------------------------------------------------
while True:
    event, values = window.read()
    if event == 'Listen':
        speak(values['tts'])
    if event == 'Record':
        convert()
    if event == ui.WIN_CLOSED or event == 'Cancel':## 'cancelstt':
        break
window.close()