from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady= 50)

def miles_to_kms():
    miles = float(miles_input.get())
    kms = round(miles * 1.609)
    my_label4.config(text=f"{kms}")


#Entry
miles_input = Entry(width=10)
miles_input.grid(column=3, row=1)

#Label
my_label1 = Label(text="is equal to")
my_label1.grid(column =0, row=2)

my_label2 = Label(text="Miles")
my_label2.grid(column =4, row=1)

my_label3 = Label(text="Km")
my_label3.grid(column =4, row=2)

my_label4 = Label(text="0")
my_label4.grid(column =3, row=2)

button1 = Button(text="Calculate", command=miles_to_kms)
button1.grid(column=3, row=4)







window.mainloop()
