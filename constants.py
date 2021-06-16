# Standard Library Imports
from dataclasses import dataclass

# third party libraries
from decouple import config

class BackgroundColor:
	background:str = "#f6f4d2"

class ButtonColor:
	background:str = "#f19c79"

class EntryColor:
	entryText:str = "#2f3e46"
	background:str = "#d4e09b"
	highlight:str = "#6d6875"

class OTP:
	correct:bool = False

class TreeviewContentShow:
	ifndef:bool = True

@dataclass
class MysqlConnect:
	host:str = config("HOST")
	user:str = config("USER")
	passwd:str = config("PASSWD")
	database:str = config("DB")

class AuthEmail:
	senderEmail:str = "<Sender Email>"
	senderPasswd:str = "<Sender Password>"
	message:str = "OTP for CRUD Machine is {}"
	OTP:str = ""

UNIQID:str = ""
	
