# Standard Libraries
from abc import ABCMeta, abstractstaticmethod

# Third party libraries
import shortuuid

# local libraries
from globals.constants import MysqlConnect, AuthEmail, OTP
from expr.check import CheckUsername, CheckPassword, CheckEmail, CheckFullname, CheckRePassword, CheckAll, ICheck
from db.database import Database
from workspace.otpWindow import OTPwindow

class IAuth(metaclass=ABCMeta):
	def __init__(self, connectorDetail:MysqlConnect):
		self.connectorDetail = connectorDetail
	@classmethod
	def __subclasshook__(cls, subclass):
		return (hasattr(subclass,"authenticate") and callable(subclass.authenticate) or NotImplemented)
	@abstractstaticmethod
	def authenticate(self)->bool:
		pass

class CheckExist(ICheck):
	def __init__(self, connectorDetail:MysqlConnect, table:str):
		self.connectorDetail = connectorDetail
		self.table = table
	def isOk(self, value:str)->bool:
		pass

class CheckUsernameExist(CheckExist):
	def isOk(self, value:str)->bool:
		with Database(self.connectorDetail) as con:
			cursor = con.cursor()
			cursor.execute(
				"SELECT * FROM {}.{} WHERE USERNAME='{}';"
				.format(self.connectorDetail.database, table, value))
			row = cursor.fetchmany(size=1)
			if (len(row)>0):
				MessageBox.showinfo("SignUp Status","Username already exist")
				return False
			return True

class CheckEmailExist(ICheck):
	def isOk(self, value:str)->bool:
		with Database(self.connectorDetail) as con:
			cursor = con.cursor()
			cursor.execute(
				"SELECT * FROM {}.{} WHERE EMAIL='{}';"
				.format(self.connectorDetail.database, table, value))
			row = cursor.fetchmany(size=1)
			if (len(row)>0):
				MessageBox.showinfo("SignUp Status","Email already exist")
				return False
			return True

class AuthLogin(IAuth):
	def authenticate(self, username:str, passwd:str)->bool:
		if (CheckAll().isOk(CheckUsername().isOk(value=username),CheckPassword().isOk(value=passwd))):
			with Database(self.connectorDetail) as con:
				cursor = con.cursor()
				cursor.execute(
					"SELECT * FROM {}.USERS where USERNAME='{}'"
					.format(self.connectorDetail.database,username))
				row = cursor.fetchmany(size=1)
				try:
					if (str(row[0][1])==str(passwd)):
						return True
					else:
						MessageBox.showinfo("Login Status","Either Password or Username is wrong")
				except IndexError:
					MessageBox.showinfo("Login Status","User not found")
			return False
		return False

def otpwindow(otp):
	top=Tk()
	toplevel=OTPwindow(root=top,otp=otp)
	top.mainloop()	

class AuthRegister(IAuth):
	def authenticate(self, fullname:str, username:str, email:str, passwd:str, repasswd:str)->bool:
		if (CheckAll.isOk(
			CheckFullname.isOk(fullname=fullname), CheckPassword.isOk(password=passwd),CheckUsername.isOk(username=username),
			CheckEmail.isOk(email=email), CheckRePassword.isOk(repassword=repasswd) 
			)):
			if (CheckUsernameExist(MysqlConnect(),"USERS").isOk(username) and 
				CheckEmailExist(MysqlConnect(),"USERS").isOk(email)):
				uniqID = shortuuid.uuid(username+password+email)
				otpwindow(otp=AuthEmail.OTP)
				if (OTP.correct):
					with Database(self.connectorDetail) as con:
						cursor = con.cursor()
						cursor.execute(
							"INSERT INTO {}.USERS VALUES('{}','{}','{}','{}','{}');"
							.format(self.connectorDetail.database,username,passwd,fullname,email,str(uniqID)))
						cursor.execute("COMMIT;")
						cursor.execute(
							"INSERT INTO {}.STUDENTS VALUES({},'{}',{},'{}');"
							.format(self.connectorDetail.database,1,"null",0,str(uniqID)))
						cursor.execute("COMMIT;")
						return True
					return False
				return False
			return False
		

				
