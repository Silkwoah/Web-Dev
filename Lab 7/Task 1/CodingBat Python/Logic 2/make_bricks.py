def make_bricks(small, big, goal):
    total_length = small + 5 * big
    return total_length >= goal and goal % 5 <= small