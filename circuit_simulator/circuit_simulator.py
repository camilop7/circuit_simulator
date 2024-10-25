import tkinter as tk
from tkinter import simpledialog, messagebox
from components.resistor import Resistor
from components.power_source import PowerSource

class CircuitSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Circuit Simulator")
        self.geometry("1000x600")

        # Main canvas and control frame
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        control_frame = tk.Frame(self)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.add_resistor_button = tk.Button(control_frame, text="Add Resistor", command=self.add_resistor)
        self.add_resistor_button.pack()

        self.add_power_source_button = tk.Button(control_frame, text="Add Power Source", command=self.add_power_source)
        self.add_power_source_button.pack()

        self.add_cable_button = tk.Button(control_frame, text="Add Cable Layout", command=self.choose_cable_layout)
        self.add_cable_button.pack()

        # Store components, cables, and layout templates
        self.components = []
        self.layout_template = None

        # Bindings for drag, drop, and editing
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.do_drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)
        self.canvas.bind("<Double-Button-1>", self.edit_value)

        self.selected_component = None

        # Calculation frame
        self.calc_frame = tk.Frame(self, width=200, height=600, bg="lightgray")
        self.calc_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.create_calculation_table()

    def create_calculation_table(self):
        tk.Label(self.calc_frame, text="Circuit Calculations", bg="lightgray", font=('Arial', 12, 'bold')).pack(pady=5)
        self.resistor_label = tk.Label(self.calc_frame, text="Resistors:", bg="lightgray", anchor="w")
        self.resistor_label.pack(fill=tk.X, padx=10)
        self.resistor_values = tk.Listbox(self.calc_frame, height=8)
        self.resistor_values.pack(fill=tk.X, padx=10, pady=5)

        self.power_source_label = tk.Label(self.calc_frame, text="Power Sources:", bg="lightgray", anchor="w")
        self.power_source_label.pack(fill=tk.X, padx=10)
        self.power_source_values = tk.Listbox(self.calc_frame, height=8)
        self.power_source_values.pack(fill=tk.X, padx=10, pady=5)

        self.current_label = tk.Label(self.calc_frame, text="Total Current (I): -- A", bg="lightgray")
        self.current_label.pack(pady=10)

    def add_resistor(self):
        resistor = Resistor(self.canvas, 100, 100, resistance=10)
        self.components.append(resistor)
        self.update_calculation_table()

    def add_power_source(self):
        power_source = PowerSource(self.canvas, 200, 200, voltage=5)
        self.components.append(power_source)
        self.update_calculation_table()

    def choose_cable_layout(self):
        self.layout_template = simpledialog.askstring("Cable Layout", "Enter layout (series or parallel):")
        messagebox.showinfo("Layout Chosen", f"Selected layout: {self.layout_template}")

    def start_drag(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        for component in self.components:
            if item[0] in component.id:
                self.selected_component = component
                break

    def do_drag(self, event):
        if self.selected_component:
            dx = event.x - self.canvas.coords(self.selected_component.id[0])[0]
            dy = event.y - self.canvas.coords(self.selected_component.id[0])[1]
            self.selected_component.move(dx, dy)

    def stop_drag(self, event):
        if self.selected_component:
            self.selected_component = None

    def edit_value(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        for component in self.components:
            if item[0] in component.id:
                new_value = simpledialog.askfloat("Edit Value", f"Enter new value for {component.name}:")
                if new_value is not None:
                    component.set_value(new_value)
                    self.update_calculation_table()

    def update_calculation_table(self):
        self.resistor_values.delete(0, tk.END)
        self.power_source_values.delete(0, tk.END)

        total_resistance = 0
        total_voltage = 0

        for component in self.components:
            if isinstance(component, Resistor):
                self.resistor_values.insert(tk.END, f"{component.resistance}Ω")
                total_resistance += component.resistance
            elif isinstance(component, PowerSource):
                self.power_source_values.insert(tk.END, f"{component.voltage}V")
                total_voltage += component.voltage

        if total_resistance > 0:
            current = total_voltage / total_resistance
            self.current_label.config(text=f"Total Current (I): {current:.2f} A")

if __name__ == "__main__":
    simulator = CircuitSimulator()
    simulator.mainloop()
