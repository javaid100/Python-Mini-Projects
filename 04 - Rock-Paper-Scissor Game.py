# ======== Rock-Paper-Scissor Game =============

# Import Useful Library
from tkinter import *
import random


# Initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)      # Used for expanding the window if (1,1)
root.title('Rock-Paper-Scissor')
root.config(bg ='seashell3')


# Computer Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissor'


# User Choice
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissor' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)


# Play Function
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie - you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose - computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissor':
        Result.set('you win - computer select scissor')
    elif user_pick == 'paper' and comp_pick == 'scissor':
        Result.set('you loose - computer select scissor')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win - computer select rock')
    elif user_pick == 'scissor' and comp_pick == 'rock':
        Result.set('you loose - computer select rock')
    elif user_pick == 'scissor' and comp_pick == 'paper':
        Result.set('you win - computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissor')

# Used to accept single-line text From Play function
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)


# Reset and Exit Functions
def Reset():
    Result.set("") 
    user_take.set("")

def Exit():
    root.destroy()


# Label and Buttons
Label(root, text = 'Rock, Paper, Scissor' , font='arial 20 bold', bg = 'seashell2').pack()

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


# Execute the Window
root.mainloop()