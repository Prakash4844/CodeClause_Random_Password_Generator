import tkinter as tk
import customtkinter as ctk
from Random_Pass_app import App, generate_password
import pyperclip

app = App()  # create CTk window like you do with the Tk window

# create a label
label = ctk.CTkLabel(app, text="Generated Password")
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# create a text box
text_box = ctk.CTkTextbox(app, width=700, height=50)
text_box.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
Include_Numbers = True
Include_Symbols = True


# create a buttonGenerate
def generate_function():
    text_box.configure(state="normal")
    text_box.delete("0.0", tk.END)
    Nums = submit_function()[0]
    Syms = submit_function()[1]
    password = generate_password(pass_length_slider.get(), num=Nums,
                                 sym=Syms)
    # print(password)
    if len(password) > 36:
        text_box.configure(font=("Liberation Mono", 25))
    else:
        text_box.configure(font=("Liberation Mono", 30))
    text_box.insert("0.0", password)
    text_box.configure(state="disabled")
    text_box.update()


def copy_fuction():
    copytext = text_box.get("0.0", tk.END)
    pyperclip.copy(copytext)


buttonCopy = ctk.CTkButton(app, text="Copy", command=copy_fuction, height=50, width=30)
buttonCopy.place(relx=0.90, rely=0.25, anchor=tk.CENTER)

buttonGenerate = ctk.CTkButton(app, text="Generate Password", command=generate_function, height=30, width=30
                                , font=("Noto Sans", 15))
buttonGenerate.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

buttonExit = ctk.CTkButton(app, text="Quit", command=app.exit, height=30, width=150, font=("Noto Sans", 15))

buttonExit.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

# create a label
Numlabel = ctk.CTkLabel(app, text="Minimum Numbers in Password")
Numlabel.place(relx=0.15, rely=0.7, anchor=tk.CENTER)
Num_entry = ctk.CTkEntry(app, width=50, placeholder_text="3")
Num_entry.place(relx=0.15, rely=0.8, anchor=tk.CENTER)

# create a label
Symlabel = ctk.CTkLabel(app, text="Minimum Symbols in Password")
Symlabel.place(relx=0.45, rely=0.7, anchor=tk.CENTER)
Sym_entry = ctk.CTkEntry(app, width=50, placeholder_text="3")
Sym_entry.place(relx=0.45, rely=0.8, anchor=tk.CENTER)


def submit_function():
    Nums = Num_entry.get()
    Syms = Sym_entry.get()
    print(Sym_entry.get())
    print(Num_entry.get())
    return [Nums, Syms]


def pass_length_slider_event(value):
    print(round(value))
    pass_length_slider_label.configure(text=f"Password Length = {round(value)}")
    pass_length_slider_label.update()
    return round(value)


pass_length_slider = ctk.CTkSlider(app, from_=8, to=64, command=pass_length_slider_event, width=300)
pass_length_slider.place(relx=0.8, rely=0.8, anchor=tk.CENTER)
pass_length_slider.set(12)
pass_length_slider_label = ctk.CTkLabel(app, bg_color="transparent", text=f"Password Length = 12")
pass_length_slider_label.place(relx=0.8, rely=0.7, anchor=tk.CENTER)
pass_length_slider_label.update()

app.mainloop()
