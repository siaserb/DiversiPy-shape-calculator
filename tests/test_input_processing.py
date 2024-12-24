import unittest
from unittest.mock import patch

from main import create_shape_instance
from shapes.input_processing import proceed_shapes_parametres, collect_shapes
from shapes.shapes import Square, Circle, Triangle


class TestProceedShapesParametres(unittest.TestCase):

    def test_square_with_side(self):
        result = proceed_shapes_parametres("Side 4", "square")
        self.assertEqual(result, {"side_length": 4.0})

    def test_square_with_not_adjacent_coordinates(self):
        result = proceed_shapes_parametres(
            "TopLeft -1 -1 BottomRight 5 5",
            "square"
        )
        self.assertEqual(result, {"side_length": 6.0})

    def test_square_with_adjacent_coordinates(self):
        result = proceed_shapes_parametres(
            "TopLeft 0 4 TopRight 4 4",
            "square"
        )
        self.assertEqual(result, {"side_length": 4.0})

    def test_square_invalid_side(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("Side -4", "square")
        self.assertEqual(
            str(context.exception),
            "Side length must be positive"
        )

    def test_square_not_full_info(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("", "square")
        self.assertEqual(
            str(context.exception),
            "Lack of information about Square or incorrect format"
        )

    def test_rectangle_with_sides(self):
        result = proceed_shapes_parametres("Side1 4 Side2 5", "rectangle")
        self.assertEqual(result, {"side1_length": 4.0, "side2_length": 5.0})

    def test_rectangle_with_two_coordinates(self):
        result = proceed_shapes_parametres(
            "TopLeft 0 0 BottomRight 4 5",
            "rectangle"
        )
        self.assertEqual(result, {"side1_length": 4.0, "side2_length": 5.0})

    def test_rectangle_with_three_coordinates_1(self):
        result = proceed_shapes_parametres(
            "TopLeft 0 0 TopRight 0 5 BottomRight 4 5",
            "rectangle"
        )
        self.assertEqual(result, {"side1_length": 4.0, "side2_length": 5.0})

    def test_rectangle_with_three_coordinates_2(self):
        result = proceed_shapes_parametres(
            "BottomLeft 0 0 TopLeft 0 5 BottomRight 6 0",
            "rectangle"
        )
        self.assertEqual(result, {"side1_length": 6.0, "side2_length": 5.0})

    def test_rectangle_invalid_side(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("Side1 4 Side2 -5", "rectangle")
        self.assertEqual(
            str(context.exception),
            "Side length must be positive"
        )

    def test_rectangle_not_full_info(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("", "rectangle")
        self.assertEqual(
            str(context.exception),
            "Lack of information about Rectangle or incorrect format"
        )

    def test_parallelogram(self):
        result = proceed_shapes_parametres(
            "Side1 4 Side2 6 AngleBetweenSidesDegrees 45",
            "parallelogram"
        )
        self.assertEqual(result, {
            "side1_length": 4.0,
            "side2_length": 6.0,
            "angle_between_sides_degrees": 45.0
        })

    def test_parallelogram_invalid_angle(self):
        with self.assertRaises(ValueError) as context:
            proceed_shapes_parametres(
                "Side1 4 Side2 6 AngleBetweenSidesDegrees -45",
                "parallelogram")
        self.assertEqual(
            str(context.exception),
            "Side lengths and angle must be positive"
        )

    def test_rhombus(self):
        result = proceed_shapes_parametres(
            "Side 4 AngleBetweenSidesDegrees 30",
            "rhombus"
        )
        self.assertEqual(result, {
            "side_length": 4.0,
            "angle_between_sides_degrees": 30.0
        })

    def test_rhombus_invalid_angle(self):
        with self.assertRaises(ValueError) as context:
            proceed_shapes_parametres(
                "Side 4 AngleBetweenSidesDegrees -30",
                "rhombus"
            )
        self.assertEqual(
            str(context.exception),
            "Side lengths and angle must be positive"
        )

    def test_triangle_with_sides(self):
        result = proceed_shapes_parametres(
            "Side1 3 Side2 4 Side3 5",
            "triangle"
        )
        self.assertEqual(result, {
            "side1_length": 3.0,
            "side2_length": 4.0,
            "side3_length": 5.0
        })

    def test_triangle_with_points(self):
        result = proceed_shapes_parametres(
            "Point1 0 0 Point2 3 0 Point3 0 4",
            "triangle"
        )
        self.assertCountEqual(
            [
                result["side1_length"],
                result["side2_length"],
                result["side3_length"]
            ],
            [3.0, 4.0, 5.0]
        )

    def test_triangle_invalid_side(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("Side1 3 Side2 4 Side3 -5", "triangle")
        self.assertEqual(
            str(context.exception),
            "Side length must be positive"
        )

    def test_triangle_not_full_info(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("", "triangle")
        self.assertEqual(
            str(context.exception),
            "Lack of information about Triangle or incorrect format"
        )

    def test_circle(self):
        result = proceed_shapes_parametres("Radius 5", "circle")
        self.assertEqual(result, {"radius": 5.0})

    def test_circle_invalid_radius(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("Radius -5", "circle")
        self.assertEqual(str(context.exception), "Radius must be positive")

    def test_invalid_shape_type(self):
        with self.assertRaises(Exception) as context:
            proceed_shapes_parametres("Side 5", "unknown")
        self.assertEqual(
            str(context.exception),
            "Lack of information about unknown or incorrect format"
        )


class TestCollectShapes(unittest.TestCase):

    @patch("builtins.input", side_effect=[
        "square", "Side 4",
        "circle", "Radius 5",
        "triangle", "Side1 3 Side2 4 Side3 5",
        "stop"
    ])
    def test_collect_shapes_valid_inputs(self, mock_input):
        result = collect_shapes()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], {
            "shape_name": "square",
            "side_length": 4.0
        })
        self.assertEqual(result[1], {"shape_name": "circle", "radius": 5.0})
        self.assertEqual(result[2], {
            "shape_name": "triangle",
            "side1_length": 3.0,
            "side2_length": 4.0,
            "side3_length": 5.0
        })

    @patch("builtins.input", side_effect=[
        "rectangle", "Side1 4 Side2 -5",
        "stop"
    ])
    def test_collect_shapes_invalid_input(self, mock_input):
        with patch("builtins.print") as mock_print:
            result = collect_shapes()
            self.assertEqual(len(result), 0)
            mock_print.assert_called_with(
                "Error processing parameters: Side length must be positive"
            )

    @patch("builtins.input", side_effect=[
        "invalid_shape", "",
        "stop"
    ])
    def test_collect_shapes_invalid_shape_type(self, mock_input):
        with patch("builtins.print") as mock_print:
            result = collect_shapes()
            self.assertEqual(len(result), 0)
            mock_print.assert_called_with("Invalid shape type. Try again.")


class TestCreateShapeInstance(unittest.TestCase):

    def test_create_square_instance(self):
        shape_data = {"shape_name": "square", "side_length": 4.0}
        instance = create_shape_instance(shape_data)
        self.assertIsInstance(instance, Square)
        self.assertEqual(instance.side1_length, 4.0)

    def test_create_circle_instance(self):
        shape_data = {"shape_name": "circle", "radius": 5.0}
        instance = create_shape_instance(shape_data)
        self.assertIsInstance(instance, Circle)
        self.assertEqual(instance.radius, 5.0)

    def test_create_triangle_instance(self):
        shape_data = {
            "shape_name": "triangle",
            "side1_length": 3.0,
            "side2_length": 4.0,
            "side3_length": 5.0
        }
        instance = create_shape_instance(shape_data)
        self.assertIsInstance(instance, Triangle)
        self.assertEqual(instance.side1_length, 3.0)
        self.assertEqual(instance.side2_length, 4.0)
        self.assertEqual(instance.side3_length, 5.0)

    def test_create_invalid_shape_instance(self):
        shape_data = {"shape_name": "unknown_shape", "param": 1}
        with self.assertRaises(ValueError):
            create_shape_instance(shape_data)


if __name__ == "__main__":
    unittest.main()
