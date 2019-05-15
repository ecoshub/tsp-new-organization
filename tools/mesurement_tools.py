from math import atan, sqrt, pi
from time import time


def calculate_angle(main_point, other_point):
    if main_point[0] == other_point[0]:
        if main_point[1] > other_point[1]:
            angle = 270
            return angle
        elif main_point[1] < other_point[1]:
            angle = 90
            return angle
    if main_point[1] == other_point[1]:
        if main_point[0] > other_point[0]:
            angle = 180
            return angle
        elif main_point[0] < other_point[0]:
            angle = 0
            return angle
    if other_point[0] > main_point[0] and other_point[1] > main_point[1]:
        cof = 0
    elif other_point[0] < main_point[0] and other_point[1] > main_point[1]:
        cof = 180
    elif other_point[0] < main_point[0] and other_point[1] < main_point[1]:
        cof = 180
    elif other_point[0] > main_point[0] and other_point[1] < main_point[1]:
        cof = 360
    deltx = main_point[0] - other_point[0]
    delty = main_point[1] - other_point[1]
    angle = atan(delty / deltx)
    angle = angle / 2 / pi * 360
    angle += cof
    return angle


def angle_matrix(points):
    leng = len(points)
    angle_matrix = [[0 for _ in range(leng)] for _ in range(leng)]
    for i in range(leng):
        for j in range(leng):
            if i != j:
                angle = calculate_angle(points[i], points[j])
                angle_matrix[i][j] = angle
    return angle_matrix


def distance_matrix(points):
    leng = len(points)
    distance_mat = [[0 for _ in range(leng)] for _ in range(leng)]
    for i in range(leng):
        for j in range(leng):
            if i != j:
                distance_mat[i][j] = euclidian_distance(points[i], points[j])
    return distance_mat


def euclidian_distance(first_point, second_point):
    delt_x = first_point[0] - second_point[0]
    delt_y = first_point[1] - second_point[1]
    distance = sqrt(delt_x ** 2 + delt_y ** 2)
    return distance


def corner_point(points):
    sorted_array = []
    len_points = len(points)
    for i in range(len_points):
        sorted_array.append([points[i][0], points[i][1], i])
    sorted_array = sorted(sorted_array, key=lambda x: x[0])
    sorted_array = sorted(sorted_array, key=lambda x: x[1])
    index = sorted_array[0][2]
    return index


def get_center(points):
    sum_x_coordinate = 0
    sum_y_coordinate = 0
    for i, j in points:
        sum_x_coordinate += i
        sum_y_coordinate += j
    len_points = len(points)
    center_x = sum_x_coordinate / len_points
    center_y = sum_y_coordinate / len_points
    return center_x, center_y


def deviation_amount(first_point, second_point, other_point, index_parameters=False):
    base_distance = euclidian_distance(first_point, second_point)
    first_deviation = euclidian_distance(first_point, other_point)
    second_deviation = euclidian_distance(second_point, other_point)
    delta = first_deviation + second_deviation - base_distance
    return delta


def deviation_amount_with_index(first_point, second_point, other_point, distance_mat):
    base_distance = distance_mat[first_point][second_point]
    first_deviation = distance_mat[first_point][other_point]
    second_deviation = distance_mat[second_point][other_point]
    delta = first_deviation + second_deviation - base_distance
    return delta


def minimum_deviation_point(points, target_points, line, distance_mat):
    lent = len(target_points)
    min_dev = float('inf')
    min_dev_point = 0
    for i in range(lent):
        if target_points[i] != line[0] and target_points[i] != line[1]:
            dev = deviation_amount_with_index(line[0], line[1], target_points[i], distance_mat)
            if dev < min_dev:
                min_dev = dev
                min_dev_point = target_points[i]
    return min_dev_point, min_dev


def length_of_the_route(route_polygon, distance_mat=[]):
    length = 0
    lenp = len(route_polygon)
    if len(distance_matrix) > 0:
        for i in range(lenp):
            length += distance_mat[route_polygon[i % lenp]][route_polygon[(i + 1) % lenp]]
    else:
        for i in range(lenp):
            length += euclidian_distance(route_polygon[i % lenp], route_polygon[(i + 1) % lenp])
    return length


def time_spend(func, args, string='__unspecified__', prt=True):
    delt = time()
    func(*args)
    delt = time() - delt
    if prt:
        print('delta time is {} second(s) function name: {}'.format(delt, string))
    return delt


def polygon_area(polygon):
    lenp = len(polygon)
    if lenp < 3:
        return 0
    area = 0
    for i in range(lenp):
        first_cross = polygon[i % lenp][0] * polygon[(i + 1) % lenp][1]
        second_cross = polygon[i % lenp][1] * polygon[(i + 1) % lenp][0]
        area += first_cross - second_cross
    area = abs(area / 2)
    return area


def polygon_area_with_index(points, polygon):
    lenp = len(polygon)
    if lenp < 3:
        return 0
    area = 0
    for i in range(lenp):
        first_cross = points[polygon[i % lenp]][0] * points[polygon[(i + 1) % lenp]][1]
        second_cross = points[polygon[i % lenp]][1] * points[polygon[(i + 1) % lenp]][0]
        area += first_cross - second_cross
    area = abs(area / 2)
    return area


def intersection_check(point_00, point_01, point_10, point_11):
    if point_00 == point_10 or point_00 == point_11 or point_01 == point_10 or point_01 == point_11:
        return False
    first_area = polygon_area([point_00, point_10, point_11])
    second_area = polygon_area([point_01, point_10, point_11])
    tot_area = polygon_area([point_00, point_11, point_01, point_10])
    if tot_area == (first_area + second_area):
        first_area = polygon_area([point_10, point_00, point_01])
        second_area = polygon_area([point_11, point_00, point_01])
        if tot_area == (first_area + second_area):
            return True
    return False
