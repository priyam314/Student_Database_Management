# Standard Library Imports
from tkinter import Frame, Label, Entry, Button
import tkinter.messagebox as MessageBox
from tkinter import ttk
import re
import smtplib 
import random, math
from abc import ABCMeta, abstractstaticmethod

# Third Party Libraries
import mysql.connector as mysql

# Local Libraries
import workspace.adminWindow
from globals.constants import *
from user.auth import AuthLogin, AuthRegister

mc = MysqlConnect()

class EntryWindow:
	def __init__(self,root):

		# configure window

		self.root = root
		self.root.title("Login")
		self.root.geometry("500x400")
		self.root.configure(bg=BackgroundColor.background)
		self.root.columnconfigure(0,weight=1)
		self.root.rowconfigure(0,weight=1)
		self.s = ttk.Style()
		self.s.configure("TFrame",background=BackgroundColor.background)
		self.s.configure("TNotebook",background=BackgroundColor.background)
		self.s.map("TNotebook.Tab", background=[("selected", BackgroundColor.background)])
		self.s.configure("TNotebook.Tab",background=ButtonColor.background)

		# Utility Variables

		# self.username 	= ""
		# self.password 	= ""
		# self.fullname 	= ""
		# self.email 	  	= ""
		# self.repassword = ""

		# Frames

		self.frame1 = Frame(self.root)
		self.frame1.grid(row=0,column=0,sticky="ewsn")
		self.frame1.columnconfigure(0,weight=1)
		self.frame1.rowconfigure(0,weight=1)

		self.frame2 = Frame(self.root,background=BackgroundColor.background)
		self.frame2.grid(row=1, column=0, sticky="ewsn")
		self.frame2.columnconfigure(0,weight=1)
		self.frame2.rowconfigure(0,weight=1)

		self.frame3 = Frame(self.root,background=BackgroundColor.background)
		self.frame3.grid(row=2, column=0, sticky="ewsn")
		self.frame3.columnconfigure(0,weight=1)
		self.frame3.rowconfigure(0,weight=1)

		# Label

		self.AuthenticationLabel = Label(self.frame1, 
			text="Login/Register",
			font=('bold',16),fg="#000000",bg=BackgroundColor.background)
		self.AuthenticationLabel.grid(row=0, column=0, sticky="ewsn")

		# Tab Notebook

		self.tabControl = ttk.Notebook(self.frame2)

		# tabs

		self.tabLogin = ttk.Frame(self.tabControl)
		self.tabSignup = ttk.Frame(self.tabControl)
		#self.tabSignup.columnconfigure(0,weight=1)

		self.tabControl.add(self.tabLogin, text ='Login')
		self.tabControl.add(self.tabSignup, text ='Sign Up')
		self.tabControl.pack(fill ="none",expand=1)
		

		# LOGIN

		# Labels

		self.usernameLabelLogin = Label(self.tabLogin, text="Username",
			font=('bold',10),fg="#000000",bg=BackgroundColor.background)
		self.usernameLabelLogin.grid(row=0, column=0, sticky="ewsn",padx=5,pady=29)

		self.passwordLabelLogin = Label(self.tabLogin, text="Password",
			font=('bold',10),fg="#000000",bg=BackgroundColor.background)
		self.passwordLabelLogin.grid(row=1, column=0, sticky="ewsn",padx=5,pady=5)

		# Entry

		self.usernameEntryLogin = Entry(self.tabLogin, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background)
		self.usernameEntryLogin.grid(row=0, column=1, sticky="ewsn",padx=5,pady=29)

		self.passwordEntryLogin = Entry(self.tabLogin, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background, show="*")
		self.passwordEntryLogin.grid(row=1, column=1, sticky="ewsn",padx=5,pady=5)

		# SIGN UP

		# Labels

		self.fullnameLabel = Label(self.tabSignup, text="Full Name",
			font=('bold',10),fg="#000000",bg=BackgroundColor.background)
		self.fullnameLabel.grid(row=0, column=0, sticky="ew",padx=5,pady=5)

		self.usernameLabel = Label(self.tabSignup, text="Username",
			font=('bold',10),fg="#000000",bg=BackgroundColor.background)
		self.usernameLabel.grid(row=1, column=0, sticky="ew",padx=5,pady=5)

		self.emailLabel = Label(self.tabSignup, text="Email",
			font=('bold',10),fg="#000000",bg=BackgroundColor.background)
		self.emailLabel.grid(row=2, column=0, sticky="ew",padx=5,pady=5)

		self.passwordLabel = Label(self.tabSignup, text="Password",
			font=('bold',10),fg="#000000",bg=BackgroundColor.background)
		self.passwordLabel.grid(row=3, column=0, sticky="ew",padx=5,pady=5)

		self.repasswordLabel = Label(self.tabSignup, text="Re Enter Password",
			font=('bold',10),fg="#000000",bg=BackgroundColor.background)
		self.repasswordLabel.grid(row=4, column=0, sticky="ew",padx=5,pady=5)

		# Entry

		self.fullnameEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background)
		self.fullnameEntry.grid(row=0, column=1, sticky="ew",padx=5,pady=5)

		self.usernameEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background)
		self.usernameEntry.grid(row=1, column=1, sticky="ew",padx=5,pady=5)

		self.emailEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background)
		self.emailEntry.grid(row=2, column=1, sticky="ew",padx=5,pady=5)

		self.passwordEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background, show="*")
		self.passwordEntry.grid(row=3, column=1, sticky="ew",padx=5,pady=5)

		self.repasswordEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background, show="*")
		self.repasswordEntry.grid(row=4, column=1, sticky="ew",padx=5,pady=5)

		# Button

		self.submitButton = Button(self.frame3,text="Submit",
			bg=ButtonColor.background,font=('italic',10),command=lambda:self.Submit())
		self.submitButton.grid(padx=10,pady=10)

	# Methods

	# def getLoginEntries(self):
	# 	self.username = self.usernameEntryLogin.get()
	# 	self.password = self.passwordEntryLogin.get()

	# def getSignUpEntries(self):
	# 	self.fullname = str(self.fullnameEntry.get())
	# 	self.username = str(self.usernameEntry.get())
	# 	self.email = str(self.emailEntry.get())
	# 	self.password = str(self.passwordEntry.get())
	# 	self.repassword = str(self.repasswordEntry.get())

	# def submitLOGIN(self):
	# 	self.getLoginEntries()
	# 	if (self.username=="" or self.password==""):
	# 			MessageBox.showinfo("Login status Error","All the fields are required")
	# 	else:
	# 		with Database() as con:
	# 			cursor = con.cursor()
	# 			cursor.execute("SELECT * FROM newDB.USERS where USERNAME='{}'".format(str(self.username)))
	# 			row = cursor.fetchmany(size=1)
	# 			try:
	# 				if (str(row[0][1])==str(self.password)):
	# 					self.root.destroy()
	# 					newroot = Tk()
	# 					app = CRUD.App(newroot,str(row[0][4]))
	# 					newroot.mainloop()
	# 				else:
	# 					MessageBox.showinfo("Login Status","Either Password or Username is wrong")
	# 			except IndexError:
	# 				MessageBox.showinfo("Login Status","User not found")

	# def clearFields(self):
	# 	self.usernameEntry.delete("1.0", 'end')
	# 	self.fullnameEntry.delete("1.0", 'end')
	# 	self.emailEntry.delete("1.0", 'end')
	# 	self.passwordEntry.delete("1.0", 'end')
	# 	self.repasswordEntry.delete("1.0", 'end')

	# def submitSIGNUP(self):
	# 	self.getSignUpEntries()
	# 	root.destroy()
	# 	if (self.fullname=="" or self.username=="" or self.email=="" or 
	# 		self.password=="" or self.repassword==""):
	# 		MessageBox.showinfo("Signup status Error","All the fields are required")
	# 	else:
	# 		if (self.checkAll(self.username,self.fullname,self.email,self.password,self.repassword)):
	# 			uniqID = shortuuid.uuid(str(self.username)+str(self.password)+str(self.email))
	# 			otpwindow()
	# 			with Database() as con:
	# 				cursor = con.cursor()
	# 				try:
	# 					if(Login.otpBOOL==True):
	# 						cursor.execute("INSERT INTO newDB.USERS VALUES('{}','{}','{}','{}','{}');".format(
	# 							str(self.username),str(self.password),str(self.fullname),str(self.email),str(uniqID)))
	# 						cursor.execute("COMMIT;")
	# 						print("first done")
	# 						cursor.execute("INSERT INTO newDB.STUDENTS VALUES({},'{}',{},'{}');".format(1,"update me",0,str(uniqID)))
	# 						cursor.execute("COMMIT;")
	# 						print("second done")
	# 					else:
	# 						print("abhi nhi hua")
	# 				except:
	# 					print("its error")

	# 			print("done")
					
	def Submit(self):
		currentTab = str(self.tabControl.tab(self.tabControl.select(), "text"))
		if (currentTab=="Login"):
			if (AuthLogin(mc).authenticate(
				username = self.usernameEntryLogin.get(),
				passwd = self.passwordEntryLogin.get())):
				# initialize workspaceCRUD
				pass 

		else:
			if (AuthRegister(mc).authenticate(
				username = self.usernameEntry.get(),
				passwd = self.passwordEntry.get(),
				fullname = self.fullnameEntry.get(),
				repasswd = self.repasswordEntry.get(),
				email = self.emailEntry.get())):
				# initialize workspaceCRUD
				pass

	# def checkUsername(self, username):
	# 	if (any(i in username for i in "!@#$%^&*()_+=-`~,./';<>?: ")):
	# 		MessageBox.showinfo("Username status","Character(s) are not allowed")
	# 		return 0
	# 	if (any(c.isalpha() for c in username)==False):
	# 		MessageBox.showinfo("Username status","Alphabest(s) mandatory in Username")
	# 		return 0
	# 	return 1
	# def checkFullname(self, fullname):
	# 	if ("".join(fullname.split(" ")).isalpha()==False):
	# 		MessageBox.showinfo("Fullname status","Only alphabests are allowed")
	# 		return 0
	# 	return 1
	# def checkEmail(self,email):
	# 	pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")
	# 	if (not bool(re.match(pattern,str(email)))):
	# 		MessageBox.showinfo("Email Status","Email has invalid format")
	# 		return 0
	# 	senderEmail = "pg7176@srmist.edu.in"
	# 	receiverEmail = str(email)
	# 	senderPassword = "Artificial!18"
	# 	Login.aOTP = str(generateOTP())
	# 	message = """
	# 				This message from CRUD Machine
	# 				Your OTP is {}
	# 	""".format(OTP.generate())
	# 	server = smtplib.SMTP('smtp.gmail.com',587)
	# 	server.starttls()
	# 	server.login(senderEmail,senderPassword)
	# 	server.sendmail(senderEmail, receiverEmail, message)
	# 	server.quit()
	# 	return 1	
	# def checkPassword(self, password):
	# 	if (len(password)<=8):
	# 		MessageBox.showinfo("Password Status","Password should contain more than 8 characters")
	# 		return 0
	# 	return 1
	# def checkRePassword(self,repassword,password):
	# 	if (repassword!=password):
	# 		MessageBox.showinfo("RePassword Status","Re-Password is different than Password")
	# 		return 0
	# 	return 1

	# def checkAll(self,username,fullname,email,password,repassword):
	# 	if (self.checkFullname(fullname and
	# 		self.checkUsername(username) and
	# 		self.checkEmail(email)	and
	# 		self.checkPassword(password) and
	# 		self.checkRePassword(repassword,password))):
	# 		return 1
	# 	return 0
				
# def generateOTP():
# 	string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 	OTP = ""
# 	length = len(string)
# 	for i in range(5) :
# 	    OTP += string[math.floor(random.random() * length)]
# 	return OTP


