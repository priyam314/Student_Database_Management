# Standard Library Imports
from tkinter import LabelFrame, Label, Entry, Button
from tkinter import ttk
import tkinter.messagebox as MessageBox

# Third Party Libraries
import mysql.connector as mysql

# Local Libraries
from globals.constants import *
from db.database import Database
from db.res import UpdateManager, DestructManager, ConstructManager, RetrieveManager, DestructAllManager

myConnect = MysqlConnect()

class AdminWindow:
    def __init__(self,root,uniqid):

        # configure window
        
        self.root = root
        self.root.title('CRUD')
        self.root.geometry('640x420')
        self.root.configure(bg=BackgroundColor.background)
        ttk.Style().configure("Treeview",fieldbackground="#E9C46A")

        # Utility Variables

        # self.Id = ""
        # self.Name = ""
        # self.Number = ""
        self.uniqid = uniqid

        # LabelFrames

        self.showFrame = LabelFrame(self.root, text="Database",
            labelanchor='n',bg=BackgroundColor.background)
        self.showFrame.grid(row=0, column=0,sticky="nswe",padx=10,pady=10)

        self.searchFrame = LabelFrame(self.root, text="Values",
            labelanchor='n',bg=BackgroundColor.background)
        self.searchFrame.grid(row=1, column=0,sticky="nswe",padx=10,pady=10)

        self.changeFrame = LabelFrame(self.root, text="Operation",
            labelanchor='n',bg=BackgroundColor.background)
        self.changeFrame.grid(row=2, column=0,sticky="nswe",padx=10,pady=10)

        # Treeview

        self.treeFrame = ttk.Treeview(self.showFrame, selectmode="browse",
            columns=(1,2,3),show="headings",height="6")
        self.treeFrame.grid(row=0, column=0,sticky="e",padx=3,pady=3)

        self.verscrlbar = ttk.Scrollbar(self.showFrame, orient ="vertical", 
            command = self.treeFrame.yview)
        self.verscrlbar.grid(row=0, column=1,sticky="nw",padx=3,pady=3)

        self.treeFrame.column("1", minwidth=90, anchor ='c', stretch=True)                      
        self.treeFrame.column("2", minwidth=200,anchor ='c', stretch=True)
        self.treeFrame.column("3", minwidth=90, anchor ='c', stretch=True)

        self.treeFrame.heading("1", text ="ID")
        self.treeFrame.heading("2", text ="NAME")
        self.treeFrame.heading("3", text ="MARKS")

        if TreeviewContentShow.ifndef:
            self.treeviewcontent=TreeviewContent(myConnect)
            self.treeviewcontent.show(Object=self.treeFrame,uniqueId=self.uniqid)
            TreeviewContentShow.ifndef=False
        self.treeviewcontent.show(Object=self.treeFrame,uniqueId=self.uniqid)

        # Labels

        self.ID = Label(self.searchFrame, text="ID", 
            font=('bold', 13),fg="#000000",bg=BackgroundColor.background).grid(
            row=0, column=0,pady=5,padx=5)

        self.NAME = Label(self.searchFrame, text="NAME", 
            font=('bold', 13),fg="#000000",bg=BackgroundColor.background).grid(
            row=1,column=0,pady=5,padx=5)

        self.NUMBER = Label(self.searchFrame, text="NUMBER", 
            font=('bold', 13),fg="#000000",bg=BackgroundColor.background).grid(
            row=2, column=0,pady=5,padx=5)

        # Entry

        self.e_ID = Entry(self.searchFrame,bg=EntryColor.background,
            highlightcolor=EntryColor.highlight,fg=EntryColor.entryText,font=('bold'))
        self.e_ID.grid(row=0, column=1,pady=5,padx=5)

        self.e_NAME = Entry(self.searchFrame,bg=EntryColor.background,
            highlightcolor=EntryColor.highlight,fg=EntryColor.entryText,font=('bold'))
        self.e_NAME.grid(row=1, column=1,pady=5,padx=5)

        self.e_NUMBER = Entry(self.searchFrame,bg=EntryColor.background,
            highlightcolor=EntryColor.highlight,fg=EntryColor.entryText,font=('bold'))
        self.e_NUMBER.grid(row=2, column=1,pady=5,padx=5)

        # Buttons

        self.insert = Button(self.changeFrame, text="insert", font=("italic", 10), 
            bg=ButtonColor.background, width=6,command=lambda:ConstructManager(myConnect).do(
            idConstruct=self.e_ID.get(), nameConstruct=self.e_NAME.get(),
            marksConstruct=self.e_NUMBER.get(), uniqueidConstruct=self.uniqid)).grid(
            row=0,column=0,sticky="nswe",pady=5,padx=5)

        self.delete = Button(self.changeFrame, text="delete", font=("italic", 10), 
            bg=ButtonColor.background, command=lambda:DestructManager(myConnect).do(
            idDestruct=self.e_ID.get(), uniqueidDestruct=self.uniqid),width=6).grid(
            row=0,column=1,sticky="nswe",pady=5,padx=5)

        self.update = Button(self.changeFrame, text="update", font=("italic", 10), 
            bg=ButtonColor.background, command=lambda:UpdateManager(myConnect).do(
            idAmend=self.e_ID.get(), nameAmend= self.e_NAME.get(), 
            marksAmend= self.e_NUMBER.get(), uniqueidAmend= self.uniqid),width=6).grid(
            row=0,column=2,sticky="nswe",pady=5,padx=5)

        self.get = Button(self.changeFrame, text="get", font=("italic", 10), 
            bg=ButtonColor.background, command=lambda:RetrieveManager(myConnect).do(
            idRetrieve=self.e_ID, nameRetrieve=self.e_NAME, marksRetrieve=self.e_NUMBER,
            uniqueidRetrieve=self.uniqid),width=6).grid(
            row=0, column=3,sticky="nswe",pady=5,padx=5)

        self.deleteall = Button(self.changeFrame, text="delete all", font=("italic", 10), 
            bg=ButtonColor.background, command=lambda:DestructAllManager(myConnect).do(
            uniqueidDestructAll=self.uniqid),width=6).grid(
            row=0,column=4,sticky="nswe",pady=5,padx=5)
            
    # def getRow(self):
    #     self.Id = self.e_ID.get()
    #     self.Name = self.e_NAME.get()
    #     self.Number = self.e_NUMBER.get()

    # def checkAll(self, messageStatus, message):
    #     if (self.Id == "" or self.Name == "" or self.Number == ""):
    #         MessageBox.showinfo(messageStatus, message)
    #         return 0
    #     return 1

    # def checkID(self, messageStatus, message):
    #     if (self.e_ID.get() == ""):
    #         MessageBox.showinfo(messageStatus, message)
    #         return 0
    #     return 1

    # def clearFields(self):
    #     self.e_ID.delete(0, 'end')
    #     self.e_NAME.delete(0, 'end')
    #     self.e_NUMBER.delete(0, 'end')

    # def insertFunc(self):
    #     self.getRow()
    #     if (self.checkAll("insert status", "all fields are required")):
    #         with Database() as con:
    #             cursor=con.cursor()
    #             cursor.execute("INSERT INTO newDB.STUDENTS VALUES({},'{}',{},'{}');".format(self.Id,self.Name,self.Number,self.uniqid))
    #             cursor.execute("COMMIT;")
    #         self.clearFields()
    #         MessageBox.showinfo("Insert Status", "Inserted Successfully")
    #         TreeviewContent(host="localhost",user="root",passwd="Artificial!18intelligence",database="newDB").show(Object=self.treeFrame,uniqueId=self.uniqid)

    # def deleteFunc(self):
    #     if (self.checkID("Delete Status", "ID is compulsory to delete")):
    #         with Database() as con:
    #             cursor = con.cursor()
    #             cursor.execute("DELETE FROM newDB.STUDENTS WHERE ID={} AND UNIQUEID='{}';".format(self.e_ID.get(),str(self.uniqid)))
    #             cursor.execute("COMMIT;")
    #         self.clearFields()
    #         MessageBox.showinfo("Delete Status", "Deleted Successfully")
    #         # self.show()
    #         TreeviewContent(host="localhost",user="root",passwd="Artificial!18intelligence",database="newDB").show(Object=self.treeFrame,uniqueId=self.uniqid)

    # def deleteallFunc(self):
    #     with Database() as con:
    #         cursor = con.cursor()
    #         cursor.execute("DELETE FROM newDB.STUDENTS WHERE UNIQUEID='{}';".format(str(self.uniqid)))
    #         cursor.execute("COMMIT;")
    #     self.clearFields()
    #     MessageBox.showinfo("Delete Status", "Deleted Successfully")
    #     # self.show()
    #     TreeviewContent(host="localhost",user="root",passwd="Artificial!18intelligence",database="newDB").show(Object=self.treeFrame,uniqueId=self.uniqid)

    # def updateFunc(self):
    #     self.getRow()
    #     if (self.checkAll("update status", "ID and (Name or Number) field is required")):
    #         with Database() as con:
    #             cursor = con.cursor()
    #             cursor.execute("UPDATE newDB.STUDENTS SET NAME='{}',MARKS={} WHERE ID={} AND UNIQUEID='{}';".format(self.Name,self.Number,self.Id,str(self.uniqid)))
    #             cursor.execute("COMMIT;")
    #         self.clearFields()
    #         MessageBox.showinfo("Update Status", "Updated Successfully")
    #         # self.show()
    #         TreeviewContent(host="localhost",user="root",passwd="Artificial!18intelligence",database="newDB").show(Object=self.treeFrame,uniqueId=self.uniqid)

    # def getFunc(self):
    #     if (self.checkID("get Status", "ID is compulsory to fetch")):
    #         with Database() as con:
    #             cursor=con.cursor()
    #             cursor.execute("SELECT * FROM newDB.STUDENTS WHERE ID={} AND UNIQUEID='{}';".format(self.e_ID.get(),str(self.uniqid)))
    #             rows = cursor.fetchmany(size=1)
    #             self.clearFields()
    #             for row in rows:
    #                 self.e_ID.insert(0, row[0])
    #                 self.e_NAME.insert(0, row[1])
    #                 self.e_NUMBER.insert(0, row[2])
    #         MessageBox.showinfo("get Status", "fetched Successfully")

class TreeviewContent:
    def __init__(self, connectorDetail:MysqlConnect):
        self.connectorDetail:MysqlConnect = connectorDetail
    def show(self, Object, uniqueId:str):
        with Database(self.connectorDetail) as con:
            cursor = con.cursor()
            cursor.execute(
                "SELECT * FROM {}.STUDENTS WHERE UNIQUEID='{}';"
                .format(self.connectorDetail.database,uniqueId))
            rows = cursor.fetchall()
            for item in Object.get_children():
                Object.delete(item)
            for row in rows:
                Object.insert('','end',values=(row[0],row[1],row[2]))
