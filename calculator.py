from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    window = Tk()

    window.title("Calculator")
    window.geometry("254x336")

    equation = StringVar()
    expression_field = Entry(window, width=8, fg='red', font='arial 13 bold', bg='black',
                             bd=20, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    button1 = Button(window, text=' 1 ', fg='red', bg='black',
                     command=lambda: press(1), height=3, width=7, font='arial 9 bold')
    button1.grid(row=2, column=0, sticky='nesw')

    button2 = Button(window, text=' 2 ', fg='red', bg='black',
                     command=lambda: press(2), height=3, width=7, font='arial 9 bold')
    button2.grid(row=2, column=1, sticky='nesw')

    button3 = Button(window, text=' 3 ', fg='red', bg='black',
                     command=lambda: press(3), height=3, width=7, font='arial 9 bold')
    button3.grid(row=2, column=2, sticky='nesw')

    button4 = Button(window, text=' 4 ', fg='red', bg='black',
                     command=lambda: press(4), height=3, width=7, font='arial 9 bold')
    button4.grid(row=3, column=0, sticky='nesw')

    button5 = Button(window, text=' 5 ', fg='red', bg='black',
                     command=lambda: press(5), height=3, width=7, font='arial 9 bold')
    button5.grid(row=3, column=1, sticky='nesw')

    button6 = Button(window, text=' 6 ', fg='red', bg='black',
                     command=lambda: press(6), height=3, width=7, font='arial 9 bold')
    button6.grid(row=3, column=2, sticky='nesw')

    button7 = Button(window, text=' 7 ', fg='red', bg='black',
                     command=lambda: press(7), height=3, width=7, font='arial 9 bold')
    button7.grid(row=4, column=0, sticky='nesw')

    button8 = Button(window, text=' 8 ', fg='red', bg='black',
                     command=lambda: press(8), height=3, width=7, font='arial 9 bold')
    button8.grid(row=4, column=1, sticky='nesw')

    button9 = Button(window, text=' 9 ', fg='red', bg='black',
                     command=lambda: press(9), height=3, width=7, font='arial 9 bold')
    button9.grid(row=4, column=2, sticky='nesw')

    button0 = Button(window, text=' 0 ', fg='red', bg='black',
                     command=lambda: press(0), height=3, width=7, font='arial 9 bold')
    button0.grid(row=5, column=1, sticky='nesw')

    plus = Button(window, text=' + ', fg='red', bg='black',
                  command=lambda: press("+"), height=3, width=7, font='arial 9 bold')
    plus.grid(row=2, column=3, sticky='nesw')

    minus = Button(window, text=' - ', fg='red', bg='black',
                   command=lambda: press("-"), height=3, width=7, font='arial 9 bold')
    minus.grid(row=3, column=3, sticky='nesw')

    multiply = Button(window, text=' * ', fg='red', bg='black',
                      command=lambda: press("*"), height=3, width=7, font='arial 9 bold')
    multiply.grid(row=4, column=3, sticky='nesw')

    divide = Button(window, text=' / ', fg='red', bg='black',
                    command=lambda: press("/"), height=3, width=7, font='arial 9 bold')
    divide.grid(row=5, column=3, sticky='nesw')

    equal = Button(window, text=' = ', fg='red', bg='black',
                   command=equalpress, height=3, width=7, font='arial 9 bold')
    equal.grid(row=5, column=2, sticky='nesw')

    clear = Button(window, text='Clear', fg='red', bg='black',
                   command=clear, height=3, width=38, font='arial 9 bold')
    clear.place(x=0, y=280)

    Decimal = Button(window, text='.', fg='red', bg='black',
                     command=lambda: press('.'), height=3, width=7, font='arial 9 bold')
    Decimal.grid(row=5, column=0, sticky='nesw')

    window.mainloop()
