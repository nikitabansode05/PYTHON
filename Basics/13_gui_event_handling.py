import tkinter as tk


def calculate_premium():

    sum_assured = float(entry.get())
    premium = sum_assured * 0.05
    result_label.config(text=f"Illustrative Premium: ₹{premium:.2f}")


window = tk.Tk()

window.title("TFLInsurance Premium Calculator")
window.geometry("400x250")

label = tk.Label(window, text="Enter Sum Assured")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

button = tk.Button( window, text="Calculate Premium", command=calculate_premium)

button.pack(pady=20)
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()