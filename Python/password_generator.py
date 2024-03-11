import secrets
import tkinter as tk


class PG:
    def __init__(self):

        self.root =  tk.Tk()
        self.root.geometry("300x500")
        self.root.configure(bg="lightgrey")
        self.root.resizable(False,False)
        
        self.l1=tk.Label(self.root,text="Password Generator",bg="lightgrey",fg="#8E7AB5",font=("Sans Serif",15,"bold"))
        self.l1.place(relx=0.18,rely=0.05)
        self.l2=tk.Label(self.root,text="Username:",fg="#8E7AB5",font=("Sans Serif",15,"bold"),bg="lightgrey")
        self.l2.place(relx=0.05,rely=0.2)
        self.l3=tk.Label(self.root,text="Password Length:",fg="#8E7AB5",font=("Sans Serif",15,"bold"),bg="lightgrey")
        self.l3.place(relx=0.05,rely=0.4)
        self.l4=tk.Label(self.root,text="Generated Password:",fg="#8E7AB5",font=("Sans Serif",15,"bold"),bg="lightgrey")
        self.l4.place(relx=0.05,rely=0.6)

        self.e1=tk.Entry(self.root,font=("Sans Serif",10,"bold"))
        self.e1.place(relx=0.05,rely=0.28)
        self.e2=tk.Entry(self.root,font=("Sans Serif",10,"bold"))
        self.e2.place(relx=0.05,rely=0.48)
        self.e3=tk.Entry(self.root,font=("Sans Serif",10,"bold"))
        self.e3.place(relx=0.05,rely=0.68)

        self.b1=tk.Button(self.root,text="Generate Password",bg="#8E7AB5",fg="white",font=("Sans Serif",12,"bold"),command=self.genpass)
        self.b1.place(relx=0.05,rely=0.8)

        self.b2=tk.Button(self.root,text="Reset",bg="#8E7AB5",fg="white",command=self.clear,font=("Sans Serif",13,"bold"))
        self.b2.place(relx=0.7,rely=0.8)       
         
        self.root.mainloop()

    def genpass(self):

        self.a = int(self.e2.get())
        self.e3.delete(0,tk.END)
        self.b = secrets.token_urlsafe(self.a)
        self.b=self.b[:self.a]
        self.e3.insert(0,self.b)


    def clear(self):
        self.e3.delete(0,tk.END)
        self.e2.delete(0,tk.END)



pg1 = PG()