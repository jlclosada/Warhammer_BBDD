from tkinter import *
from tkinter import ttk, filedialog, messagebox
from client.gui import Frame, barra_menu

def main():
    root = Tk()
    root.title("Warhammer DB")
    root.resizable(0, 0)

    barra_menu(root)

    app = Frame(root = root)



    app.mainloop()


if __name__ == '__main__':
    main()

