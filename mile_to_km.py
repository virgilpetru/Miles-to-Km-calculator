#       Entry    label
# label  label   label
#        button

from tkinter import *

def button_click():
    new_text = input.get()
    sum = int(new_text) * 1.60934
    sum = round(sum, 2)
    label_sum.config(text=sum)


window =Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)

input = Entry(width=10)
input.get()
input.grid(column=2, row=2)

empty_label = Label(text="")
empty_label.grid(column=1, row=0)
empty_label.config(padx=40, pady=5)

label_miles = Label(text="Miles", font=("Arial", 24, "bold"))
label_miles.grid(column=3, row=2)

label_equal = Label(text="is equal to", font=("Arial", 24,"bold"))
label_equal.grid(column=1, row=3)

label_sum = Label(text="input", font=("Arial", 24,"bold"))
label_sum.grid(column=2, row=3)

label_km = Label(text="Km", font=("Arial", 24,"bold"))
label_km.grid(column=3, row=3)

button = Button(text="Calculate", command=button_click)
button.grid(column=2, row=5)






window.mainloop()