import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    text_result.delete(1.0, "end")

    

root = tk.Tk()
root.geometry("300x245")
text_result = tk.Text(root, height=2, width=16, font=("Arial",26), fg="white",bg="black")
text_result.grid(columnspan=7)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial",14), fg="white", bg="black")       # frame button make
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=5, font=("Arial",14), fg="white", bg="black")
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda:add_to_calculation(3), width=5, font=("Arial",14), fg="white", bg="black")
btn_3.grid(row=2, column=3)

btn_plus = tk.Button(root, text="+", command=lambda:add_to_calculation("+"), width=5, font=("Arial",14), fg="white", bg="black")
btn_plus.grid(row=2, column=4)

btn_4 = tk.Button(root, text="4", command=lambda:add_to_calculation(4), width=5, font=("Arial",14), fg="white", bg="black")
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda:add_to_calculation(5), width=5, font=("Arial",14), fg="white", bg="black")
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda:add_to_calculation(6), width=5, font=("Arial",14), fg="white", bg="black")
btn_6.grid(row=3, column=3)

btn_minus = tk.Button(root, text="-", command=lambda:add_to_calculation("-"), width=5, font=("Arial",14),  fg="white", bg="black")
btn_minus.grid(row=3, column=4)


btn_7 = tk.Button(root, text="7", command=lambda:add_to_calculation(7), width=5, font=("Arial",14), fg="white", bg="black")
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda:add_to_calculation(8), width=5, font=("Arial",14), fg="white", bg="black")
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda:add_to_calculation(9), width=5, font=("Arial",14), fg="white", bg="black")
btn_9.grid(row=4, column=3)

btn_multi= tk.Button(root, text="*", command=lambda:add_to_calculation("*"), width=5, font=("Arial",14), fg="white", bg="black")
btn_multi.grid(row=4, column=4)


btn_0 = tk.Button(root, text="0", command=lambda:add_to_calculation(0), width=5, font=("Arial",14), fg="white", bg="black")
btn_0.grid(row=5, column=1)

btn_Equal = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial",14), fg="white", bg="black")
btn_Equal.grid(row=5, column=2, )

btn_devide = tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width=5, font=("Arial",14), fg="white", bg="black")
btn_devide.grid(row=5, column=4)

btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial",14), fg="white", bg="black")
btn_clear.grid(row=5, column=3)

root.title('calulator')
root.mainloop()