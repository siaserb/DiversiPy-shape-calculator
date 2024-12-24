from shapes.shapes import (
    Shape,
    Parallelogram,
    Rectangle,
    Square,
    Rhombus,
    Triangle,
    Circle,
)
from shapes.input_processing import collect_shapes


def create_shape_instance(shape_data: dict) -> Shape:
    shape_name = shape_data.pop("shape_name")

    if shape_name == "parallelogram":
        return Parallelogram(**shape_data)
    elif shape_name == "rectangle":
        return Rectangle(**shape_data)
    elif shape_name == "square":
        return Square(**shape_data)
    elif shape_name == "rhombus":
        return Rhombus(**shape_data)
    elif shape_name == "triangle":
        return Triangle(**shape_data)
    elif shape_name == "circle":
        return Circle(**shape_data)
    else:
        raise ValueError(f"Unknown shape type: {shape_name}")


def main():
    shapes_data = collect_shapes()

    for shape_data in shapes_data:
        instance = create_shape_instance(shape_data)
        print(instance)


if __name__ == "__main__":
    main()
