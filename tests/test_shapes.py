import unittest
from shapes.shapes import (
    Parallelogram,
    Rectangle,
    Square,
    Rhombus,
    Triangle,
    Circle
)


class TestShapes(unittest.TestCase):

    def test_parallelogram(self):
        p = Parallelogram(5, 10, 30)
        self.assertAlmostEqual(p.perimeter, 30)
        self.assertAlmostEqual(p.area, 50 * 0.5, places=2)

    def test_rectangle(self):
        r = Rectangle(4, 6)
        self.assertEqual(r.perimeter, 20)
        self.assertEqual(r.area, 24)

    def test_square(self):
        s = Square(4)
        self.assertEqual(s.perimeter, 16)
        self.assertEqual(s.area, 16)

    def test_rhombus(self):
        rh = Rhombus(5, 60)
        self.assertAlmostEqual(rh.area, 5 * 5 * 0.866, places=2)

    def test_triangle(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.perimeter, 12)
        self.assertEqual(t.area, 6)

    def test_circle(self):
        c = Circle(3)
        self.assertAlmostEqual(c.perimeter, 18.849, places=2)
        self.assertAlmostEqual(c.area, 28.274, places=3)


if __name__ == "__main__":
    unittest.main()
