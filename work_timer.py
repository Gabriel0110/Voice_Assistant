import time
import pyautogui
import win32com.client as wincl

def workTimer():
	speak = wincl.Dispatch("SAPI.SpVoice")
	
	check = confirm(text = "TAKE A 15 MINUTE BREAK", title = "Work/Study Break Timer", buttons = ['OK', 'No thanks'])
	
	while check == "OK":
		speak.Speak("Timer started for 15 minutes")
		time.sleep(15 * 60)
		speak.Speak("Break time has ended")
		alert(text = "Break over, get back to work! (1 Hour)", title = "Work/Study Break Timer", buttons = ['OK'])
		time.sleep(60 * 60)
		check = confirm(text = "TAKE A 15 MINUTE BREAK", title = "Work/Study Break Timer", buttons = ['OK', 'No thanks'])
