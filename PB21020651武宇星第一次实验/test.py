class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

def place_rectangles(container_width, rectangles):
    # Sort rectangles by height in descending order to utilize vertical space efficiently
    rectangles.sort(key=lambda x: x.height, reverse=True)

    current_x = 0
    current_y = 0
    max_row_height = 0

    for rect in rectangles:
        # Check if the rectangle can fit in the current row
        if current_x + rect.width <= container_width:
            rect.x = current_x
            rect.y = current_y
            current_x += rect.width
        else:
            # Move to the next row
            current_y += max_row_height
            max_row_height = 0
            rect.x = 0
            rect.y = current_y
            current_x = rect.width

        # Update the tallest rectangle in the current row
        if rect.height > max_row_height:
            max_row_height = rect.height

    # Print the positions of the rectangles
    for idx, rect in enumerate(rectangles):
        print(f"Rectangle {idx + 1} placed at ({rect.x}, {rect.y}) with size ({rect.width}x{rect.height})")

# Example Usage
rectangles = [Rectangle(3, 2), Rectangle(5, 5), Rectangle(2, 3), Rectangle(6, 1)]
place_rectangles(10, rectangles)
