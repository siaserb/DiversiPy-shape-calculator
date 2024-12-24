def distance_between_points(point1: tuple, point2: tuple) -> float:
    length_of_point1 = len(point1)
    length_of_point2 = len(point2)
    if length_of_point1 != 2 or length_of_point2 != 2:
        raise Exception("Points must be in 2D")
    for number1, number2 in zip(point1, point2):
        if (
                not isinstance(number1, (int, float))
                or not isinstance(number2, (int, float))
        ):
            raise Exception(
                "Points must be numbers"
            )
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def is_adjacent(name_of_angle1: str, name_of_angle2: str) -> bool:
    names_of_angles = {name_of_angle1, name_of_angle2}

    positions = ("topleft", "topright", "bottomright", "bottomleft")
    if name_of_angle1 not in positions or name_of_angle2 not in positions:
        raise Exception("Angles must be in the following positions: "
                        "TopLeft, TopRight, BottomRight, BottomLeft")
    return (names_of_angles in (
        {positions[0], positions[1]},
        {positions[1], positions[2]},
        {positions[2], positions[3]},
        {positions[3], positions[0]}
    ))


def calculate_sides_from_points(
        coord1: tuple,
        coord2: tuple
) -> float | tuple[float, float]:

    if len(coord1) != len(coord2):
        raise ValueError("Coordinates must be of the same dimension")

    if len(coord1) not in (2, 3):
        raise ValueError("Coordinates must be 2D")

    side1_length = abs(coord2[0] - coord1[0])
    side2_length = abs(coord2[1] - coord1[1])

    if side1_length == side2_length:
        return side1_length

    return side1_length, side2_length
