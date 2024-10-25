# components/power_source.py
from .component import Component  # Import Component

class PowerSource(Component):
    def __init__(self, canvas, x, y, voltage):
        super().__init__("Power Source")
        self.canvas = canvas
        self.voltage = voltage
        self.x = x
        self.y = y
        self.id = self.draw()

    def draw(self):
        line_pos = self.canvas.create_line(self.x, self.y - 20, self.x, self.y + 20, fill="black", width=3)
        line_neg = self.canvas.create_line(self.x, self.y + 10, self.x + 10, self.y + 20, fill="black", width=3)
        text = self.canvas.create_text(self.x + 15, self.y, text=f"{self.voltage}V")
        return (line_pos, line_neg, text)

    def move(self, dx, dy):
        self.canvas.move(self.id[0], dx, dy)
        self.canvas.move(self.id[1], dx, dy)
        self.canvas.move(self.id[2], dx, dy)

    def set_value(self, new_voltage):
        self.voltage = new_voltage
        self.canvas.itemconfig(self.id[2], text=f"{self.voltage}V")
