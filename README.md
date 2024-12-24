# Shape Calculator

## Overview

This project is a Python-based application designed to process geometric shapes, their parameters, and calculate specific properties such as side lengths, perimeter, and area. The program includes modular components for handling shapes, utilities for geometric calculations, and tests for ensuring functionality.

## Features

- **Shape Processing**: Support for various shapes including squares, rectangles, parallelograms, rhombuses, triangles, and circles.
- **Parameter Parsing**: Input is processed to extract shape parameters like side lengths, angles, and coordinates.
- **Validation**: Ensures valid data input (e.g., positive side lengths and angles).
- **Unit Tests**: Comprehensive test suite to verify the functionality of all components.

## Supported Shapes and Inputs

1. **Square**:  
   - Input: `Side <length>` or `TopLeft <x1> <y1> BottomRight <x2> <y2> ...(all angle pairs are allowed)`
   - Example: `Side 4` or `TopLeft 0 0 BottomRight 4 4`

2. **Rectangle**:  
   - Input: `Side1 <length1> Side2 <length2>` or `TopLeft <x1> <y1> BottomRight <x2> <y2>` or `TopRight <x1> <y1> BottomLeft <x2> <y2>`
   - Example: `Side1 4 Side2 5` or `TopLeft 0 0 BottomRight 4 5`

3. **Parallelogram**:  
   - Input: `Side1 <length1> Side2 <length2> AngleBetweenSidesDegrees <angle>`
   - Example: `Side1 4 Side2 6 AngleBetweenSidesDegrees 45`

4. **Rhombus**:  
   - Input: `Side <length> AngleBetweenSidesDegrees <angle>`
   - Example: `Side 4 AngleBetweenSidesDegrees 30`

5. **Triangle**:  
   - Input: `Side1 <length1> Side2 <length2> Side3 <length3>` or `Point1 <x1> <y1> Point2 <x2> <y2> Point3 <x3> <y3>`
   - Example: `Side1 3 Side2 4 Side3 5` or `Point1 0 0 Point2 3 0 Point3 0 4`

6. **Circle**:  
   - Input: `Radius <radius>`
   - Example: `Radius 5`

## Code Structure

1. **`shapes/shapes.py`**  
   - Contains classes for each geometric shape, such as `Square`, `Rectangle`, and `Circle`.

2. **`shapes/utils.py`**  
   - Utility functions for calculations like distance between points and adjacency checks.

3. **`shapes/input_processing.py`**  
   - Processes user input to extract shape parameters.

4. **`tests/`**  
   - Unit tests for each module, ensuring correctness and robustness.

5. **`main.py`**  
   - Entry point for the program. Allows user interaction to input shapes and outputs their properties.

## Running the Program

### Requirements

- Python 3.8 or higher.

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/siaserb/DiversiPy-shape-calculator.git
   cd <repository_folder>
   ```
   
2. Create annd activate a virtual environment on Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Run the main program:
   ```bash
   python main.py
   ```

4. Follow the prompts to input shape data.

### Example Session

```text
Enter shape type: (square, rectangle, parallelogram, rhombus, triangle, circle) or 'stop' to finish: square
Enter side length or coordinates of two angles (e.g., 'Side 2' or 'TopLeft 0 0 BottomRight 4 4'): Side 4
Enter shape type: stop
```

Output:
```text
Square Perimeter: 16 Area: 16
```

## Running Tests

Run all unit tests to ensure functionality:
```bash
python -m unittest discover tests
```

## Error Handling

- Invalid shape inputs raise descriptive exceptions (e.g., "Side length must be positive").
- Incorrect formats or unsupported shapes are handled gracefully.
