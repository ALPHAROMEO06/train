import tkinter as tk
from tkinter import *

class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_1 = tk.Label(self, text="Username")
        self.label_2 = tk.Label(self, text="Password")

        self.entry_1 = tk.Entry(self)
        self.entry_2 = tk.Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.logbtn = tk.Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        # print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        # print(username, password)

        if username == "john" and password == "password":
            print("Successful login")
        else:
            print("Wrong username or password")

root = tk.Tk()
lf = Login(root)
root.mainloop()
