# components/resistor.py
import tkinter as tk
from components.component import Component

class Resistor(Component):
    def __init__(self, canvas, x, y, resistance):
        super().__init__("Resistor")
        self.resistance = resistance
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = self.draw()

    def draw(self):
        # Draw the resistor as a rectangle with the resistance value
        rect = self.canvas.create_rectangle(self.x - 20, self.y - 10, self.x + 20, self.y + 10, fill="gray")
        text = self.canvas.create_text(self.x, self.y, text=f"{self.resistance}Ω")
        return (rect, text)

    def move(self, dx, dy):
        # Move the resistor by dx and dy
        self.canvas.move(self.id[0], dx, dy)
        self.canvas.move(self.id[1], dx, dy)

    def get_position(self):
        return self.x, self.y
