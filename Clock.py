from tkinter import *
import time

def times():
    # curent_time = time.strftime("%I:%M:%S")   Todo : for 12 hour
    curent_time = time.strftime("%I:%M:%S")
    clock.config(text=curent_time)
    clock.after(200,times)

root = Tk()
root.geometry( "500x250" )
root.resizable(0,0)
# root.wm_iconbitmap("clock.ico")
root.title("Digital Clock")
clock = Label(root,font=("times" , 50 , "bold"), bg = "black" , fg = "white")
clock.grid(row = 2 , column = 2, pady = 25 , padx = 100)
times()

digi = Label(root,text = "Digital Clock" , font="times 24 bold")
digi.grid(row=0,column= 2)
nota = Label(root,text="Hour    Minutes     Second  ", font = "times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()
