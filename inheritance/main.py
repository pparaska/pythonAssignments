from rectangle import Rectangle
from triangle import Triangle

rectangle = Rectangle()
rectangle.set_values(20, 10)
rectangle.set_color('red')
print(rectangle.area_of_rectangle())
print(rectangle.get_color())

triangle = Triangle()
triangle.set_values(15, 10)
triangle.set_color('green')
print(triangle.area_of_triangle())
print(triangle.get_color())
