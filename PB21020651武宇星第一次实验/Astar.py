import random
import heapq

class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'up':
            self.y += 1
        elif direction == 'down':
            self.y -= 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1

def calculate_overlap(rect1, rect2):
    left = max(rect1.x, rect2.x)
    right = min(rect1.x + rect1.width, rect2.x + rect2.width)
    bottom = max(rect1.y, rect2.y)
    top = min(rect1.y + rect1.height, rect2.y + rect2.height)
    if left < right and bottom < top:
        return (right - left) * (top - bottom)
    return 0

def total_overlap(rectangles):
    total = 0
    n = len(rectangles)
    for i in range(n):
        for j in range(i + 1, n):
            total += calculate_overlap(rectangles[i], rectangles[j])
    return total

def astar_search(rectangles, big_rectangle_width, big_rectangle_height):
    initial_state = [(rect.x, rect.y) for rect in rectangles]
    queue = [(total_overlap(rectangles), 0, initial_state, rectangles)]
    visited = set()
    visited.add(tuple(initial_state))

    while queue:
        current_overlap, cost, state, rects = heapq.heappop(queue)
        if current_overlap == 0:
            return rects

        for rect in rects:
            for direction in ['up', 'down', 'left', 'right']:
                old_x, old_y = rect.x, rect.y
                rect.move(direction)
                if rect.x < 0 or rect.y < 0 or rect.x + rect.width > big_rectangle_width or rect.y + rect.height > big_rectangle_height:
                    rect.x, rect.y = old_x, old_y
                    continue

                new_state = [(r.x, r.y) for r in rects]
                new_state_tuple = tuple(new_state)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    new_overlap = total_overlap(rects)
                    heapq.heappush(queue, (new_overlap, cost + 1, new_state, rects.copy()))
                rect.x, rect.y = old_x, old_y

    return None

print("Enter the number of small rectangles:")
num_rectangles = int(input())
print("Enter the width of the large rectangle:")
big_rectangle_width = int(input())
print("Enter the height of the large rectangle:")
big_rectangle_height = int(input())

small_rectangles = []
for i in range(num_rectangles):
    print(f"Enter the width of small rectangle {i+1}:")
    width = int(input())  
    print(f"Enter the height of small rectangle {i+1}:")
    height = int(input())
    x = random.randint(0, big_rectangle_width - width)
    y = random.randint(0, big_rectangle_height - height)
    small_rectangles.append(Rectangle(width, height, x, y))

result = astar_search(small_rectangles, big_rectangle_width, big_rectangle_height)
if result:
    for idx, rect in enumerate(result):
        print(f"Rectangle {idx + 1} at position: ({rect.x}, {rect.y})")
else:
    print("No solution found")
