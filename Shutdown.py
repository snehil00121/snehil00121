from tkinter import*
import os

def restart():
    os.system("ShutDown /r /t 1")

def restart_time():
    os.system("shutDown /r /t 20")

def Log_out():
    os.system("shutDown -l")

def Shut_down():
    os.system("shutDown /s /t 20")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Skyblue")

#RESTART
r_button = Button(st, text="Restart",font=("Time New Roman", 30, "bold"),relief=RAISED,cursor="plus", command=restart)
r_button.place(x=150,y=60,height=50,width=200)

#RESTART TIME
rt_button = Button(st, text="Restart Time",font=("Time New Roman", 20, "bold"),relief=RAISED,cursor="plus", command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

#LOG OUT
lg_button = Button(st, text="Log Out",font=("Time New Roman", 20, "bold"),relief=RAISED,cursor="plus", command=Log_out)
lg_button.place(x=150,y=280,height=50,width=200)

#SHUT DOWN
st_button = Button(st, text="Shut Down",font=("Time New Roman", 20, "bold"),relief=RAISED,cursor="plus",command=Shut_down)
st_button.place(x=150,y=390,height=50,width=200)


st.mainloop()