from tkinter import *



windows = Tk()
windows.minsize(width=300,height=500)
windows.title("Miles to Kilometer")
windows.config(padx = 20, pady = 20)



input = Entry(width = 20)
input.grid(column = 1,row =0)
# input.config(padx = 10, pady =10)

miles = Label(text = "MILES" ,font =("Arial",24))
miles.grid(column = 2, row =0)
miles.config(padx = 10,pady = 10)



def converter():
      change = int(round(float(input.get()) *1.60934))
      blank_text.config(text = change)


guide = Label(text = "is equal to", font = ("Arial",24))
guide.grid(row = 1, column =0)
# guide.config(padx = 10, pady = 10)

blank_text = Label(text = "", font = ("Arial",24))
blank_text.grid(row = 1,column =1)
# blank_text.config(padx = 10,pady =10)

mile = Label(text = "KM",font =("Arial",24))
mile.grid(row = 1 ,column = 2)
# mile.config(padx = 10,pady =10)

button = Button(text= "CONVERT",command =converter)
button.grid(row = 3 ,column =1)
button.config(padx = 10, pady = 10)


windows.mainloop()