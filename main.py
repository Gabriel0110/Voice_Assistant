import speech_recognition as sr
import win32com.client as wincl
import re
import pickle
import time

speak = None
reminders = {}

def findWholeWord(w):
    '''
        findWholeWord allows for easier recognition of certain commands, making
        it act just like Amazon's Alexa. If it hears a certain command, like
        "goodbye jarvis" in a sentence, it will execute command. With Alexa,
        if you say Alexa in a sentence while talking to someone, she activates.
        This could be more or less annoying, so it is just preference to user.
        It can be changed if desired, just don't use the function.
    '''
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def isWakePhrase(result):
    return str(findWholeWord('hey jarvis')(result.lower())) != "None"

def loadReminders():
    try:
        with open('saved_reminders.dat', 'rb') as file:
            reminders = pickle.load(file)
    except:
        print("No reminder list found! Returning empty list.")
        reminders = {}
    return reminders

def saveReminderList(reminders):
    with open('saved_reminders.dat', 'wb') as file:
        pickle.dump(reminders, file)

def refreshKeys(reminders):
    i = 0
    for key, value in reminders.items():
        key = i
        i += 1

def getSpeech():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            result = r.recognize_google(audio)

            if str(findWholeWord('stop')(result.lower())) != "None":
                return "stop"
            else:
                return str(result)
        except sr.UnknownValueError as e:
            print(f"Google Speech Recognition could not understand audio: {e}")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

def listening():
    global speak, reminders
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            
        # COMMAND OPTIONS
        try:
            result = r.recognize_google(audio)
            
            if str(findWholeWord('goodbye')(result.lower())) != "None": # exit command-entry loop
                speak.SpeaK("Goodbye!")
                return
            elif str(findWholeWord('exit')(result.lower())) != "None": # close the program completely
                speak.Speak("Closing program.")
                exit()
            elif str(findWholeWord('new reminder')(result.lower())) != "None": # add a new reminder to reminders list
                speak.Speak("Okay. What is the reminder?")
                reminder = getSpeech()
                if len(reminder) == 0:
                    print("Reminder length == 0. Returning.")
                    return
                elif reminder == "stop":
                    print("'Stop' returned. Stopping...")
                    return
                else:
                    speak.Speak(f"You said, {reminder}. Do you want to add this reminder?")
                    ans = getSpeech()
                    if ans.lower() == "yes":
                        i = 0
                        while True:
                            if i not in reminders.keys():
                                reminders[i] = reminder
                                break
                            else:
                                i += 1
                        speak.Speak("Reminder has been added to the list.")
                        refreshKeys(reminders)
                        saveReminderList(reminders)
                    elif ans.lower() == "no":
                        speak.Speak("Reminder was not added to the list.")
                    else:
                        speak.Speak("Please respond either yes or no. This reminder was not added to the list.")
                return
            elif str(findWholeWord('my reminders')(result.lower())) != "None": # see what reminders are in the list
                if len(reminders) == 0:
                    speak.Speak("You have zero reminders.")
                else:
                    speak.Speak("Here are your reminders.")
                    time.sleep(0.5)
                    for key, value in reminders.items():
                        speak.speak(f"{key+1}, {value}")
                        print(f"{key+1}: {value}")
                        time.sleep(1)
                return
            else:
                speak.Speak("I do not recognize that command. Please try again.")
                print(f"Google Speech Recognition thinks you said: {result}")
        except sr.UnknownValueError as e:
            print(f"Google Speech Recognition could not understand audio: {e}")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

def main():
    global speak, reminders

    # Go ahead and load any reminders
    reminders = loadReminders()

    # create TTS (text-to-speech) voice
    speak = wincl.Dispatch("SAPI.SpVoice")
    
    # recognize speech using Google Speech Recognition
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            print("Listening for wake phrase...\n")
            result = r.recognize_google(audio)

            if isWakePhrase(result):
                speak.Speak("How can I help you?") # just to know it activates -- can remove
                print("WAKE PHRASE DETECTED -- LISTENING...\n")
                listening()
            else:
                pass
        except sr.UnknownValueError as e:
            print(f"Google Speech Recognition could not understand audio: {e}")

if __name__ == "__main__":
    main()