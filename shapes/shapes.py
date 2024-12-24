from math import radians, sin, pi


class Shape:
    pass


class Parallelogram(Shape):
    def __init__(
            self,
            side1_length: int | float,
            side2_length: int | float,
            angle_between_sides_degrees: int | float,
    ) -> None:
        self.side1_length = side1_length
        self.side2_length = side2_length
        self.angle_between_sides_degrees = angle_between_sides_degrees

    @property
    def perimeter(self) -> int | float:
        return 2 * (self.side1_length + self.side2_length)

    @property
    def area(self) -> int | float:
        return (self.side1_length
                * self.side2_length
                * sin(radians(self.angle_between_sides_degrees)))

    def __repr__(self) -> str:
        return (
            f"Parallelogram(side1_length={self.side1_length}, "
            f"side2_length={self.side2_length}, "
            f"angle_between_sides_degrees={self.angle_between_sides_degrees})"
        )

    def __str__(self) -> str:
        return (f"{self.__class__.__name__} "
                f"Perimeter {self.perimeter} Area {self.area}")


class Rhombus(Parallelogram):
    def __init__(
            self,
            side_length: int | float,
            angle_between_sides_degrees: int | float
    ) -> None:
        super().__init__(side_length, side_length, angle_between_sides_degrees)


class Rectangle(Parallelogram):
    def __init__(self, side1_length, side2_length) -> None:
        super().__init__(
            side1_length,
            side2_length,
            90
        )  # between sides rectangle has 90 degrees


class Square(Rectangle):
    def __init__(self, side_length: int | float) -> None:
        super().__init__(side_length, side_length)


class Triangle(Shape):
    def __init__(
            self,
            side1_length: int | float,
            side2_length: int | float,
            side3_length: int | float
    ) -> None:
        self.side1_length = side1_length
        self.side2_length = side2_length
        self.side3_length = side3_length

    @property
    def perimeter(self) -> int | float:
        return self.side1_length + self.side2_length + self.side3_length

    @property
    def area(self) -> int | float:
        p = self.perimeter / 2
        return (p * (p - self.side1_length)
                * (p - self.side2_length)
                * (p - self.side3_length)) ** 0.5

    def __repr__(self) -> str:
        return (f"Triangle(side1_length={self.side1_length}, "
                f"side2_length={self.side2_length}, "
                f"side3_length={self.side3_length})")

    def __str__(self) -> str:
        return f"Triangle Perimeter {self.perimeter} Area {self.area}"


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"

    def __str__(self) -> str:
        return f"Circle Perimeter {self.perimeter} Area {self.area}"
