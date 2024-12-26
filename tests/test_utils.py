import unittest
from shapes.utils import (
    distance_between_points, is_adjacent, calculate_sides_from_points
)


class TestGeometryUtils(unittest.TestCase):

    def test_distance_between_points_2d(self):
        self.assertAlmostEqual(distance_between_points((0, 0), (3, 4)), 5)
        self.assertAlmostEqual(distance_between_points((1, 1), (4, 5)), 5)

    def test_distance_between_points_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            distance_between_points((1, 2), (3, 4, 5))

        with self.assertRaises(ValueError):
            distance_between_points((1,), (2,))

    def test_distance_between_points_non_numeric(self):
        with self.assertRaises(ValueError):
            distance_between_points((1, 2), ("a", "b"))

    def test_is_adjacent_valid(self):
        self.assertTrue(is_adjacent("topleft", "topright"))
        self.assertTrue(is_adjacent("bottomleft", "topleft"))
        self.assertFalse(is_adjacent("topleft", "bottomright"))

    def test_is_adjacent_invalid_names(self):
        with self.assertRaises(ValueError):
            is_adjacent("center", "topright")

        with self.assertRaises(ValueError):
            is_adjacent("topleft", "middle")

    def test_calculate_sides_from_points_2d(self):
        self.assertEqual(calculate_sides_from_points((0, 0), (3, 4)), (3, 4))
        self.assertEqual(calculate_sides_from_points((1, 1), (4, 5)), (3, 4))

    def test_calculate_sides_from_points_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            calculate_sides_from_points((1, 2), (3, 4, 5))

        with self.assertRaises(ValueError):
            calculate_sides_from_points((1,), (2,))

    def test_calculate_sides_from_points_invalid_coordinates(self):
        with self.assertRaises(TypeError):
            calculate_sides_from_points((1, 2), ("a", "b"))


if __name__ == "__main__":
    unittest.main()
