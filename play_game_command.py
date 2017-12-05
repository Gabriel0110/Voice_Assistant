import subprocess
import pyautogui

def chooseGame(game.lower()):
	if game == "avolition":
		playAvolition()
		
def playAvolition():
	p = subprocess.Popen(['C:\WINDOWS\system32\cmd.exe'])
	
	pyautogui.typewrite("cd ..")
	pyautogui.press("enter")
	pyautogui.typewrite("cd ..")
	pyautogui.press("enter")
	pyautogui.typewrite("cd Avolition")
	pyautogui.press("enter")
	pyautogui.typewrite("python main.py")
	pyautogui.press("enter")
	p.kill()
