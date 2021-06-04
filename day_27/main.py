import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.configure(padx=20, pady=20, width = 300, height = 200, )
window.resizable(False, False)

miles_label = tkinter.Label(text="Miles", font=("Arial", 16, "normal"))
miles_label.grid(column=2, row=0)

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.focus_set()

equal_label = tkinter.Label(text="is equal to", font=("Arial", 16, "normal"))
equal_label.grid(column=0, row=1)

km_result_label = tkinter.Label(text="0", font=("Arial", 16, "normal"))
km_result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 16, "normal"))
km_label.grid(column=2, row=1)


def calculate():
    miles = float(miles_input.get())
    km = miles * 1.6
    km_result_label.config(text=f'{km:.2f}')


calculate_button = tkinter.Button(window, text="Calculate", background="blue", width=10, command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
