import tkinter as tk

#color #B07EEC  

class GUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x600")
        self.root.resizable(False,False)
        self.root.configure(bg="#AAC8A7")
        self.root.title("Todo List")

        


        self.l1 = tk.Label(self.root,font = ("Comic Sans MS",40,"bold"), text="Todo List",fg = "#4F6F52",bg = "#C3EDC0")
        self.l1.place(relx=0,height = 80, width = 500, )

        self.e1 = tk.Entry(self.root,fg="#4F6F52",bd=0,bg="#E9FFC2",font = ("Comic Sans MS",10,"bold"))
        self.e1.place(relx =0.05, rely=0.2,height = 30, width=400)

        self.b1 = tk.Button(self.root,text="+ New Task",font = ("Comic Sans MS",10,"bold"),fg="#4F6F52",bd=0,bg="#E9FFC2",command = self.add)
        self.b1.place(relx =0.05, rely=0.28, height = 40,width=110)

        self.b2 = tk.Button(self.root,text="- Remove Task",font = ("Comic Sans MS",10,"bold"),fg="#4F6F52",bd=0,bg="#E9FFC2",command = self.remove)
        self.b2.place(relx =0.3, rely=0.28, height = 40,width=120)

        self.lb1 = tk.Listbox(self.root,bg="#FDFFAE",fg="#4F6F52",font = ("Comic Sans MS",10,"bold"),bd=0)
        self.lb1.place(relx = 0.05, rely = 0.4,width=400,height=300)

        self.root.mainloop()

    def add(self):
        a = self.e1.get()
        self.lb1.insert(tk.END, a)
        self.e1.delete(1.0,tk.END)

    def remove(self):
        b = self.lb1.curselection()
        self.lb1.delete(b)
        
        



        





g1 = GUI()