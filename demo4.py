from tkinter import *

class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.title("Calculator")

        self['padx'] = 10
        self['pady'] = 10

        Label(self, text='I\'m a calculator!').grid(row=0, column=0, columnspan=2, sticky=E+W, pady=5)

        number_width = op_width = 4
        number_height = op_height = 2

        self.operators = ['/', '*', '-', '+']

        self.create_numbers(self, number_width, number_height).grid(row=1, column=0, padx=5, pady=5)
        self.create_operators(self, op_width, op_height).grid(row=1, column=1, padx=5, pady=5)

        Button(self, text='=', height=op_height, command=lambda: self.on_button('='))\
            .grid(row=2, column=0, columnspan=2, sticky=E+W, padx=5)

        self.grid(row=0, column=0, sticky=N+E+S+W)

        self.bind('<Key>', lambda event: self.on_button(event.char))
        self.bind('<Return>', lambda event: self.on_button('='))
        # So we get keyboard events
        self.focus_set()

    def create_numbers(self, parent, w, h):
        frame_numbers = Frame(parent)

        self.buttons_numbers = dict()

        for i in range(3):
            for j in range(3):
                n = 3*i + j + 1
                self.buttons_numbers[n] = Button(frame_numbers,
                                                 text='%i' % n,
                                                 width=w, height=h,
                                                 command=lambda x=n: self.on_button(x)
                )
                self.buttons_numbers[n].grid(row=2-i, column=j)

        self.buttons_numbers[0] = Button(frame_numbers, text='0', width=w, height=h, command=lambda: self.on_button(0))
        self.buttons_numbers[0].grid(row=3, column=0, columnspan=2, sticky=E+W)

        self.buttons_numbers['.'] = Button(frame_numbers, text='.', width=w, height=h, command=lambda: self.on_button('.'))
        self.buttons_numbers['.'].grid(row=3, column=2)

        return frame_numbers

    def create_operators(self, parent, w, h):
        frame_operators = Frame(parent)

        self.buttons_ops = dict()

        r = 0
        for o in self.operators:
            self.buttons_numbers[o] = Button(frame_operators, text=o, width=w, height=h, command=lambda x=o: self.on_button(x))
            self.buttons_numbers[o].grid(row=r, column=0)
            r += 1

        return frame_operators

    def on_button(self, n):
        print('on_button called with argument \'%s\'.' % str(n))

def main():
    root = Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
