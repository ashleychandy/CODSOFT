import tkinter as tk
import math

class calc:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("300x500")
        self.root.title("Calculator")
        self.root.configure(bg="#D2E3C8")

        self.bc = "#B2C8BA"

        self.e1 = tk.Entry(self.root,bg="#D2E3C8",fg="black",bd=0,font=("Sans serif",40,"bold"),justify="right",width=10)
        self.e1.place(relx=0.02,rely=0.3)

        self.b21 = tk.Button(self.root,text="C",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=self.clear)
        self.b21.place(relx=0.01,rely=0.46)
        self.b22 = tk.Button(self.root,text="√",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=self.sqrt)
        self.b22.place(relx=0.26,rely=0.46)
        self.b23 = tk.Button(self.root,text="/",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num("/"))
        self.b23.place(relx=0.51,rely=0.46)
        self.b24 = tk.Button(self.root,text="<-",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=self.remove)
        self.b24.place(relx=0.76,rely=0.46)

        self.b31 = tk.Button(self.root,text="7",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(7))
        self.b31.place(relx=0.01,rely=0.56)
        self.b32 = tk.Button(self.root,text="8",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(8))
        self.b32.place(relx=0.26,rely=0.56)
        self.b33 = tk.Button(self.root,text="9",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(9))
        self.b33.place(relx=0.51,rely=0.56)
        self.b34 = tk.Button(self.root,text="x",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num("*"))
        self.b34.place(relx=0.76,rely=0.56)

        self.b41 = tk.Button(self.root,text="4",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(4))
        self.b41.place(relx=0.01,rely=0.66)
        self.b42 = tk.Button(self.root,text="5",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(5))
        self.b42.place(relx=0.26,rely=0.66)
        self.b43 = tk.Button(self.root,text="6",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(6))
        self.b43.place(relx=0.51,rely=0.66)
        self.b44 = tk.Button(self.root,text="-",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num("-"))
        self.b44.place(relx=0.76,rely=0.66)        
        
        self.b51 = tk.Button(self.root,text="1",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(1))
        self.b51.place(relx=0.01,rely=0.76)
        self.b52 = tk.Button(self.root,text="2",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(2))
        self.b52.place(relx=0.26,rely=0.76)
        self.b53 = tk.Button(self.root,text="3",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(3))
        self.b53.place(relx=0.51,rely=0.76)
        self.b54 = tk.Button(self.root,text="+",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num("+"))
        self.b54.place(relx=0.76,rely=0.76)

        self.b11 = tk.Button(self.root,text="!",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=self.fact)
        self.b11.place(relx=0.01,rely=0.86)
        self.b12 = tk.Button(self.root,text="0",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num(0))
        self.b12.place(relx=0.26,rely=0.86)
        self.b13 = tk.Button(self.root,text=".",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=lambda:self.num("."))
        self.b13.place(relx=0.51,rely=0.86)
        self.b14 = tk.Button(self.root,text="=",bg=self.bc,bd=0,font=("times roman",16,"bold"),width=4,command=self.sol)
        self.b14.place(relx=0.76,rely=0.86)

        self.root.mainloop()

    def num(self,i):
        if i==1:
            self.e1.insert(tk.END,"1")
        elif i==2:
            self.e1.insert(tk.END,"2")
        elif i==3:
            self.e1.insert(tk.END,"3")
        elif i==4:
            self.e1.insert(tk.END,"4")
        elif i==5:
            self.e1.insert(tk.END,"5")
        elif i==6:
            self.e1.insert(tk.END,"6")
        elif i==7:
            self.e1.insert(tk.END,"7")
        elif i==8:
            self.e1.insert(tk.END,"8")
        elif i==9:
            self.e1.insert(tk.END,"9")
        elif i==0:
            self.e1.insert(tk.END,"0")
        elif i == "+":
            self.e1.insert(tk.END,"+")
        elif i == "-":
            self.e1.insert(tk.END,"-")
        elif i == "*":
            self.e1.insert(tk.END,"*")
        elif i == "/":
            self.e1.insert(tk.END,"/")
        elif i == ".":
            self.e1.insert(tk.END,".")
                    
    def sol(self):
        try:

                self.ans = eval(self.e1.get())
                self.e1.delete(0,tk.END)
                self.e1.insert(0,str(self.ans))
        except Exception as e:
                self.e1.delete(0,tk.END)
                self.e1.insert(0,"invalid input")
        
    def clear(self):
        self.e1.delete(0,tk.END)   

    def remove(self):
        self.a = self.e1.get()
        self.a = self.a[:-1]
        self.e1.delete(0,tk.END)
        self.e1.insert(0,self.a)
     
    def sqrt(self):
        self.ans = self.e1.get()
        self.a= float(self.ans)
        self.sq= math.sqrt(self.a)
        self.e1.delete(0,tk.END)
        self.e1.insert(0,str(self.sq))

    def fact(self):
        self.ans = self.e1.get()
        self.a= int(self.ans)
        self.sq= math.factorial(self.a)
        self.e1.delete(0,tk.END)
        self.e1.insert(0,str(self.sq))
        

c1 = calc()