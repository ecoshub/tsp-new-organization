from tools import mesurement_tools as mesure
from tools import assistant_algorithms as ass
from tools import plot_tools as pt


def minimum_deviations(wrap_list, array, distance_matrix):
    min_delt = float('inf')
    len_wrap = len(wrap_list)
    len_array = len(array)
    main_mem = []
    all_minimals = []
    for i in range(len_array):
        for j in range(len_wrap):
            if j == len_wrap - 1:
                temp_delt = mesure.deviation_amount(wrap_list[j], wrap_list[0], array[i])
                mem = [temp_delt, j, 0, i, wrap_list[j], wrap_list[0], array[i]]
            else:
                temp_delt = mesure.deviation_amount(wrap_list[j], wrap_list[j + 1], array[i])
                mem = [temp_delt, j, j + 1, i, wrap_list[j], wrap_list[j + 1], array[i]]
            if temp_delt < min_delt:
                min_delt = temp_delt
                main_mem = mem
        all_minimals.append(main_mem)
        min_delt = float('inf')
        main_mem = []
    return all_minimals


def merge_all(num_point, space_size, seed, pp):
    points = ass.create_points(num_point, space_size, seed)
    distance_matrix = mesure.distance_matrix(points)
    wrap_list = ass.find_exterior_polygon(points)
    new_points = []
    for i in range(len(points)):
        if points[i] not in wrap_list:
            new_points.append(points[i])
    for _ in range(len(new_points)):
        min_dev = minimum_deviations(wrap_list, new_points, distance_matrix)
        min_dev = sorted(min_dev, key=lambda x: x[0], reverse=False)
        max_dev = min_dev[0]
        wrap_list.insert(max_dev[2], new_points[max_dev[3]])
        new_points.pop(max_dev[3])  # sns.set()
    leng = mesure.length_of_the_route(wrap_list)
    if pp:
        pt.plot_polygon(wrap_list, space_size, True)
    return leng


num_point = 10
space_size = 100
seed = 11

asd = merge_all(num_point, space_size, seed, False)
print(asd)
