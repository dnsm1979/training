import math


class Shape:
    def __init__(self, segment_a: int, segment_b: int, segment_h: int):
        self.segment_a = segment_a  # отрезок соответствующий одной стороны фигуры
        self.segment_b = segment_b  # отрезок соответствующий другой стороны фигуры
        self.segment_h = segment_h  # отрезок соответствующий высоты или радиуса фигуры

    def __str__(self):
        return f"Площадь фигуры квадрат ровна: {self.segment_a ** 2}"


class Rectangle(Shape):
    def __str__(self):
        return f"Площадь фигуры прямоугольника ровна: {self.segment_a * self.segment_b}"


class Circle(Shape):
    def __str__(self):
        return f"Площадь фигуры круг ровна: {round(self.segment_h ** 2 * math.pi, 2)}"


class Right_triangle(Shape):
    def __str__(self):
        return f"Площадь фигуры прямоугольного треугольника ровна: {round(self.segment_a * self.segment_h / 2, 2)}"


class Trapezoid(Shape):
    def __str__(self):
        return f"Площадь фигуры трапеция ровна: {round((self.segment_a + self.segment_b) / 2 * self.segment_h, 2)}"


shape = Shape(5, 0, 0)
print(shape)
rectangle = Rectangle(5, 8, 0)
print(rectangle)
circle = Circle(0, 0, 6)
print(circle)
right_triangle = Right_triangle(7, 0, 4)
print(right_triangle)
trapezoid = Trapezoid(4, 8, 3)
print(trapezoid)
