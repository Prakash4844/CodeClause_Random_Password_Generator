import tkinter as tk
import customtkinter as ctk
from Random_Pass_app import App, generate_password

app = App()  # create CTk window like you do with the Tk window

# create a label
label = ctk.CTkLabel(app, text="Generated Password")
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# create a text box
text_box = ctk.CTkTextbox(app, width=800, height=50)
text_box.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
Include_Numbers = True
Include_Symbols = True


def checkbox_eventA_Z():
    pass


check_varA_Z = ctk.StringVar(app, "on")
print(check_varA_Z)
checkboxA_Z = ctk.CTkCheckBox(app, text="A-Z", command=checkbox_eventA_Z,
                              variable=check_varA_Z, onvalue="on", offvalue="off", state="disabled")
checkboxA_Z.place(relx=0.05, rely=0.7)


def checkbox_eventa_z():
    pass


check_vara_z = ctk.StringVar(app, "on")
checkboxa_z = ctk.CTkCheckBox(app, text="a-z", command=checkbox_eventa_z,
                              variable=check_vara_z, onvalue="on", offvalue="off", state="disabled")
checkboxa_z.place(relx=0.2, rely=0.7)


def checkbox_event_num():
    state = checkbox_num.get()
    if state == "on":
        Include_Numbers = True
    else:
        Include_Numbers = False
        print("exluded numbers")


check_var_num = ctk.StringVar(app, "on")
checkbox_num = ctk.CTkCheckBox(app, text="Numbers", command=checkbox_event_num,
                               variable=check_var_num, onvalue="on", offvalue="off")
checkbox_num.place(relx=0.05, rely=0.8)

def checkbox_event_symbol():
    state = checkbox_num.get()
    if state == "on":
        Include_Symbols = True
    else:
        Include_Symbols = False
        print("exluded symbols")


check_var_symbol = ctk.StringVar(app, "on")
checkbox_symbol = ctk.CTkCheckBox(app, text="Symbols", command=checkbox_event_symbol(),
                                  variable=check_var_symbol, onvalue="on", offvalue="off")
checkbox_symbol.place(relx=0.2, rely=0.8)

# create a buttonGenerate
def button_function():
    text_box.configure(state="normal")
    text_box.delete("0.0", tk.END)
    password = generate_password(pass_length_slider.get(), include_num=Include_Numbers,
                                 include_sym=Include_Symbols)
    print(password)
    if len(password) > 36:
        text_box.configure(font=("Liberation Mono", 25))
    else:
        text_box.configure(font=("Liberation Mono", 35))
    text_box.insert("0.0", password)
    text_box.configure(state="disabled")
    text_box.update()


buttonGenerate = ctk.CTkButton(app, text="Generate Password", command=button_function)
buttonGenerate.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

buttonExit = ctk.CTkButton(app, text="Quit", command=app.exit)

buttonExit.place(relx=0.7, rely=0.5, anchor=tk.CENTER)


def pass_length_slider_event(value):
    print(round(value))
    pass_length_slider_label.configure(text=f"Password Length = {round(value)}")
    pass_length_slider_label.update()
    return round(value)


pass_length_slider = ctk.CTkSlider(app, from_=8, to=64, command=pass_length_slider_event)
pass_length_slider.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
pass_length_slider.set(12)
pass_length_slider_label = ctk.CTkLabel(app, bg_color="transparent", text=f"Password Length = 12")
pass_length_slider_label.place(relx=0.5, rely=0.82, anchor=tk.CENTER)
pass_length_slider_label.update()

app.mainloop()
