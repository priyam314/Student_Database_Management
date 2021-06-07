# Standard Library Imports
from abc import ABCMeta, abstractstaticmethod
from database import Database
import tkinter.messagebox as MessageBox

# Local Libraries
from clear import Entry
from constants import MysqlConnect
from check import CheckSubjectName, CheckSubjectMarks, CheckSubjectId

class IDatabaseManagerProcess(meta=ABCMeta):
	def __init__(self, connectorDetail:MysqlConnect):
		self.connectorDetail:MysqlConnect = connectorDetail
	@abstractstaticmethod
	def do(self):
		pass

class DatabaseManagerCheckDetails(IDatabaseManagerProcess):
	@abstractstaticmethod
	def checkDetails(self)->bool:
		pass

class UpdateManager(DatabaseManagerCheckDetails):
	def checkDetails(self, idAmend:str, nameAmend:str, marksAmend:str)->bool:
		if (CheckSubjectId.isOk(idAmend) and CheckSubjectName.isOk(nameAmend) and 
			CheckSubjectMarks.isOk(marksAmend)):
			return True
		return False
	def do(self, idAmend:str, nameAmend:str, marksAmend:str, uniqueidAmend:str):
		if (self.checkDetails(idAmend, nameAmend, marksAmend)):
			with Database(self.connectorDetail) as con:
				cursor = con.cursor(
					"UPDATE {}.STUDENTS SET NAME='{}',MARKS={} WHERE ID={} AND UNIQUEID='{}';"
					.format(self.connectorDetail.databse,nameAmend,marksAmend,idAmend,uniqueidAmend))
				cursor.execute("COMMIT;")
			MessageBox.showinfo("Update Status","Updated Successfully")

class DestructManager(DatabaseManagerCheckDetails):
	def checkDetails(self, idDestruct:str)->bool:
		if (CheckSubjectId.isOk(idDestruct)):
			return True
		return False
	def do(self,idDestruct:str, uniqueidDestruct:str):
		if (self.checkDetails(idDestruct)):
			with Database(self.connectorDetail) as con:
				cursor = con.cursor()
				cursor.execute(
					"DELETE FROM {}.STUDENTS WHERE ID={} AND UNIQUEID='{}';"
					.format(self.connectorDetail.database, idDestruct, uniqueidDestruct))
				cursor.execute("COMMIT;")
			MessageBox.showinfo("Delete Status", "Deleted Successfully")

class ConstructManager(DatabaseManagerCheckDetails):
	def checkDetails(self, idConstruct:str, nameConstruct:str, marksConstruct:str)->bool:
		if (CheckSubjectId.isOk(idConstruct) and CheckSubjectName.isOk(nameConstruct) and 
			CheckSubjectMarks.isOk(marksConstruct)):
			return True
		return False
	def do(self, idConstruct:str, nameConstruct:str, marksConstruct:str, uniqueidConstruct:str):
		if (self.checkDetails(idConstruct, nameConstruct, marksConstruct)):
			with Database(self.connectorDetail) as con:
				cursor = con.cursor()
				cursor.execute(
					"INSERT INTO {}.STUDENTS VALUES({},'{}',{},'{}');"
					.format(self.connectorDetail.database,idConstruct,nameConstruct,marksConstruct,uniqueidConstruct))
				cursor.execute("COMMIT;")
			MessageBox.showinfo("Insert Status","Inserted Successfully")
			Entry(idConstruct, nameConstruct, marksConstruct).clear()

class RetrieveManager(DatabaseManagerCheckDetails):
	def checkDetails(self, idRetrieve:str)->bool:
		if (CheckSubjectId.isOk(idRetrieve)):
			return True
		return False
	def do(self, idRetrieve, nameRetrieve, marksRetrieve, uniqueidRetrieve):
		if (self.checkDetails(idRetrieve.get())):
			with Database(self.connectorDetail) as con:
				cursor = con.cursor()
				cursor.execute(
					"SELECT * FROM {}.STUDENTS WHERE ID={} AND UNIQUEID='{}';"
					.format(self.connectorDetail.database,idRetrieve.get(),uniqueidRetrieve.get()))
				rows = cursor.fetchmany(size=1)
				Entry(idRetrieve,nameRetrieve,marksRetrieve).clear()
				for row in rows:
					idRetrieve.insert(0, row[0])
					nameRetrieve.insert(0, row[1])
					marksRetrieve.insert(0, row[2])
			MessageBox.showinfo("Get Status","Retrieved Successfully")

class DestructAllManager(IDatabaseManagerProcess):
	def do(self, uniqueidDestructAll:str):
		with Database(self.connectorDetail) as con:
			cursor = con.cursor()
			cursor.execute(
				"DELETE FROM {}.STUDENTS WHERE UNIQUEID='{}';"
				.format(self.connectorDetail.database,uniqueidDestructAll))
			cursor.execute("COMMIT;")
		MessageBox.showinfo("Delete All Status","All fields deleted Successfully")
