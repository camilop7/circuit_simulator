# components/component.py
class Component:
    def __init__(self, name):
        self.name = name
        self.id = []  # Store IDs of shapes drawn on the canvas

    def get_position(self):
        # Return the current position of the component
        if self.id:
            coords = self.canvas.coords(self.id[0])  # Assuming the first ID is the main visual element
            return (coords[0] + (coords[2] - coords[0]) / 2, coords[1] + (coords[3] - coords[1]) / 2)  # Center of the rectangle
        return (0, 0)  # Default return if no ID exists

    def is_mouse_over(self, x, y):
        if self.id:
            return self.canvas.bbox(self.id[0])[0] <= x <= self.canvas.bbox(self.id[0])[2] and \
                   self.canvas.bbox(self.id[0])[1] <= y <= self.canvas.bbox(self.id[0])[3]
        return False
