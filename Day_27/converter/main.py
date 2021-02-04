import tkinter as tk


def kilometers_calculate():
    miles = float(input_miles.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=km)


window = tk.Tk()
window.title("Mile to km converter")
window.minsize(width=250, height=140)
window.config(padx=30, pady=30)


input_miles = tk.Entry(width=10)
input_miles.focus()
input_miles.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tk.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tk.Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", command=kilometers_calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
