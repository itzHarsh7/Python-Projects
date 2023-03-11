import os
from tkinter import *


def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")



st = Tk()    # st is object of class Tkinter
st.title("Shut Down App")
st.geometry("500x500")    # Frame of our app
st.config(bg = "blue")  # config means background color

r_button = Button(st, text="Restart", font=("Time New Roman", 30, "bold"), relief=RAISED, cursor="plus", command= restart())
r_button.place(x=100, y=20, height = 80, width= 200)

rt_button = Button(st, text="Restart Time", font=("Time New Roman", 30, "bold"), relief=RAISED, cursor="plus", command = restart_time())
rt_button.place(x=100, y=140, height = 80, width= 250)

lg_button = Button(st, text="Log Out", font=("Time New Roman", 30, "bold"), relief=RAISED, cursor="plus", command= logout())
lg_button.place(x=100, y=260, height = 80, width= 200)

sd_button = Button(st, text="Shut Down", font=("Time New Roman", 30, "bold"), relief=RAISED, cursor="plus", command= shutdown())
sd_button.place(x=100, y=380, height = 80, width= 220)


st.mainloop()
