import tkinter as tk
from components.resistor import Resistor
from components.power_source import PowerSource
from components.cable import Cable

class CircuitSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Circuit Simulator")
        self.geometry("800x600")

        # Create the canvas
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Store components and cables
        self.components = []
        self.cables = []

        # Create buttons for components
        self.add_resistor_button = tk.Button(self, text="Add Resistor", command=self.add_resistor)
        self.add_resistor_button.pack(side=tk.LEFT)

        self.add_power_source_button = tk.Button(self, text="Add Power Source", command=self.add_power_source)
        self.add_power_source_button.pack(side=tk.LEFT)

        self.add_cable_button = tk.Button(self, text="Add Cable", command=self.start_cable)
        self.add_cable_button.pack(side=tk.LEFT)

        # Bind mouse events for drag-and-drop
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.do_drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)  # Corrected binding

        self.selected_component = None
        self.cable_start = None

    def add_resistor(self):
        resistance = 10  # Placeholder value
        resistor = Resistor(self.canvas, 100, 100, resistance)
        self.components.append(resistor)

    def add_power_source(self):
        voltage = 5  # Placeholder value
        power_source = PowerSource(self.canvas, 200, 200, voltage)
        self.components.append(power_source)

    def start_cable(self):
        self.cable_start = None  # Reset starting point for cable
        print("Click on a component to start the cable")  # Debug message

    def start_drag(self, event):
        item = self.canvas.find_closest(event.x, event.y)

        # Check if the clicked item is a component
        for component in self.components:
            if item[0] in component.id:  # Check if the component's ID matches
                self.selected_component = component
                print(f"Selected component: {component.name}")  # Debug message
                break  # Exit the loop if found

        # If no component was selected, check if starting cable
        if self.cable_start is None:
            for component in self.components:
                if item[0] in component.id:
                    self.cable_start = component.get_position()  # Set start point to component position
                    print(f"Cable start position: {self.cable_start}")  # Debug message
                    break

    def do_drag(self, event):
        # Move the selected component with the mouse
        if self.selected_component:
            dx = event.x - self.canvas.coords(self.selected_component.id[0])[0]
            dy = event.y - self.canvas.coords(self.selected_component.id[0])[1]
            self.selected_component.move(dx, dy)

        # If drawing cable, update cable position
        if self.cable_start is not None:
            self.canvas.delete("temp_cable")  # Clear previous temp cable
            self.canvas.create_line(self.cable_start[0], self.cable_start[1], event.x, event.y, fill="gray", dash=(2, 2), tags="temp_cable")

    def stop_drag(self, event):
        # Deselect component
        if self.selected_component:
            self.selected_component = None

        # Finish drawing cable
        if self.cable_start is not None:
            for component in self.components:
                # Check if the mouse is over a component
                if component.is_mouse_over(event.x, event.y):
                    end_pos = component.get_position()
                    new_cable = Cable(self.canvas, self.cable_start, end_pos)
                    self.cables.append(new_cable)
                    print(f"Cable added from {self.cable_start} to {end_pos}")  # Debug message
                    break

        # Reset cable start
        self.cable_start = None


if __name__ == "__main__":
    simulator = CircuitSimulator()
    simulator.mainloop()
