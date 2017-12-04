import speech_recognition as sr
import win32com.client as wincl
import subprocess
import webbrowser
import time
import re
import twilio_texting


def main():
	voice_ai()

def findWholeWord(w):
	return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
	# findWholeWord allows for easier recognition of certain commands, making
	# it act just like Amazon's Alexa. If it hears a certain command, like
	# "goodbye jarvis" in a sentence, it will execute command. With Alexa,
	# if you say Alexa in a sentence while talking to someone, she activates.
	# This could be more or less annoying, so it is just preference to user.
	# It can be changed if desired, just don't use the function.
	
def googleSearch(query):
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	address = 'http://www.google.com/#q='
	search = address + query
	webbrowser.get(chrome_path).open(search)
		
def voice_ai():
	# create TTS (text-to-speech) voice
	speak = wincl.Dispatch("SAPI.SpVoice")
	
	# recognize speech using Google Speech Recognition
	while True:
		# obtain audio from the microphone
		r = sr.Recognizer()
		with sr.Microphone() as source:
			audio = r.listen(source)
		
		try:
			result = r.recognize_google(audio)
			
			if str(findWholeWord('hey jarvis')(result)) != "None" or str(findWholeWord('hey Jarvis')(result)) != "None":
				active = True
				speak.Speak("How can I help you?") # just to know it activates, can remove later
				
				while active:
					# obtain audio from the microphone
					r = sr.Recognizer()
					with sr.Microphone() as source:
						audio = r.listen(source)
					
					# COMMAND OPTIONS
					try:
						result = r.recognize_google(audio)
						
						""" 
							REPEATING active = False: to return back to main
							program loop after any command, requiring you to
							initialize Jarvis again by saying the init command.
						"""	
						
						if str(findWholeWord('goodbye jarvis')(result.lower())) != "None":
							speak.Speak("Goodbye!")
							active = False
						elif str(findWholeWord('open epic games')(result)) != "None":
							speak.Speak("Opening Epic Games Launcher")
							subprocess.call(['C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe'])
							active = False
						elif result.lower() == "open youtube": # open youtube on your browser
							speak.Speak("Opening YouTube on your browser")
							webbrowser.open("https://www.youtube.com/")
							active = False
						elif result.startswith("search"): # search for anything on Google
							speak.Speak("Searching for " + result[7:] + " on your browser")
							googleSearch(result[7:])
							active = False
						elif result.startswith("text my girlfriend"):
							speak.Speak("Texting your girlfriend " + result[19:])
							twilio_texting.sendText(result[19:])
						else:
							speak.Speak("I do not recognize that command, please try again.")
							print("Google Speech Recognition thinks you said \"" + result + "\"")
					except sr.UnknownValueError:
						print("Google Speech Recognition could not understand audio")
					except sr.RequestError as e:
						print("Could not request results from Google Speech Recognition service; {0}".format(e))
		except sr.UnknownValueError:
						print("Google Speech Recognition could not understand audio")
			
if __name__ == "__main__":
    main()		
