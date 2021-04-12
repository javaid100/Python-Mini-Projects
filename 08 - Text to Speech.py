# ============== Text to Speech =================

# Import Useful Libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound





# Initialize the window & add Heading and Label in it
root = Tk()
root.geometry('350x200')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('TEXT_TO_SPEECH')

Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)


# Create an Entry for text
Msg = StringVar()
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20, y=100)


# Create Buttons for Play, Exit & Reset
# Fuction for converting Text into Speech
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('E:/WORK\PYTHON/01 - Basic Python Projects/08 - Text to Speech/Speech.mp3')
    playsound('E:/WORK\PYTHON/01 - Basic Python Projects/08 - Text to Speech/Speech.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=50, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=125,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=200 , y =140)


# Execute the program
root.mainloop()

