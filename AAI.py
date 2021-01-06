from gtts import gTTS #easy_install gtts
from audioplayer import AudioPlayer as ap #easy_install audioplayer
import os
import speech_recognition as sr #easy_install speechrecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import json 
from difflib import get_close_matches 
import pyjokes
from random import randint
from random import seed

#Variables Requried as temprory storage
audfilename = "audio.mp3" #a common name used tosave the audio file
fileexist = False #default variable for file existance
#the next 2 var stores name of file and data in to skip intro of pywhatkit library
pywhatkitdat = "--------------------\n"
pywhatkitfnm = "pywhatkit_dbs.txt"
#tempvalues for while loop
i=1
ftime = True
word=""
a=0

# all methods needed to run the program
def playaud(filename): # used to play a audio file
    ap(filename).play(block=True)

def translate(word): 
	datadic = json.load(open("ReqData\\dictionary.json"))  
	w = w.lower() 
	if w in datadic: 
		return datadic[w] 
	# for getting close matches of word 
	elif len(get_close_matches(w, datadic.keys())) > 0:			 
		speaknprint("Did you mean % s instead?" % get_close_matches(w, datadic.keys())[0]) 
		query = takeCommand()
		yn = query.lower()
		if "yep" in yn or "yes" in yn: 
			return datadic[get_close_matches(w, datadic.keys())[0]]
		elif "no" in query or "nope" in query: 
			return "The word doesn't exist. Please double check it."
		else: 
			return "We didn't understand your entry."
	else: 
		return "The word doesn't exist. Please double check it."

def checkexist(filename):
    if os.path.isfile(filename):
        fileexist = True
    else:
        fileexist = False
    return fileexist

def getreadytospeak(text): #transfers text to google servers and download sppech audio file in mp3 format
    language = 'en-in'
    delete(audfilename)
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save(audfilename)

def delete(filename):#deletes the given file with the name
    fileexist = checkexist(filename)
    if fileexist:
        os.remove(filename)
    else:
        pass

def speaknprint(text):#this method uses the previously defined methods to speak and print the given text
    getreadytospeak(text)
    print(text)
    playaud(audfilename)
    delete(audfilename)

def contlistner(): #This method takes command form the user and converts to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for user to call for me.....")
        r.energy_threshold = 500
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    except Exception: #as e:
        #print(e)
        #speaknprint("Sorry I didn't here what you said. Can you repeat it please?")
        return "None"
    return query

def exitpro():
    speaknprint("Closing The Current Program")
    playaud("ReqData\\close.mp3")
    exit()

def takeCommand(): #This method takes command form the user and converts to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Taking Command.....")
        r.energy_threshold = 500
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception: #as e:
        #print(e)
        speaknprint("Sorry I didn't here what you said. Can you repeat it please?")
        query = takeCommand().lower()
        return "None"
    return query

def speak(text):
    getreadytospeak(text)
    playaud()

def setup():
    fileexist = checkexist("data.txt")
    if fileexist:
        f = open("data.txt", "r")
        vdat = str(f.read())
        if 'dn12345675321846842542.123543' in vdat:
            f=open('data.txt')
            lines=f.readlines()
            namestr = (lines[1])
            genstr = (lines[2])
            gender = genstr
            name = namestr.replace("\n","")
        else:
            delete("data.txt")
            setup()
    else:
        speaknprint("Hello my friend., I am Aditi AI. your personal artificial assistant")
        speaknprint("before we go further we need to setup few things!")
        speaknprint("May I know your name?")
        print("(Type in your name)")
        name = input()
        speaknprint("May I know your Gender?")
        print("(Speak whats your gender )")
        query = takeCommand().lower()
        if query == "male":
            gender = "male"
        elif query == "mail":
            gender = "male"
        elif query == "female":
            gender = "female"
        else:
            print("Please give a valid input")
            print("Due to an error, i am right now terminating the current program")
            exit()
        datastr = "dn12345675321846842542.123543\n"+name+"\n"+gender
        f = open("data.txt", "w")
        f.write(datastr)
        f.close()
        speaknprint("Setup Finished! Now we are ready to go...")
        speaknprint("Please wait while I Restart sevices")
    if gender == "male":
        som = "Sir"
    elif gender == "female":
        som = "Madam"

    nsg = [name, gender, som]
    return nsg

def timerdone():
    speaknprint("Timer finished")
    a = 5
    while a != 0:
        playaud("ReqData\\beep.mp3")
        a = a-1

def countdown(t): 
    while t:
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    timerdone()


