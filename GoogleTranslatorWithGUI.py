from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text = "type", src = "english", dest = "hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text = text1, src=src1, dest=dest1)
    return trans1.text


def data():
    s= comb_sor.get()
    d = comb_dest.get()
    mes = SOR_txt.get(1.0, END)
    textget = change(text = mes, src = s, dest =d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk() 
root.title("Translator") 
root.geometry('500x700') 
root.config(bg = "Navy")

lab_txt = Label(root, text = "Translator", font = ("Time New Roman", 40,"bold"), bg="yellow")
lab_txt.place(x=100,y=40,height=45,width = 300)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root, text = "Source Text", font = ("Time New Roman", 30,"bold"), bg="red")
lab_txt.place(x=100,y=110,height=45,width = 300)

SOR_txt= Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
SOR_txt.place(x=50,y=170,height=150, width=400)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value = list_text)
comb_sor.place(x=140, y=350, height=30, width=70)
comb_sor.set("english")


comb_dest = ttk.Combobox(frame, value = list_text)
comb_dest.place(x=290, y=350, height=30, width=70)
comb_dest.set("hindi")

vari = Label(root, text = "To", font = ("Time New Roman", 30,"bold"))
vari.place(x=230,y=350,height=35,width = 50)



button_change =Button(frame, text = "Translate", relief = RAISED, command=data)
button_change.place(x=215, y=420, height=50, width=70)


dest_txt = Text(frame, font =("Time New Roman", 20, "bold"),wrap = WORD)
dest_txt.place(x=10, y= 500, height = 150, width=480)


root.mainloop()