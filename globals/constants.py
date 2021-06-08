# Standard Library Imports
from dataclasses import dataclass

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
	host:str = "localhost"
	user:str = "root"
	passwd:str = "Artificial!18intelligence"
	database:str = "newDB"

class AuthEmail:
	senderEmail:str = "<Sender Email>"
	senderPasswd:str = "<Sender Password>"
	message:str = "OTP for CRUD Machine is {}"
	OTP:str = ""
	
