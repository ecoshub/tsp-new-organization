from multiprocessing import Pool, cpu_count
from tools.mesurement_tools import distance_matrix
from assistant_algorithms import create_points
from itertools import islice, permutations, repeat
from tools.plot_tools import plot_polygon_with_index
from math import factorial


def iters_local_min(args):
    iterable, distance_mat, num_point = args
    current_sum = 0
    minimum_distance = float('inf')
    for current_permutation in iterable:
        current_sum = 0
        for i in range(num_point):
            current_distance = distance_mat[current_permutation[i % num_point]][current_permutation[(i + 1) % num_point]]
            current_sum += current_distance
        if current_sum < minimum_distance:
            minimum_distance = current_sum
            minimum_permutation = current_permutation
    return minimum_distance, minimum_permutation


def minumum_permutation_calculation(distance_mat, num_point):
    index = [each for each in range(num_point)]
    perms = permutations(index, num_point)
    number_of_circular_permutation = int(factorial(num_point - 1))
    reduced_permutations = islice(perms, 0, number_of_circular_permutation)
    iter_slice_list = slice_iter(reduced_permutations, number_of_circular_permutation, cpu_count())
    p = Pool()
    args = zip(iter_slice_list, repeat(distance_mat), repeat(num_point))
    res = p.map(iters_local_min, args)
    p.close()
    p.join()
    return res


def slice_iter(iterable, total_iteration, number_of_slice):
    iter_list = []
    batch_size = int(total_iteration / number_of_slice + 0.5)
    for i in range(0, total_iteration, batch_size):
        start = i
        end = i + batch_size
        if end > total_iteration:
            end = total_iteration
        it = islice(iterable, start, end)
        iter_list.append(it)
    return iter_list



def brute_force_improved_multiprocessing(num_point, space_size, seed, plot=False):
    if __name__ == '__main__':
        points = create_points(num_point, space_size, seed)
        distance_mat = distance_matrix(points)
        res = minumum_permutation_calculation(distance_mat, num_point)
        res = sorted(res)
        minimum_distance, minimum_permutation = res[0]
        if plot:
            plot_polygon_with_index(points, minimum_permutation, title=minimum_distance)
        return minimum_distance, minimum_permutation
        # return minimum_distance





# num_point = 11
# space_size = 100
# seed = 298

# brute_force_improved_multiprocessing(num_point, space_size, seed, True)

