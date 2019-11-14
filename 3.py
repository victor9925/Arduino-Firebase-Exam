from pyfirmata import Arduino, util
from tkinter import *
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()

x=0
led1= placa.get_pin('d:8:o') 
led2= placa.get_pin('d:9:o') 
led3= placa.get_pin('d:10:o') 
led4= placa.get_pin('d:11:o') 
led5= placa.get_pin('d:12:o') 
led6= placa.get_pin('d:13:o') 

ventana = Tk()
ventana.geometry('850x850')
ventana.configure(bg = 'white')
ventana.title("Bienvenidos a las UI")
texto = Label(ventana, text="OPERADOR LED", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
texto.place(x=110, y=20)


def entrada(input):

    content = dato.get()
    
    dato.delete(0, END)
    
    if int(content)in range(8,13):
        led1.write(1)
        time.sleep(1)
        x=content
    else:
        ventana1 = Tk()
        ventana1.geometry('220x40')
        ventana1.configure(bg = 'RED')
        ventana1.title("Bienvenidos a las UI")
        texto1 = Label(ventana1, text="NUMERO INCORRECTO", bg='RED', font=("Arial Bold", 14), fg="white")
        texto1.place(x=0, y=0)

def on(input):
    if content == 

Label(ventana, text="NUMERO LED: ").place(x=20, y=60)
dato = Entry(ventana)
dato.place(x=100, y=60)
dato.bind('<Return>', entrada) 

Label1(ventana, text="ON or OFF").place(x=20, y=120)
dato2 = Entry(ventana)
dato2.place(x=100, y=120)
dato.bind('<Return>', on) 

ventana.mainloop()
