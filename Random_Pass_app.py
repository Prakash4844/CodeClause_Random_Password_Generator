import customtkinter as ctk
from password_generator import PasswordGenerator
MIN_UPPER = 0
MIN_LOWER = 0
MIN_NUM = 0
MIN_SYM = 0


def generate_password(pass_length, include_num=True, include_sym=True):

    section = int(pass_length)//4

    pwo = PasswordGenerator()
    # All properties are optional
    pwo.minlen = int(pass_length)
    pwo.maxlen = int(pass_length)

    if not include_num:
        pwo.minnumbers = 0

    if not include_sym:
        pwo.minsymbols = 0


    password = pwo.generate()
    print(password)
    return password


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("green")
        self.title("Password Generator")
        self.geometry("900x300")
        self.resizable(False, False)
        generate_password(10)

    def exit(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()