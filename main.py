# Standard library modules
from tkinter import Tk 

# Local Libraries
from workspace.entryWindow import EntryWindow

if __name__=="__main__":
	rootEntry = Tk()
	app= EntryWindow(rootEntry)
	rootEntry.mainloop()