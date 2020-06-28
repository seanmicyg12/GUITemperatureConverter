import tkinter as tk
import tkinter.ttk as ttk
#import Code as cd # you can delete this I'm having a hard time pip installing this package even though it should work.
import tkinter.messagebox as messagebox

root = tk.Tk()
root.title("Temperature Unit Converter")
root.geometry("620x300")
root.resizable(0, 0)
root.config(bg="white")

temp_label = tk.Label(root, text="Enter Temperature:", bg="white")
temp_label.grid(row=0, column=0, pady=20, padx=50)
temperature = tk.StringVar()
temp_ent = ttk.Entry(root, width=25, textvariable=temperature)
temp_ent.grid(row=0, column=1)
temp_ent.focus()

unit_label = tk.Label(root, text="Select Unit:", bg="white")
unit_label.grid(row=1, column=0)
unit = tk.StringVar()
unit_box = ttk.Combobox(root, width=23, textvariable=unit, state="readonly")
unit_box["values"] = ("Celsius", "Fahrenheit")
unit_box.current(0)
unit_box.grid(row=1, column=1)

unit1 = tk.StringVar()
unit_box1 = ttk.Combobox(root, width=23, textvariable=unit1, state="readonly")
unit_box1["values"] = ("Celsius", "Fahrenheit")
unit_box1.current(1)
unit_box1.grid(row=2, column=1, padx=50, pady=20)

ans_label = tk.Label(root, text="Answer Is:" , bg='white')
ans_label.grid(row=3, column=0)

def convert():
    try:
        if len(temperature.get()) < 8:
            ans = cd.temperature_convert(int(temperature.get()), unit.get(), unit1.get())
            global ans_frame
            ans_frame = tk.Frame(root, width=50, height=50, bg="white")
            ans_frame.grid(row=3, column=1)
            win = tk.Label(ans_frame, text=f"{round(ans)} {unit1.get()}", bg="white")
            win.grid(row=0, column=0)
        else:
            messagebox.showerror("Input Error", "Limit of Entry is 7")
    except:
        messagebox.showerror("Input Error", "Enter A Number")

def clear():
    ans_frame.destroy()

def exit():
    root.destroy()

convert_btn = ttk.Button(root, text="Convert", command=convert)
convert_btn.grid(row=3, column=1, pady=10)

clear_btn = ttk.Button(root, text="Clear", command=clear)
clear_btn.grid(row=4, column=1, pady=10)

exit_btn = ttk.Button(root, text="Exit", command=exit)
exit_btn.grid(row=5, column=1, pady=10)

root.mainloop()
