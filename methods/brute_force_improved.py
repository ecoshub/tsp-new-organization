from math import factorial
from itertools import permutations
from assistant_algorithms import create_points
from tools.mesurement_tools import distance_matrix
from tools.plot_tools import plot_polygon_with_index



def minumum_permutation_calculation(points, distance_mat):
    len_points = len(points)
    index = [each for each in range(len_points)]
    perms = permutations(index, len_points)
    number_of_permutation = int(factorial(len_points - 1))
    current_sum = 0
    minimum_distance = float('inf')
    minimum_permutation = []
    for k in range(number_of_permutation):
        current_permutation = next(perms)
        for i in range(len_points):
            if i == len_points - 1:
                current_distance = distance_mat[current_permutation[i]][current_permutation[0]]
            else:
                current_distance = distance_mat[current_permutation[i]][current_permutation[i + 1]]
            current_sum += current_distance
        if current_sum < minimum_distance:
            minimum_distance = current_sum
            minimum_permutation = current_permutation
        current_sum = 0
    return minimum_distance, minimum_permutation


def brute_force_method(num_point, space_size, seed, plot=False):
    points = create_points(num_point, space_size, seed)
    distance_mat = distance_matrix(points)
    minimum_distance, minimum_permutation = minumum_permutation_calculation(points, distance_mat)
    if plot:
        plot_polygon_with_index(points, minimum_permutation, title=minimum_distance)
    return minimum_distance, minimum_permutation
    # return minimum_distance


# num_point = 11
# space_size = 100
# seed = 298

# brute_force_method(num_point, space_size, seed, plot=True)
