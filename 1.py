import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time


placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()
#arduino con analog_0 quemado

a0 = placa.get_pin('a:1:i')
a1 = placa.get_pin('a:2:i')
a2 = placa.get_pin('a:3:i')

time.sleep(0.5)

ventana = Tk()
ventana.geometry('1080x800')
ventana.title("PUNTO 1")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('lave/lave.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-8fa09.firebaseio.com/'
})


marco1 = Frame(ventana, bg="lightskyblue4", highlightthickness=1, width=1280, height=800, bd= 5)
marco1.place(x = 0,y = 0)

frame1 = Frame(marco1, bg="darkolivegreen4", highlightthickness=1, width=500, height=500, bd= 5)
frame1.place(x = 15,y = 15)


label1= Label(frame1, bg='light cyan', font=("times", 15), fg="lightyellow4", width=5)
info1=StringVar()
label1.configure(textvariable=info1)
label1.place(x=20,y=30)

label2= Label(frame1, bg='light cyan', font=("times", 15), fg="lightyellow4", width=5)
label2.place(x=20,y=70)
info2=StringVar()
label2.configure(textvariable=info2)

label3= Label(frame1, bg='light cyan', font=("times", 15), fg="lightyellow4", width=5)
label3.place(x=20,y=110)
info3=StringVar()
label3.configure(textvariable=info3)
   
def adc_read():
        x=a0.read()
        print(x)
        
      
        info1.set(x)
        ventana.update()
        time.sleep(0.1)

        ref = db.reference('sensor')
        ref.update({
            'sensor 1': x
        })
def adc_read2():
   

        x=a1.read()
        print(x)
        
 
        info2.set(x)
        ventana.update()
        time.sleep(0.1)

        ref = db.reference('sensor')
        ref.update({
            'sensor 2': x
        })

def adc_read3():
    

        x=a2.read()
        print(x)
        
       
        info3.set(x)
        ventana.update()
        time.sleep(0.1)

        ref = db.reference('sensor')
        ref.update({
            'sensor 3': x
        })


prom_15=Button(marco1,text="SENSOR 1",command=adc_read)
prom_15.place(x=130, y=50)

save_button=Button(marco1,text="SENSOR 2",command=adc_read2)
save_button.place(x=130, y=90)

save_button=Button(marco1,text="SENSOR 3",command=adc_read3)
save_button.place(x=130, y=130)    
    
ventana.mainloop()
