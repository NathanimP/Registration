from tkinter import *
import sqlite3
from time import strftime

class Registration(Tk):
	def __init__(self):
		super().__init__()
		fnametxt = StringVar()
		lnametxt = StringVar()
		idtxt = StringVar()
		schooltxt = StringVar()
		label = Label(self,text="Registration",font="alian 15 bold",fg="yellow",bg="black")
		self.clock()
		label.pack()
		lname = Label(self,text="First Name",font="alian 10 bold",textvariable=fnametxt).place(y=180,x=0)
		lfname = Label(self,text="Last Name",font="alian 10 bold",textvariable=lnametxt).place(y=260,x=0)
		lid = Label(self,text="Id",font="alian 10 bold",textvariable=idtxt).place(y=340,x=0)
		lschool = Label(self,text="School",font="alian 10 bold",textvariable=schooltxt).place(y=420,x=0)
		self.fnameE = Entry(self,width=20)
		self.fnameE.place(y=180,x=250)
		self.lnameE = Entry(self,width=20)
		self.lnameE.place(y=260,x=250)
		self.idE = Entry(self,width=20)
		self.idE.place(y=340,x=250)
		self.schoolE = Entry(self,width=20)
		self.schoolE.place(y=420,x=250)
		btn = Button(self,text="Register Done",bg="lightblue",font="Times 10 bold",width=10,height=0,fg="blue",command=self.done).place(y=500,x=200)
	def done(self):
		fname = self.fnameE.get()
		lname = self.lnameE.get()
		id= self.idE.get()
		school = self.schoolE.get()
		DataBase.create_table()
		label = Label(self,text="",font="Times 10 italic",fg="black",width=30)
		label.place(y=600,x=0)
		if fname in [' ','']:
			label.config(text="First name is empty")
		elif lname in ['',' ']:
			label.config(text="Last Name is empty")
		elif id in ['',' ']:
			label.config(text="Id is empty ")
		elif school in ['',' ']:
			label.config(text="School is empty")
		else:
			text=DataBase.save_data(fname,lname,id,school)
			label.config(text=text)		
	def clock(self):
		time = strftime("%H:%M:%S")
		timelabel = Label(self,text=time,fg="black",font="Times 10 bold")
		timelabel.place(y=100,x=250)
		timelabel.after(1000,self.clock)
class DataBase:
	def __get(self):
		connection = sqlite3.connect("mydb.db")
		return connection
	@classmethod
	def create_table(cls):
		conn = cls.__get(cls)
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS studentdata(fist_name TEXT NOT NULL,last_name TEXT NOT NULL,id INTIGER NOT NULL,school TEXT NOT NULL)")
		conn.commit()
	@classmethod
	def save_data(cls,fname,lname,id,school):
		conn = cls.__get(cls)
		c = conn.cursor()
		c.execute("INSERT INTO studentdata VALUES(?,?,?,?)",(fname,lname,id,school))
		conn.commit()
		return "Your Data Has been saved!"
Registration().mainloop()