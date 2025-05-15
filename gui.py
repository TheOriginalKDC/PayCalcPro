import tkinter as tk
from tkinter import ttk, messagebox
from logic import calculate_pay

def launch_app():
    def on_calculate():
        try:
            hours = float(entry_hours.get())
            rate = float(entry_pay.get())
            ot_type_val = overtime_type.get()
            ot_custom = float(entry_custom_ot.get()) if ot_type_val == "Custom" else None

            result = calculate_pay(hours, rate, ot_type_val, ot_custom)

            label_result.config(text=f"Regular Pay: ${result['regular']:.2f}\n"
                                     f"Overtime Pay: ${result['overtime']:.2f}\n"
                                     f"Total Pay: ${result['total']:.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    root = tk.Tk()
    root.title("Professional Pay Calculator")
    root.geometry("420x380")
    root.configure(bg="#1e1e1e")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))
    style.configure("TButton", font=("Segoe UI", 10))
    style.configure("TEntry", font=("Segoe UI", 10))

    ttk.Label(root, text="Hours Worked:").pack(pady=5)
    entry_hours = ttk.Entry(root)
    entry_hours.pack()

    ttk.Label(root, text="Base Pay Rate ($/hr):").pack(pady=5)
    entry_pay = ttk.Entry(root)
    entry_pay.pack()

    ttk.Label(root, text="Overtime Rate:").pack(pady=5)
    overtime_type = ttk.Combobox(root, values=["Time and a Half (1.5x)", "Double Time (2x)", "Custom"])
    overtime_type.set("Time and a Half (1.5x)")
    overtime_type.pack()

    entry_custom_ot = ttk.Entry(root)
    entry_custom_ot.insert(0, "1.5")
    entry_custom_ot.pack(pady=5)
    ttk.Label(root, text="(Used only for 'Custom' rate)").pack()

    ttk.Button(root, text="Calculate Pay", command=on_calculate).pack(pady=15)

    label_result = ttk.Label(root, text="")
    label_result.pack()

    root.mainloop()
