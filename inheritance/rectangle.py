from polygon import Polygon
from shape import Shape


class Rectangle(Polygon, Shape):
    def area_of_rectangle(self):
        return self.get_height() * self.get_width()