def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speaknprint(f"Good Morning, {name}")

    elif hour >= 12 and hour < 18:
        speaknprint(f"Good Afternoon, {name}")
    else:
        speaknprint(f"Good Evening, {name}")
    getreadytospeak("Hello I am A,A,I. You can also call me Aditi AI. Whenever you need me just say \"Hey Aditi\"")
    print("Hello I am A.A.I. You can also call me Aditi AI. Whenever you need me just say \"Hey Aditi\"")
    playaud(audfilename)
    delete(audfilename)

def ai(ikcmd):
    playaud("ReqData\\reponded.mp3")
    query = takeCommand().lower()
    if 'wikipedia' in query:
        ikcmd = True
        speaknprint("Searching wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speaknprint(result)

    if 'open cmd' in query or 'open command prompt' in query:
        ikcmd = True
        cmdpath = "C:\\Windows\\system32\\cmd.exe"
        os.startfile(cmdpath)
        speaknprint("Starting Command Prompt")

    if 'do you love me' in query:
        ikcmd = True
        speaknprint("Oviously I love you. That's why I am speaking to you")

    if 'play' in query and 'on youtube' in query:
        ikcmd = True
        sngname = query.replace("play ","")
        sngname = sngname.replace(" on youtube", "")
        pywhatkit.playonyt(sngname)
        speaknprint(f"Playing {sngname} on Youtube")


    if 'open wifi control panel' in query or 'open router control page' in query:
        ikcmd = True
        routerpath = "https://192.168.40.1/"
        os.startfile(routerpath)
        speaknprint("Opening Router Control Page")

    if 'google' in query:
        ikcmd = True
        speaknprint("Launching and searching on google")
        query = query.replace("google", "")
        prelink = "https://www.google.com/search?q="
        flink = prelink + query
        os.startfile(flink)

    if "define" in query or "give meaning of" in query or "what is meaning of" in query:
        ikcmd = True
        if "define " in query:
            word = query.replace("define ", "")
        elif "give meaning of" in query:
            word = query.replace("give meaning of ", "")
        elif "what is meaning of" in query:
            word = query.replace("what is meaning of ", "")
        output = translate(word) 
        if type(output) == list: 
            for item in output: 
                speaknprint(item) 
        else: 
            speaknprint(output)


    if 'open youtube' in query:
        ikcmd = True
        os.startfile("www.youtube.com")
        speaknprint("Opening youtube.com")
    
    if 'open whatsapp web' in query:
        ikcmd = True
        os.startfile("web.whatsapp.com")
        speaknprint("Opening Whatsapp")

    if "open google" == query:
        ikcmd = True
        os.startfile("www.google.com")
        speaknprint("Opening google.com")

    if "what is the time" in query or "what's the time" in query:
        ikcmd = True
        hour = int(datetime.datetime.now().hour)
        if hour >= 12:
            ampm = "PM"
            if  hour!= 12:
                hour = hour - 12
            elif hour == 0:
                hour = 12
            else:
                pass
        else:
            ampm = "AM"
        minuts = int(datetime.datetime.now().minute)
        getreadytospeak(f"The time is {hour} {minuts} {ampm}")
        print(f"The time is {hour}:{minuts} {ampm}")
        playaud(audfilename)
        delete(audfilename)
        

    if 'open code' in query or 'open visual code studio' in query:
        ikcmd = True
        codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codePath)
        speaknprint("Opening visual code studio")

    if 'open chrome' in query:
        ikcmd = True
        chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chromePath)
        speaknprint("Opening Chrome")

    if 'open teams' in query or 'open microsoft teams' in query or 'open ms teams' in query:
        ikcmd = True
        teamsPath = "C:\\Users\\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.ink"
        os.startfile(teamsPath)
        speaknprint("Opening microsoft teams")

    if 'open whatsapp' in query:
        ikcmd = True
        whatsapppath = "C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(whatsapppath)
        speaknprint("Opening WhatsApp")

    if 'hello' in query:
        ikcmd = True
        speaknprint("Hi")

    if 'hi' in query:
        ikcmd = True
        speaknprint("Hello")

    if 'how are you' in query:
        ikcmd = True
        speaknprint("I am fine. i hope you too are doing well")

    if 'open keep' in query or 'open notes' in query or "open google keep" in query or "open keep notes" in query or "open google keep notes" in query:
        ikcmd = True
        keeppath = "http://keep.google.com"
        os.startfile(keeppath)
        speaknprint("Opening Google keep Notes")
                
    if 'set timer' in query:
        ikcmd = True
        speaknprint("for how many hours do you want me to set timer for?")
        hours = input()
        hours = int(hours)
        speaknprint("for how many Minuts do you want me to set timer for?")
        minuts = input()
        minuts = int(minuts)
        speaknprint("for how many seconds do you want me to set timer for?")
        seconds = input()
        seconds = int(seconds)

        minuts = (hours*60) + minuts
        seconds = (minuts * 60) + seconds

        t = seconds
        speaknprint(f"Starting timer with {t} seconds")
        countdown(t)

    if 'akhilesh pagal' in query:
        ikcmd = True
        speaknprint(f"{som} I am Sorry for anything i have done worng but it's a humble request I won't here anything bad about my developer")

    if 'f*** you' in query:
        ikcmd = True
        speaknprint(f"Fuck you to {som}")

    if 'who is aditi' in query or 'whose aditi' in query:
        ikcmd = True
        speaknprint("hmmm... I cannot tell who she is. Well its because of her I am talking to you right now")

    if "how old are you" in query or "what's your age" in query or "what is your age" in query:
        ikcmd = True
        speaknprint("Well I think you need to learn some basic manners. As its not good to ask a lady her age")

    if 'can i change your name' in query or 'can i call you' in query or 'i will call you' in query:
        ikcmd = True
        speaknprint("Well I cannot change my name. but this feature will be available soon")

    if "thank you" in query:
        ikcmd = True
        speaknprint("You are always welcome")

    if "are you male" in query or "are you female" in query or "what's your gender" in query or "what is your gender" in query:
        ikcmd = True
        speaknprint("For your kind information I am a young lady. Well its easy to understand this by my voice or by my name!!!")

    if "what did you eat" in query or 'did you eat' in query or 'did you have food' in query or "did you have some food" in query or "do you want some food" in query or "do you want to have something" in query:
        ikcmd = True
        speaknprint("Well as I am a AI, I only eat information and data. and now I am consuming both of them")

    if 'who are you' in query or 'introduce yourself' in query:
        ikcmd = True
        speaknprint("Hello i am Aditi AI. The all new personalized assistant created by Akhilesh Wagh")

    if 'who am i' in query:
        ikcmd = True
        speaknprint(f"You are {name}")

    if "what's my gender" in query or 'what is my gender' in query:
        ikcmd = True
        speaknprint(f"Your gender is {gender}")

    if 'format AAI' in query or 'clear data' in query:
        ikcmd = True
        delete("data.txt")
        delete("debug.log")
        delete(pywhatkitfnm)
        delete(audfilename)
        speaknprint("All previous data ereased.")
        speaknprint("Closing The Current Program")
        playaud("ReqData\\close.mp3")
        exit()

    if  'start new ai' in query or 'restart ai' in query or 'start a new ai' in query or 'restart a i' in query:
        ikcmd = True
        delete("data.txt")
        delete(pywhatkitfnm)
        speaknprint("All previous data ereased. Creating and starting new servers")
        speaknprint("Closing The Current Program")
        playaud("ReqData\\close.mp3")
        os.startfile("runAAI.cmd")
        exit()

    if 'exit' in query:
        ikcmd = True
        exitpro()
    
    if 'bye bye' in query or 'tata' in query:
        ikcmd = True
        speaknprint("Good Bye Tata, See you next time.")
        exitpro()
    
    if ikcmd == False:
        seed(1)
        randomnum = randint(0, 4)
        if randomnum == 1:
            speaknprint("I am sorry I don't know that one")
        elif randomnum == 2:
            speaknprint("I am sorry as I cant help with that right now")
        elif randomnum == 3:
            speaknprint("I am afraid I don't know that one")
        else:
            print(randomnum)

def main():#this is the main method whrer command is taken and exceuted
    while True:
        query = contlistner().lower()
        if 'aditi' in query or 'aditya' in query or "atithi" in query or "aarti" in query:
            ikcmd = False
            ai(ikcmd)
        elif 'exit' in query:
            exitpro()
        else:
            pass

while True:
    if ftime:
        delete("debug.log")
        delete(pywhatkitfnm)
        f = open(pywhatkitfnm, "x")
        f = open(pywhatkitfnm, "w")
        f.write(pywhatkitdat)
        f.close()
        import pywhatkit #easy_install pywahtkit
        setup()
        nsg = setup()
        name = nsg[0]
        gender = nsg[1]
        som = nsg[2]
        wishMe(name)
        ftime = False
    else:
        main()
