from  polygon import Polygon
from shape import Shape

class Triangle(Polygon, Shape):
    def area_of_triangle(self):
        return self.get_height() * self.get_width() / 2