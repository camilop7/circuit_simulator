# components/resistor.py
from .component import Component  # Import Component

class Resistor(Component):
    def __init__(self, canvas, x, y, resistance):
        super().__init__("Resistor")
        self.canvas = canvas
        self.resistance = resistance
        self.x = x
        self.y = y
        self.id = self.draw()

    def draw(self):
        rect = self.canvas.create_rectangle(self.x - 20, self.y - 10, self.x + 20, self.y + 10, fill="gray")
        text = self.canvas.create_text(self.x, self.y, text=f"{self.resistance}Ω")
        return (rect, text)

    def move(self, dx, dy):
        self.canvas.move(self.id[0], dx, dy)
        self.canvas.move(self.id[1], dx, dy)

    def set_value(self, new_resistance):
        self.resistance = new_resistance
        self.canvas.itemconfig(self.id[1], text=f"{self.resistance}Ω")
