# Standard libraries
from tkinter import Frame, Entry, Button
import tkinter

# locall libraries
from globals.constants import *
from expr.check import *

class OTPcheck(ICheck):
	def __init__(self,entryBox, genOTP):
		self.entryBox = entryBox
		self.genOTP = genOTP
	def isOk(self)->bool:
		if (self.entryBox==self.genOTP):
			return True
		return False

class OTPwindow:
	def __init__(self,root,otp):

		# configure variables

		self.root = root
		self.otp = otp
		self.root.title("aOTP")
		self.root.geometry("200x200")
		self.root.columnconfigure(0,weight=1)
		self.root.rowconfigure(0,weight=1)

		# Frames
		
		self.frame1 = Frame(self.root,background=BackgroundColor.background)
		self.frame1.grid(padx=5,pady=5,sticky = "esnw",row=0,column=0)
		self.frame2 = Frame(self.root,background=BackgroundColor.background)
		self.frame2.grid(padx=5,pady=5,sticky = "esnw",row=1,column=0)

		# Entry

		self.entry = Entry(self.frame1, font=('bold',10),
			fg=EntryColor.entryText,bg=EntryColor.background)
		self.entry.pack()

		# Button

		self.button = Button(self.frame2, text="submit",
			bg=ButtonColor.background,font=('italic',10),command=lambda:self.Submit())
		self.button.pack()

	def Submit(self):
		if OTPcheck(self.entry.get(), self.otp).isOk():
			OTP.correct = True
		else:
			MessageBox.showinfo("aOTP Status","Wrong aOTP")
		self.destroy()

	def destroy(self):
		self.root.destroy()
	