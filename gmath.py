import math
from display import *


# vector functions
# normalize vector, should modify the parameter
def normalize(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    magnitude = math.sqrt(x * x + y * y + z * z)
    vector[0] = x / magnitude
    vector[1] = y / magnitude
    vector[2] = z / magnitude
    return vector


# Return the dot product of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


# Calculate the surface normal for the triangle whose first
# point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = polygons[i]
    p1 = polygons[i + 1]
    p2 = polygons[i + 2]

    a = [p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]]
    b = [p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]]

    normal = [0, 0, 0]
    normal[0] = a[1] * b[2] - a[2] * b[1]
    normal[1] = a[2] * b[0] - a[0] * b[2]
    normal[2] = a[0] * b[1] - a[1] * b[0]
    return normal
