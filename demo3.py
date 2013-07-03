from tkinter import *

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.title("Calculator")

        Label(self, text='I\'m a calculator!').grid(row=0, column=0, columnspan=2, sticky=E+W, pady=5)

        number_width = 4
        number_height = 2

        self.create_numbers(self, number_width, number_height).grid(row=1, column=0, padx=5, pady=5)
        self.grid(row=0, column=0, sticky=N+E+S+W)

    def create_numbers(self, parent, w, h):
        frame_numbers = Frame(parent)

        self.buttons_numbers = dict()

        for i in range(3):
            for j in range(3):
                n = 3*i + j + 1
                self.buttons_numbers[n] = Button(frame_numbers,
                                                 text='%i' % n,
                                                 width=w, height=h,
                                                 command=lambda: self.on_button(n)
                )
                self.buttons_numbers[n].grid(row=2-i, column=j)

        self.buttons_numbers[0] = Button(frame_numbers, text='0', width=w, height=h, command=lambda: self.on_button(0))
        self.buttons_numbers[0].grid(row=3, column=0, columnspan=2, sticky=E+W)

        self.buttons_numbers['.'] = Button(frame_numbers, text='.', width=w, height=h, command=lambda: self.on_button('.'))
        self.buttons_numbers['.'].grid(row=3, column=2)

        return frame_numbers

    def on_button(self, n):
        print('on_button called with \'%s\'' % str(n))

def main():
    root = Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
