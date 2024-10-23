# components/cable.py
import tkinter as tk
from components.component import Component

class Cable:
    def __init__(self, canvas, start, end):
        self.canvas = canvas
        self.start = start
        self.end = end
        self.id = self.draw()  # Call draw when initializing

    def draw(self):
        # Draw a line on the canvas representing the cable
        return self.canvas.create_line(self.start[0], self.start[1], self.end[0], self.end[1], fill="black", width=2)

    def update_position(self, new_start, new_end):
        # Update the cable's position and redraw it
        self.start = new_start
        self.end = new_end
        self.canvas.coords(self.id, self.start[0], self.start[1], self.end[0], self.end[1])
