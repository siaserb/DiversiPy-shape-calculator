from shapes.utils import (
    is_adjacent,
    calculate_sides_from_points,
    distance_between_points,
)


def proceed_shapes_parametres(shape_info: str, shape_type: str) -> dict:
    shape_params = {}
    shape_info = shape_info.lower().split()

    positions = ("topright", "bottomright", "bottomleft", "topleft")

    def get_value(key: str) -> float:
        return float(shape_info[shape_info.index(key) + 1])

    def get_coordinates(keys: list) -> dict:
        return {
            key: (float(shape_info[shape_info.index(key) + 1]),
                  float(shape_info[shape_info.index(key) + 2]))
            for key in keys
        }

    if shape_type == "square":
        angles = [angle for angle in positions if angle in shape_info]

        if "side" in shape_info:
            side_length = get_value("side")
            if side_length <= 0:
                raise ValueError("Side length must be positive")
            shape_params.update({"side_length": side_length})

        elif len(angles) >= 2:
            point1, point2 = get_coordinates([angles[0], angles[1]]).values()
            if is_adjacent(angles[0], angles[1]):
                shape_params.update(
                    {
                        "side_length": distance_between_points(point1, point2)
                    }
                )
            else:
                side_length = calculate_sides_from_points(point1, point2)
                shape_params.update({"side_length": side_length})
        else:
            raise ValueError(
                "Lack of information about Square or incorrect format"
            )

    elif shape_type == "rectangle":

        angles = [angle for angle in positions if angle in shape_info]

        if "side1" in shape_info and "side2" in shape_info:
            side1_length, side2_length = get_value("side1"), get_value("side2")
            if side1_length <= 0 or side2_length <= 0:
                raise ValueError("Side length must be positive")
            shape_params.update(
                {
                    "side1_length": side1_length,
                    "side2_length": side2_length
                }
            )

        elif len(angles) >= 2:
            coordinates = 0
            if not is_adjacent(angles[0], angles[1]):
                coordinates = get_coordinates([angles[0], angles[1]])
            elif len(angles) > 2:
                if not is_adjacent(angles[0], angles[2]):
                    coordinates = get_coordinates([angles[0], angles[2]])
                else:
                    coordinates = get_coordinates([angles[1], angles[2]])
            if coordinates:
                point1, point2 = coordinates.values()
                side1_length, side2_length = calculate_sides_from_points(
                    point1,
                    point2
                )

                shape_params.update(
                    {
                        "side1_length": side1_length,
                        "side2_length": side2_length
                    }
                )
        else:
            raise ValueError(
                "Lack of information about Rectangle or incorrect format"
            )

    elif (
        shape_type == "parallelogram"
        and all(
            key in shape_info for key in (
                "side1", "side2", "anglebetweensidesdegrees"
            )
        )
    ):
        side1_length, side2_length, angle = map(
            get_value,
            ("side1", "side2", "anglebetweensidesdegrees")
        )
        if min(side1_length, side2_length, angle) <= 0:
            raise ValueError("Side lengths and angle must be positive")
        shape_params.update(
            {
                "side1_length": side1_length,
                "side2_length": side2_length,
                "angle_between_sides_degrees": angle
            }
        )

    elif (
        shape_type == "rhombus"
        and all(
            key in shape_info for key in (
                "side", "anglebetweensidesdegrees"
            )
        )
    ):
        side_length, angle = map(
            get_value,
            ("side", "anglebetweensidesdegrees")
        )
        if min(side_length, angle) <= 0:
            raise ValueError("Side lengths and angle must be positive")
        shape_params.update(
            {
                "side_length": side_length,
                "angle_between_sides_degrees": angle
            }
        )

    elif shape_type == "triangle":
        if all(
            point in shape_info for point in [
                "point1", "point2", "point3"
            ]
        ):
            coordinates = get_coordinates(["point1", "point2", "point3"])
            side_lengths = {
                f"side{i + 1}_length": (
                    distance_between_points(
                        coordinates[f"point{i % 3 + 1}"],
                        coordinates[f"point{(i + 1) % 3 + 1}"]
                    )
                )
                for i in range(3)
            }
            shape_params.update(side_lengths)
        elif all(side in shape_info for side in ["side1", "side2", "side3"]):
            side1_length, side2_length, side3_length = (
                get_value("side1"), get_value("side2"), get_value("side3")
            )
            if any(side <= 0 for side in [
                side1_length, side2_length, side3_length
            ]):
                raise ValueError("Side length must be positive")
            shape_params.update(
                {
                    "side1_length": side1_length,
                    "side2_length": side2_length,
                    "side3_length": side3_length
                }
            )
        else:
            raise ValueError(
                "Lack of information about Triangle or incorrect format"
            )

    elif shape_type == "circle" and "radius" in shape_info:
        radius = get_value("radius")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        shape_params.update({"radius": radius})

    else:
        raise ValueError(
            f"Lack of information about {shape_type.capitalize()} "
            f"or incorrect format"
        )

    return shape_params


def collect_shapes() -> list[dict]:
    shapes = []
    print("Enter shapes and their attributes. Type 'stop' to finish.")

    available_shapes = {
        "square": (
            "side length or coordinates of two angles "
            "(e.g., 'Side 2' or 'TopRight 1 1, BottomLeft -3 -10')"
        ),
        "rectangle": (
            "length of two sides or coordinates of two opposite angles "
            "(e.g., 'Side1 2 Side2 10' or 'TopRight 1 1, BottomLeft -3 -10')"
        ),
        "rhombus": (
            "side length and angle between sides in degrees "
            "(e.g., 'Side 2 AngleBetweenSidesDegrees 30')"
        ),
        "parallelogram": (
            "length of two sides and angle between them in degrees "
            "(e.g., 'Side1 2 Side2 10 AngleBetweenSidesDegrees 30')"
        ),
        "triangle": (
            "length of three sides or coordinates of three points "
            "(e.g., 'Side1 2 Side2 10 Side3 11' "
            "or 'Point1 2 1, Point2 -3 -10, Point3 7 8')"
        ),
        "circle": "radius (e.g., 'Radius 5')",
    }

    while True:
        shape_type = input(
            f"Enter shape type: "
            f"{tuple(available_shapes.keys())} or 'stop' to finish: "
        ).strip().lower()
        if shape_type == "stop":
            break
        if shape_type not in available_shapes:
            print("Invalid shape type. Try again.")
            continue

        shape_info = input(f"Enter {available_shapes[shape_type]}: ").strip()
        try:
            shape_params = proceed_shapes_parametres(shape_info, shape_type)
        except ValueError as e:
            print(f"Error processing parameters: {e}")
            continue

        shapes.append({"shape_name": shape_type, **shape_params})

    return shapes
