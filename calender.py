#import tkintrer
from tkinter import *
#import calender module
import calendar
#initializing tkinter
root=Tk()
#setting geometry of our GUI
root.geometry("700x700")
#setting title of our GUI
root.title("My Calender")
#year for which we want the calender to be show in our GUI
year = 2021
#storing 2021year calender data inside mycal
myCal=calendar.calendar(year)
#show calendar data using label widget
cal_year=Label(root,text=myCal,font="Consolas 10 bold")
#packing the label widget
cal_year.pack()
#running the program using in mainloop
root.mainloop()
