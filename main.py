from tkinter import *
from tkinter import messagebox

w = Tk()
w.geometry('350x500')
w.title('User Login')
w.resizable(0,0)

j=0
r=0
for i in range(100):
    Frame(w,width=10,height=500,bg='#11999E').place(x=j,y=0)
    j=j+10
    r=r+1

Frame(w,width=250,height=400,bg='white').place(x=50,y=50)

#Label
label1=Label(w,text='Username',bg='white')
l=('consolas',14)
label1.config(font=1)
label1.place(x=80,y=200)

entry1=Entry(w,width=18,border=0)
entry1.config(font=1)
entry1.place(x=80,y=230)

#Label2
label2=Label(w,text='Password',bg='white')
l=('consolas',14)
label2.config(font=1)
label2.place(x=80,y=280)

entry2=Entry(w,width=18,border=0)
entry2.config(font=1)
entry2.place(x=80,y=310)

Frame(w,width=180,height=2,bg="#141414").place(x=80,y=250)
Frame(w,width=180,height=2,bg="#141414").place(x=80,y=328)

from PIL import ImageTk,Image

image1=Image.open("---Image Path---").resize((121,120))
image2=ImageTk.PhotoImage(image1)


Label3=Label(image=image2,border=0,justify=CENTER)
Label3.place(x=115,y=50)

def cmd():
    if entry1.get()=='programmed' and entry2.get()=='programmed':
        messagebox.showinfo("Login Successful","     Welcome!    ")
        q=Tk()
        q.mainloop()
    else:
        messagebox.showwarning("Login failed","     Try Again     ")

def bttn(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor 
        myButton1['foreground']= lcolor 

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text=text,
                   width=20,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=cmd)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)


bttn(100,375,'L O G I N','white','#FF2E63')
w.mainloop()