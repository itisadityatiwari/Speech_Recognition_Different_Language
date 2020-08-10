import speech_recognition as sr
import time
#from playsound import playsound

def musical():
    r = sr.Recognizer()
    with sr.Microphone() as sound:
            try:
                print("Sing a song:")
                audio = r.listen(sound)
                text = r.recognize_google(audio)
                time.sleep(5)
                print("You Sang:{}".format(text))
            except:
                print("You can't sing")

def gana():
    r = sr.Recognizer()
    with sr.Microphone() as sound:
            try:
                print("Sing a song:")
                audio = r.listen(sound)
                time.sleep(5)
                text = r.recognize_google(audio,language="hin")
                print("You Sang:{}".format(text))
            except:
                print("You can't sing")

def ag():
    r = sr.Recognizer()
    with sr.Microphone() as sound:
            try:
                print("Bol Kahi tari:")
                audio = r.listen(sound)
                time.sleep(5)
                text = r.recognize_google(audio, language='mr')
                print("Mi Kai manto:{}".format(text))
            except:
                print("Tula nahi jamnare")

def su():
    r = sr.Recognizer()
    with sr.Microphone() as sound:
            try:
                print("Su bole che:")
                audio = r.listen(sound)
                time.sleep(5)
                text = r.recognize_google(audio, language='gu')
                print("Tamme bole:{}".format(text))
            except:
                print("Tamme nahi bole")



ln= int(input("Please select a language 1 for EngLish, 2 for hindi, 3 for marathi, 4 for gujurati:"))
if ln==1:
    print("you selected english")
    musical()
elif ln==2:
    print("Aapne hindi chuna")
    gana()
elif ln==3:
    print("Apan marathi nivadle")
    ag()
elif ln==4:
    print("Tamme guju mein bolo")
    su()
else:
    print("Invalid option")
    exit()