# Standard Library Imports
from abc import ABC, abstractstaticmethod
import tkinter.messagebox as MessageBox
from smtplib import SMTP

# Local libraries
from util.generate import OTP
from globals.constants import MysqlConnect

class ICheck(ABC):
	@abstractstaticmethod
	def isOk(self):
		pass

class CheckSubjectName(ICheck):
	def isOk(self, name:str)->bool:
		if (name==""):
			MessageBox.showinfo("Subject Status","Subject field cannot be empty")
			return False
		return True

class CheckSubjectMarks(ICheck):
	def isOk(self, marks:str)->bool:
		if (int(marks)>100 or int(marks)<0):
			MessageBox.showinfo("Marks Status","Marks cannot be either less than 0 or more than 100")
			return False
		elif (marks==""):
			MessageBox.showinfo("Marks Status","Marks field cannot be left empty")
			return False
		return True

class CheckSubjectId(ICheck):
	def isOk(self, id:str)->bool:
		if (id==""):
			MessageBox.showinfo("Id Status","Id field is required")
			return False
		return True
class CheckUsername(ICheck):
	def isOk(self, username:str)->bool:
		if (any(i in username for i in "!@#$%^&*()_+=-`~,./';<>?: ")):
			MessageBox.showinfo("Username status","Character(s) are not allowed")
			return False
		if (any(c.isalpha() for c in username)==False):
			MessageBox.showinfo("Username status","Alphabest(s) mandatory in Username")
			return False
		return True

class CheckFullname(ICheck):
	def isOk(self, fullname:str)->bool:
		if ("".join(fullname.split(" ")).isalpha()==False):
			MessageBox.showinfo("Fullname status","Only alphabests are allowed")
			return False
		elif (fullname==""):
			MessageBox.showinfo("Fullname status","Fullname field cannot be remained empty")
			return False
		return True

class CheckPassword(ICheck):
	def isOk(self, password:str)->bool:
		if (len(password)<=8):
			MessageBox.showinfo("Password Status","Password should contain more than 8 characters")
			return False
		return True

class CheckRePassword(ICheck):
	def isOk(self, password:str, repassword:str)->bool:
		if (repassword!=password):
			MessageBox.showinfo("RePassword Status","Re-Password is different than Password")
			return False
		return True

class CheckEmail(ICheck):
	def isOk(self, email:str)->bool:
		pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")
		if (not bool(re.match(pattern,email))):
			MessageBox.showinfo("Email Status","Email has invalid format")
			return False
		senderEmail = AuthEmail.senderEmail
		receiverEmail = email
		senderPassword = AuthEmail.senderPasswd
		AuthEmail.OTP = OTP.generate()
		message = AuthEmail.message.format(AuthEmail.OTP)
		try:
			server = SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(senderEmail, senderPassword)
			server.sendmail(senderEmail, receiverEmail, message)
		except SMTPResponseException as e:
			error_code = e.smtp_code
			error_message = e.smtp_error
			MessageBox.showinfo("Error Code {}".format(error_code),
    			"ERROR MSG: {}".format(error_message))
			return False
		finally:
			server.quit()
			return True

class CheckAll(ICheck):
	def isOk(self, *args)->bool:
		return all(args)




