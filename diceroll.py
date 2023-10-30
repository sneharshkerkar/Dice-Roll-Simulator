import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

dice = ["C:/Users/User/Documents/python project/dice_simulator/dice1.png","C:/Users/User/Documents/python project/dice_simulator/dice2.png","C:/Users/User/Documents/python project/dice_simulator/dice3.png","C:/Users/User/Documents/python project/dice_simulator/dice4.png","C:/Users/User/Documents/python project/dice_simulator/dice5.png","C:/Users/User/Documents/python project/dice_simulator/dice6.png"]
Image1=ImageTk.PhotoImage(Image.open( random.choice(dice)))
Image2=ImageTk.PhotoImage(Image.open( random.choice(dice)))

label1 =tk.Label(window,image=Image1)
label2 =tk.Label(window,image=Image2)

label1.image =Image1
label2.image =Image2

label1.place(x=100,y=100)
label2.place(x=700,y=100)

def dice_roll():
    Image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=Image1)
    label1.image = Image1

    Image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=Image2)
    label2.image = Image2

    
button = tk.Button(window,text="ROLL",bg = "green", fg="white",font="Times 20 bold",command=dice_roll)
button.place(x=600, y=20)

window.mainloop()





