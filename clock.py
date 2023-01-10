from tkinter import *
import datetime
import time
from playsound import playsound
from threading import *

 
obj = Tk()
obj.title("Python Alarm clock")
 
#now here we are Setting the geometry 
obj.geometry("500x300")

def Threading():
    
    t1=Thread(target=alarm) 
    t1.start()
 
def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    while True:
       
         
    
        time.sleep(1)
 
    #here input the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 #check the condition
        if current_time == set_alarm_time:
            print("Time to Wake up!!")
            playsound('C:\\Users\\Prathmesh\\Desktop\\prj\\a.mp3')
            minu=int(minute.get())
            if minu+3>=60:
                minu=int(minute.get())+(int(minute.get())%60)
                hor=(int(hour.get())+1)%24
                set_alarm_time= f"{hor}:{minu}:{second.get()}"
            else:
                minu=int(minute.get())+3
                set_alarm_time= f"{hour.get()}:{minu}:{second.get()}"
                
            
 
# creating GUI for the clock i.e Add Labels, Frame, Button, Optionmenus
Label(obj,text="ALARM CLOCK",font=("comic sans",20),fg="Blue").pack(pady=10)       
Label(obj,text="Input Time",font=("comic sans",15),fg="purple").pack()
 
frame = Frame(obj)
frame.pack()
 
hour = StringVar(obj)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(obj)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(obj)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
 
Button(obj,text="Set Alarm",font=("comic sans",15),command=Threading).pack(pady=20)
 

obj.mainloop()

