# ====== ALARM CLOCK =============

# Import Useful Libraries
from tkinter import *
from threading import *
import datetime
import time
import winsound


# Variables of Hours, Minutes & Seconds
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', 
         '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23', '24')

minutes = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')

seconds = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60')


# Make Tkinter Object and add Frame in it
root = Tk()
root.geometry("400x200")
root.title('Alarm Clock') 

frame = Frame(root)
frame.pack()


# Add Option-menus in the Frame
hour = StringVar(root)
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)    
      
second = StringVar(root)
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)


# Add Labels
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=20)   


# Create Button
def Threading():
    t1=Thread(target=alarm)
    t1.start()
Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=10)


# Alarm Function
def alarm():
    # Infintite Loop
    while True:
        # Set Alarm time
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
  
        # Wait for one seconds
        time.sleep(1)
  
        # Get Current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
  
        # Check whether set alarm time is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break


# Execute Tkinter
root.mainloop()