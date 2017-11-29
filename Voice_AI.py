import speech_recognition as sr
import win32com.client as wincl
import subprocess
import webbrowser
import time


def main():
	
	# create TTS (text-to-speech) voice
	speak = wincl.Dispatch("SAPI.SpVoice")

	prompt = input("To activate the AI, first press T and then enter.\n")

	if prompt == "T" or prompt == "t":
		time.sleep(1.5)
		voice_ai()
	else:
		time.sleep(2.5)
		print("That command is not recognized!")
		print("Exiting.")
		exit()
		
def voice_ai():
	print("Hello! What can I help you with?")
	
	# recognize speech using Google Speech Recognition
	while True:
		# obtain audio from the microphone
		r = sr.Recognizer()
		with sr.Microphone() as source:
			audio = r.listen(source)
		
		try:
			if r.recognize_google(audio) == "goodbye":
				speak.Speak("Goodbye!")
				exit()
			elif r.recognize_google(audio) == "open epic games":
				speak.Speak("Opening Epic Games Launcher")
				subprocess.call(['C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe'])
			elif r.recognize_google(audio).lower() == "open youtube":
				speak.Speak("Opening YouTube on your browser")
				webbrowser.open("https://www.youtube.com/")
			else:
				speak.Speak("I do not recognize that command")
				print("Google Speech Recognition thinks you said \"" + r.recognize_google(audio) + "\"")
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			
if __name__ == "__main__":
    main()		
