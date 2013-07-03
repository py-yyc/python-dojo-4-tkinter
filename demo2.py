from tkinter import *

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.title("Calculator")

        Label(self, text='I\'m a calculator!').grid(row=0, column=0, columnspan=2, sticky=E+W, pady=5)

        self.grid(row=0, column=0, sticky=N+E+S+W)

def main():
    root = Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
