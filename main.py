import numpy as np
import matplotlib.pyplot as plt
from point import Point

n = 25
m = 0
x_value_range = 10
x_value = x_value_range * np.random.rand(n, 1)

# Initial point
initial_point = Point(4, 4)
plt.scatter(initial_point.x, initial_point.y, color="#ff0000", s=100)

# Randomize values arround linear function
y_value = m * x_value + 5 + np.random.randn(n, 1)


point_list = []
for i in range(n):
    point = Point(x_value[i], y_value[i])
    point_list.append(point)


# Sort points by distance with initial point
def sort_point_by_distance(point, points: list) -> list:
    """
    This function returns a sorted point list by the euclidean distance
    between a reference point and the rest of the points

    Parameters:
        point (Point): Reference point
        points (list): List of points

    Returns:
        list: List of sorted points
    """
    for i in range(len(points)):  # pylint: disable=C0200
        min_idx = i
        min_distance = point.distance_to(points[min_idx])
        for j in range(i + 1, len(points)):
            if point.distance_to(points[j]) < min_distance:
                min_idx = j
                min_distance = point.distance_to(points[j])

        points[min_idx], points[i] = points[i], points[min_idx]
    return points


sorted_points = sort_point_by_distance(initial_point, point_list)

for i in sorted_points:
    print(i.x, i.y, initial_point.distance_to(i))

for point in point_list:
    plt.scatter(point.x, point.y, color='#0800ff', s=60)
plt.show()
