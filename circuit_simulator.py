import tkinter as tk
from tkinter import ttk
from sympy import symbols, Eq, solve

# Create the main application window
root = tk.Tk()
root.title("Simple Circuit Simulator")
root.geometry("400x300")

# Define symbols for voltage, resistance, and current
V, R, I = symbols('V R I')

# Function to calculate current using KVL (V = IR)
def calculate_current():
    try:
        voltage = float(voltage_entry.get())
        resistance = float(resistance_entry.get())

        # Define KVL equation: V = IR
        equation = Eq(V, I * R)

        # Substitute given values into the equation
        equation = equation.subs(V, voltage).subs(R, resistance)

        # Solve for current
        current_solution = solve(equation, I)[0]

        # Display the result
        result_label.config(text=f"Current: {current_solution:.2f} A")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create input fields and labels for voltage and resistance
voltage_label = tk.Label(root, text="Voltage (V):")
voltage_label.pack(pady=5)
voltage_entry = tk.Entry(root)
voltage_entry.pack(pady=5)

resistance_label = tk.Label(root, text="Resistance (Ω):")
resistance_label.pack(pady=5)
resistance_entry = tk.Entry(root)
resistance_entry.pack(pady=5)

# Button to calculate current
calculate_button = tk.Button(root, text="Calculate Current", command=calculate_current)
calculate_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="Current: N/A")
result_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
