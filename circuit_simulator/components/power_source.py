# components/power_source.py
import tkinter as tk
from components.component import Component

class PowerSource(Component):
    def __init__(self, canvas, x, y, voltage):
        super().__init__("Power Source")
        self.voltage = voltage
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = self.draw()

    def draw(self):
        # Draw the power source as two lines
        line_pos = self.canvas.create_line(self.x, self.y - 20, self.x, self.y + 20, fill="black", width=3)
        line_neg = self.canvas.create_line(self.x, self.y + 10, self.x + 10, self.y + 20, fill="black", width=3)
        text = self.canvas.create_text(self.x + 15, self.y, text=f"{self.voltage}V")
        return (line_pos, line_neg, text)

    def move(self, dx, dy):
        # Move the power source by dx and dy
        self.canvas.move(self.id[0], dx, dy)
        self.canvas.move(self.id[1], dx, dy)
        self.canvas.move(self.id[2], dx, dy)

    def get_position(self):
        return self.x, self.y
