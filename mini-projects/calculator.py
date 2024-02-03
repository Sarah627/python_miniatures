from tkinter import *
root = Tk()
root.title("calculator")  # The title of our simple program
mainScreen = Entry(root, width=35).grid(
    row=0, column=0, columnspan=3)


def cal(number):
    current = mainScreen.get()
    mainScreen.delete(0, END)
    mainScreen.insert(0, str(current)+str(number))


button_1 = Button(root, text="1", padx=20, pady=20,
                  command=lambda: cal(1)).grid(row=2, column=0)
button_2 = Button(root, text="2", padx=20, pady=20,
                  command=lambda: cal(2)).grid(row=2, column=1)
button_3 = Button(root, text="3", padx=20, pady=20,
                  command=lambda: cal(3)).grid(row=2, column=2)
button_4 = Button(root, text="4", padx=20, pady=20,
                  command=lambda: cal(4)).grid(row=3, column=0)
button_5 = Button(root, text="5", padx=20, pady=20,
                  command=lambda: cal(5)).grid(row=3, column=1)
button_6 = Button(root, text="6", padx=20, pady=20,
                  command=lambda: cal(6)).grid(row=3, column=2)
button_7 = Button(root, text="7", padx=20, pady=20,
                  command=lambda: cal(7)).grid(row=4, column=0)
button_8 = Button(root, text="8", padx=20, pady=20,
                  command=lambda: cal(8)).grid(row=4, column=1)
button_9 = Button(root, text="9", padx=20, pady=20,
                  command=lambda: cal(9)).grid(row=4, column=2)
button_0 = Button(root, text="0", padx=20, pady=20,
                  command=lambda: cal(0)).grid(row=5, column=1)
button_dot = Button(root, text=".", padx=20, pady=20,
                    command=cal).grid(row=5, column=0)
button_c = Button(root, text="c", padx=20, pady=20,
                  command=cal).grid(row=5, column=2)
button_p = Button(root, text="+", padx=20, pady=20,
                  command=cal).grid(row=2, column=3)
button_m = Button(root, text="-", padx=20, pady=20,
                  command=cal).grid(row=1, column=3)
button_mod = Button(root, text="%", padx=20, pady=20,
                    command=cal).grid(row=1, column=2)
button_e = Button(root, text="=", padx=20, pady=80,
                  command=cal).grid(row=3, rowspan=3, column=3)
button_mul = Button(root, text="*", padx=20, pady=20,
                    command=cal).grid(row=1, column=1)
button_d = Button(root, text="/", padx=20, pady=20,
                  command=cal).grid(row=1, column=0)

root.mainloop()
