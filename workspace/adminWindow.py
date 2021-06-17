# Standard Library Imports
from tkinter import LabelFrame, Label, Entry, Button, StringVar
from tkinter import ttk
import tkinter.messagebox as MessageBox

# Third Party Libraries
import mysql.connector as mysql

# Local Libraries
from constants import *
from db.database import Database
from db.req import UpdateManager, DestructManager, ConstructManager, RetrieveManager, DestructAllManager

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

        self.Id = StringVar()
        self.Name = StringVar()
        self.Number = StringVar()
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
            highlightcolor=EntryColor.highlight,fg=EntryColor.entryText,
            textvariable=self.Id,font=('bold'))
        self.e_ID.grid(row=0, column=1,pady=5,padx=5)

        self.e_NAME = Entry(self.searchFrame,bg=EntryColor.background,
            highlightcolor=EntryColor.highlight,fg=EntryColor.entryText,
            textvariable=self.Name,font=('bold'))
        self.e_NAME.grid(row=1, column=1,pady=5,padx=5)

        self.e_NUMBER = Entry(self.searchFrame,bg=EntryColor.background,
            highlightcolor=EntryColor.highlight,fg=EntryColor.entryText,
            textvariable=self.Number,font=('bold'))
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
