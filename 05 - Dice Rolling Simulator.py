# ======= Dice Rolling Simulator =========

# Import Useful Libraries
from tkinter import *
from PIL import Image, ImageTk
import random


# Initialize the window and add label in it
root = Tk()
root.geometry('400x400')
root.title('Roll the Dice')

# Adding label
Label(root, text="Hello!", fg = "light green", bg = "dark green", font = "Helvetica 16 bold italic").pack(pady=20)


# Dice Images
path = 'E:/WORK/PYTHON/01 - Basic Python Projects/05 - Dice Rolling Simulator/'
d1 = path + 'dice1.png'
d2 = path + 'dice2.png'
d3 = path + 'dice3.png'
d4 = path + 'dice4.png'
d5 = path + 'dice5.png'
d6 = path + 'dice6.png'

dice = [d1, d2, d3, d4, d5, d6]


# Simulating the dice with random numbers between 0 to 5 and Generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = Label(root, image=image1)

# Function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

label1.pack(expand=True)


# Adding button in which command will use rolling_dice function
Button(root, text='Roll the Dice', fg='blue', command=rolling_dice).pack(pady=20)


# Execute the Window
root.mainloop()