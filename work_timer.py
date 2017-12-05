import time
import pyautogui
import win32com.client as wincl

def workTimer(limit):
	speak = wincl.Dispatch("SAPI.SpVoice")
	
	check = pyautogui.confirm(text = "TAKE A " + str(limit) + " MINUTE BREAK", title = "Work/Study Break Timer", buttons = ['OK', 'No thanks'])
	
	if check == "OK":
		speak.Speak("Timer started for " + str(limit) + " minutes")
		time.sleep(limit * 60)
		speak.Speak("Break time has ended")
		pyautogui.alert(text = "Break over, get back to work! (1 Hour)", title = "Work/Study Break Timer", button = ['OK'])
	
	"""
	while check == "OK":
		speak.Speak("Timer started for " + str(limit) + " minutes")
		time.sleep(limit * 60)
		speak.Speak("Break time has ended")
		pyautogui.alert(text = "Break over, get back to work! (1 Hour)", title = "Work/Study Break Timer", button = ['OK'])
		time.sleep(60 * 60)
		check = pyautogui.confirm(text = "TAKE A " + str(limit) + " MINUTE BREAK", title = "Work/Study Break Timer", buttons = ['OK', 'No thanks'])
	"""
