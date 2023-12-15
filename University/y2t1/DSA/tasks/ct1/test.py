from customtkinter import *

app = CTk()
app.title("Data Structures and Algorithms")
app.geometry("700x400")
app.resizable(False, False)

checkBox = CTkCheckBox(
    app,
    text="Yes",
    onvalue=1,
    offvalue=0,
    command=lambda: print(checkBox.get()),
)
checkBox.pack()

app.mainloop()
