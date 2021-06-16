## Standard Library Imports
from tkinter import Frame, Label, Entry, Button, Tk, StringVar
import tkinter.messagebox as MessageBox
from tkinter import ttk
import re
import smtplib 
import random, math
from abc import ABCMeta, abstractstaticmethod

## Local Libraries
import workspace.adminWindow as admin
from constants import *
from form.auth import AuthLogin, AuthRegister

mc = MysqlConnect()     

class EntryWindow:
	"""
	EntryWindow is the first window that will appear after main.py 
	will execute. This window contains form, for login, signup of 
	existing or new users respectively. 

	LOGIN Workflow
		- username,password (@Compulsory fields,Not Null)
		- The following variables with MySqlConnect object is passed to AuthLogin

		- check class does grammer check to verify both are in correct format


	"""
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

		self.username = StringVar()
		self.password = StringVar()
		self.fullname = StringVar()
		self.email    = StringVar()
		self.repassword = StringVar()

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
			fg=EntryColor.entryText,bg=EntryColor.background,textvariable=self.username)
		self.usernameEntryLogin.grid(row=0, column=1, sticky="ewsn",padx=5,pady=29)

		self.passwordEntryLogin = Entry(self.tabLogin, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background, show="*",textvariable=self.password)
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
			fg=EntryColor.entryText,bg=EntryColor.background,textvariable=self.fullname)
		self.fullnameEntry.grid(row=0, column=1, sticky="ew",padx=5,pady=5)

		self.usernameEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background, textvariable=self.username)
		self.usernameEntry.grid(row=1, column=1, sticky="ew",padx=5,pady=5)

		self.emailEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background,textvariable=self.email)
		self.emailEntry.grid(row=2, column=1, sticky="ew",padx=5,pady=5)

		self.passwordEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background, show="*",textvariable=self.password)
		self.passwordEntry.grid(row=3, column=1, sticky="ew",padx=5,pady=5)

		self.repasswordEntry = Entry(self.tabSignup, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background, show="*",textvariable=self.repassword)
		self.repasswordEntry.grid(row=4, column=1, sticky="ew",padx=5,pady=5)

		# Button

		self.submitButton = Button(self.frame3,text="Submit",
			bg=ButtonColor.background,font=('italic',10),command=lambda:self.Submit())
		self.submitButton.grid(padx=10,pady=10)

	# Methods
					
	def Submit(self):
		currentTab = str(self.tabControl.tab(self.tabControl.select(), "text"))
		if (currentTab=="Login"):
			if (AuthLogin(mc).authenticate(
				username = self.username.get(),
				passwd = self.password.get())):
				# initialize workspaceCRUD
				self.root.destroy()
				ifndef = True
				rootAdmin = Tk()
				app = admin.AdminWindow(rootAdmin, UNIQID)
				if ifndef:
					# self.root.destroy()
					ifndef = False
				rootAdmin.mainloop()

		else:
			if (AuthRegister(mc).authenticate(
				username = self.usernameEntry.get(),
				passwd = self.passwordEntry.get(),
				fullname = self.fullnameEntry.get(),
				repasswd = self.repasswordEntry.get(),
				email = self.emailEntry.get())):
				# initialize workspaceCRUD
				pass

	

