import tkinter as tk
from datetime import datetime, date, timedelta

def calculate():
    try:
        # Define the format: Day-Month-Year (2 digits)
        date_format = "%d-%m-%y"
        
        # Convert the string from the Entry box into a date object
        start_dt = datetime.strptime(entry_start.get(), date_format).date()
        target_dt = datetime.strptime(entry_target.get(), date_format).date()
        today = date.today()

        # Logic
        elapsed = (today - start_dt).days
        remaining_days = (target_dt - today).days
        remaining_years = remaining_days / 365.25

        # Update labels with results
        label_elapsed.config(text=f"Days Elapsed: {elapsed}")
        label_years.config(text=f"Years Remaining: {remaining_years:.4f}")
        
    except ValueError:
        label_elapsed.config(text="Error: Use DD-MM-YY")
        label_years.config(text="")

# Setup Window
root = tk.Tk()
root.title("Time Metrics Calculator")
root.geometry("350x280")

# Logic to self-populate with current dates
today_str = date.today().strftime("%d-%m-%y")
future_str = (date.today() + timedelta(days=365)).strftime("%d-%m-%y")

# Input Fields
tk.Label(root, text="Start Date (DD-MM-YY):", font=("Arial", 10)).pack(pady=5)
entry_start = tk.Entry(root, justify='center')
entry_start.insert(0, today_str) 
entry_start.pack()

tk.Label(root, text="Target Date (DD-MM-YY):", font=("Arial", 10)).pack(pady=5)
entry_target = tk.Entry(root, justify='center')
entry_target.insert(0, future_str)
entry_target.pack()

# Calculation Button
btn_calc = tk.Button(root, text="Calculate Metrics", command=calculate, bg="#e1e1e1")
btn_calc.pack(pady=15)

# Display Results
label_elapsed = tk.Label(root, text="Days Elapsed: --", font=("Arial", 11, "bold"))
label_elapsed.pack()

label_years = tk.Label(root, text="Years Remaining: --", font=("Arial", 11, "bold"))
label_years.pack()

root.mainloop()