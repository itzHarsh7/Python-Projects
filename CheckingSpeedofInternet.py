from tkinter import *
import speedtest
sp = Tk()  # sp is a object of class Tk and Tk is class in Tkinter Module

# Tkinter used to make GUI for our app like interface
sp.title("Internet Speed Test")  #giving title for our app
sp.geometry('500x500')  #dimensions for app
sp.config(bg = "Navy")  # config is uded to provide shape, color font etc to our app

def speedcheck():      
    sp = speedtest.Speedtest()   #creating a object for Speedtest class
    sp.get_servers()   # used to get server connection for checking speed
    down = str(round(sp.download()/(10**6),3))+ "Mbps"  # download will give downloading speed in bytes. we have dibided it by 10^6 because we want our speed in Mbps and in 3 digit number
    up = str(round(sp.upload()/(10**6),3))+ "Mbps"
    lab_down.config(text=down) #it will be displayed in 00
    lab_up.config(text=up) # it will be displaced in 00



lab = Label(sp,text="Internet Speed Test", font=("Time New Roman", 30,"bold"), bg = "navy", fg = "yellow")
lab.place(x=60, y=40, height=30, width=380)
'''
Label function is in Tkinter Module which helps in making a text in our app
sp is object in which in which it will label
text = used to display the text in app
font= text style, size, format(bold, italic, underlined)
bg = background of text
fg = text color. fg=forground

placefunction is used to place our text in that particular dimension
'''

lab = Label(sp,text="Download Speed", font=("Time New Roman", 30,"bold"), bg = "navy", fg = "red")
lab.place(x=60, y=100, height=30, width=380)

lab_down = Label(sp,text="00", font=("Time New Roman", 30,"bold"), bg = "navy", fg = "yellow")
lab_down.place(x=60, y=160, height=30, width=380)

lab = Label(sp,text="Upload Speed", font=("Time New Roman", 30,"bold"), bg = "navy", fg = "yellow")
lab.place(x=60, y=220, height=30, width=380)

lab_up = Label(sp,text="00", font=("Time New Roman", 30,"bold"), bg = "navy", fg = "yellow")
lab_up.place(x=60, y=280, height=30, width=380)

button = Button(sp, text="Check Speed", font=("Time New Roman", 30, "bold"), relief=RAISED, bg = "red", command=speedcheck())
button.place(x=60, y=340, height=40, width=380)
'''
Button function will create a button. it is just same like the Label function.
it takes parameter command to perform its particular task
relief = RAISED means  text is raised a little bit.

'''

sp.mainloop()   # it will be called for infinitely as it makes our app works continuously