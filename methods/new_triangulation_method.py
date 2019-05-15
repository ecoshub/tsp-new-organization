from tools.mesurement_tools import distance_matrix
from tools.mesurement_tools import deviation_amount_with_index
from tools.mesurement_tools import intersection_check
from assistant_algorithms import create_points
from assistant_algorithms import graph_balance
from assistant_algorithms import graph_search
from assistant_algorithms import main_route
from assistant_algorithms import find_exterior_polygon
from assistant_algorithms import add_polygon_to_graph
from assistant_algorithms import eliminate_list
from tools.plot_tools import plot_polygon_with_index


def minimum_deviation_point_to_polygon(points, exterior, distance_mat, new_points, graph):
    main_min = float('inf')
    main_mem = [0, 0, 0]
    lenx = len(exterior)
    lenp = len(new_points)
    for i in range(lenp):
        min_side = float('inf')
        mem_side = [0, 0, 0]
        for j in range(lenx):
            dev = deviation_amount_with_index(exterior[j % lenx], exterior[(j + 1) % lenx], new_points[i], distance_mat)
            temp_mem = [j % lenx, (j + 1) % lenx, i]
            if dev < min_side:
                min_side = dev
                mem_side = temp_mem
        if min_side < main_min:
            main_min = min_side
            main_mem = mem_side
    graph[new_points[main_mem[2]]].append(exterior[main_mem[0]])
    graph[new_points[main_mem[2]]].append(exterior[main_mem[1]])
    exterior.insert(main_mem[1], new_points[main_mem[2]])
    new_points.pop(main_mem[2])
    return new_points, exterior, graph


def first_step(number_of_points, space_size, seed):
    points = create_points(number_of_points, space_size, seed)
    distance_mat = distance_matrix(points)
    ext = find_exterior_polygon(points, True)
    graph = [[] for j in range(len(points))]
    graph = add_polygon_to_graph(ext, graph)
    point_indices = [each for each in range(len(points))]
    new_points = eliminate_list(point_indices, ext)
    lenp = len(new_points)
    for _ in range(lenp):
        new_points, ext, graph = minimum_deviation_point_to_polygon(points, ext, distance_mat, new_points, graph)
        # pt.plot_graph(points, graph)
    graph = graph_balance(graph)
    return points, distance_mat, graph, ext


def control_all_intersections(points, graph, line):
    leng = len(graph)
    for i in range(leng):
        for j in range(len(graph[i])):
            if i == line[0] and graph[i][j] == line[1]:
                return True
            if i == line[1] and graph[i][j] == line[0]:
                return True
            res = intersection_check(points[line[0]], points[line[1]], points[i], points[graph[i][j]])
            if res:
                return True
    return False



def second_step(points, graph, ext, distance_mat):
    lenx = len(ext)
    if lenx > 4:
        min_dev = float('inf')
        mem = 0
        for i in range(lenx):
            first = ext[i % lenx]
            second = ext[(i + 1) % lenx]
            other = ext[(i + 2) % lenx]
            dist = distance_mat[first][other]

            # dev = deviation_amount_with_index(first, second, other, distance_mat)
            # dist = dist + dev

            l0 = distance_mat[first][second]
            l1 = distance_mat[first][other]
            l2 = distance_mat[second][other]
            lx = float(min(l0, l1, l2))
            delt = (l0 * l1 * l2) / lx ** 3
            delt = abs(1 / delt)
            dist = dist + delt

            # min_area = lx ** 2 * 1.73205080757 / 4
            # small_area = polygon_area([points[first], points[second], points[other]])
            # prop = 1 / (1 - min_area / small_area)
            # print(delt)

            # dist = polygon_area([points[first], points[second], points[other]])

            # temp_ext = [i for i in range(len(ext)) if i != second]
            # big_area = polygon_area_and_polygon(points, temp_ext)
            # dist = big_area / small_area


            res = control_all_intersections(points, graph, [first, other])
            temp_mem = [first, second, other, dist]
            if res is False:
                if dist < min_dev:
                    min_dev = dist
                    mem = temp_mem

        graph[mem[2]].append(mem[0])
        graph[mem[0]].append(mem[2])
        ext.pop(ext.index(mem[1]))
    else:
        res_1 = control_all_intersections(points, graph, [ext[0], ext[2]])
        res_2 = control_all_intersections(points, graph, [ext[1], ext[3]])
        dist_1 = distance_mat[ext[0]][ext[2]]
        dist_2 = distance_mat[ext[1]][ext[3]]
        if dist_1 < dist_2:
            if res_1 is False:
                graph[ext[0]].append(ext[2])
                graph[ext[2]].append(ext[0])
                ext = []
            else:
                graph[ext[1]].append(ext[3])
                graph[ext[3]].append(ext[1])
                ext = []
        else:
            if res_2 is False:
                graph[ext[1]].append(ext[3])
                graph[ext[3]].append(ext[1])
                ext = []
            else:
                graph[ext[0]].append(ext[2])
                graph[ext[2]].append(ext[0])
                ext = []
    return graph, ext


def triangulation_method(number_of_points, space_size, seed, plot=False):
    points, distance_mat, graph, ext = first_step(number_of_points, space_size, seed)
    # pt.plot_graph(points, graph)
    while len(ext) > 3:
        graph, ext = second_step(points, graph, ext, distance_mat)
        # pt.plot_graph(points, graph)
    graph_sol = graph_search(graph)
    dist, route = main_route(points, graph_sol, distance_mat)
    if plot:
        plot_polygon_with_index(points, route)
    return dist


# number_of_points = 10
# space_size = 100
# seed = 202


# dist = triangulation_method(number_of_points, space_size, seed, True)
# print(dist)
# time_spend(triangulation_method, (number_of_points, space_size, seed, False), 'triangulation_method')
