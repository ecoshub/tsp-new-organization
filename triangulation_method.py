from tools.mesurement_tools import distance_matrix
from tools.mesurement_tools import deviation_amount_with_index
from tools.mesurement_tools import intersection_check
from tools.mesurement_tools import minimum_deviation_point
from assistant_algorithms import create_points
from assistant_algorithms import graph_balance
from assistant_algorithms import find_exterior_polygon
from assistant_algorithms import add_polygon_to_graph
from assistant_algorithms import eliminate_list
from tools.plot_tools import plot_graph



def minimum_deviation_exterior_polygon(points, exterior, distance_mat, new_points, graph):
    deviations = []
    for i in range(len(new_points)):
        min_dev = float('inf')
        mem = []
        for j in range(len(exterior)):
            if j == len(exterior) - 1:
                dev = deviation_amount_with_index(exterior[j], exterior[0], new_points[i], distance_mat)
                temp_mem = [dev, exterior[j], exterior[0], new_points[i]]
            else:
                dev = deviation_amount_with_index(exterior[j], exterior[j + 1], new_points[i], distance_mat)
                temp_mem = [dev, exterior[j], exterior[j + 1], new_points[i]]
            if dev < min_dev:
                min_dev = dev
                mem = temp_mem
        deviations.append(mem)

    deviations = sorted(deviations, key=lambda x: x[0])
    graph[deviations[0][3]].append(deviations[0][1])
    graph[deviations[0][3]].append(deviations[0][2])
    new_points.pop(new_points.index(deviations[0][3]))
    exterior.insert(exterior.index(deviations[0][2]), deviations[0][3])
    return new_points, exterior, graph


def method_1(number_of_points, space_size, seed):
    points = create_points(number_of_points, space_size, seed)
    distance_mat = distance_matrix(points)
    ext = find_exterior_polygon(points, True)
    graph = [[] for j in range(len(points))]
    graph = add_polygon_to_graph(ext, graph)
    new_points = eliminate_list([each for each in range(len(points))], ext)
    lenp = len(new_points)
    for _ in range(lenp):
        new_points, ext, graph = minimum_deviation_exterior_polygon(points, ext, distance_mat, new_points, graph)
    graph = graph_balance(graph)
    while len(ext) > 2:
        ext, graph = graph_correction(points, ext, graph, distance_mat)
        # plot_graph(points, graph)
    return ext, graph



def graph_correction(points, ext, graph, distance_mat):
    lenx = len(ext)
    if lenx > 4:
        min_dist = float('inf')
        mem = 0
        for i in range(lenx):
            if i < lenx - 2:
                first = ext[i]
                second = ext[i + 1]
                third = ext[i + 2]
            else:
                if i == lenx - 2:
                    first = ext[i]
                    second = ext[0]
                    third = ext[1]
                if i == lenx - 1:
                    first = ext[i]
                    second = ext[1]
                    third = ext[2]
            dist = distance_mat[first][third]
            temp_mem = [first, second, third, dist]
            for i in range(len(graph)):
                for j in range(len(graph[i])):
                    res = intersection_check(points[first], points[third], points[i], points[graph[i][j]])
                    if res:
                        print(points[i], points[graph[i][j]])
            if res is False:
                if third not in graph[first]:
                    if first not in graph[third]:
                        if dist < min_dist:
                            min_dist = dist
                            mem = temp_mem

        print(mem)
        ext.pop(ext.index(mem[1]))
        graph[mem[0]].append(mem[2])
        graph[mem[2]].append(mem[0])
    else:
        dist_1 = distance_mat[ext[0]][ext[2]]
        dist_2 = distance_mat[ext[1]][ext[3]]
        if dist_1 <= dist_2:
            graph[ext[0]].append(ext[2])
            graph[ext[2]].append(ext[0])
            ext = []
        else:
            graph[ext[1]].append(ext[3])
            graph[ext[3]].append(ext[1])
            ext = []
    return ext, graph



def is_exterior(line, exterior_polygon):
    lenx = len(exterior_polygon)
    for i in range(lenx):
        if i == lenx - 1:
            first = exterior_polygon[i]
            second = exterior_polygon[0]
        else:
            first = exterior_polygon[i]
            second = exterior_polygon[i + 1]
        if line == [first, second] or line == [second, first]:
            return True
    return False



def asd(points, new_points, exts, exteriors, graph, distance_mat):
    lene = len(exts)
    min_dev = float('inf')
    min_curr = 0
    min_point = 0
    for i in range(lene):
        curr = exts[i]
        min_dev_point, dev = minimum_deviation_point(points, new_points, curr, distance_mat)
        if dev < min_dev:
            min_dev = dev
            min_curr = curr
            min_point = min_dev_point
    curr = min_curr
    min_dev_point = min_point
    graph[curr[0]].append(min_dev_point)
    graph[curr[1]].append(min_dev_point)
    graph[min_dev_point].append(curr[0])
    graph[min_dev_point].append(curr[1])
    exts.append([curr[0], min_dev_point])
    exts.append([curr[1], min_dev_point])
    exts.pop(exts.index(curr))
    new_points.pop(new_points.index(min_dev_point))
    new_exts = []
    for i in range(len(exts)):
        res = is_exterior(exts[i], exteriors)
        if res is False:
            new_exts.append(exts[i])
    exts = new_exts
    new_points = eliminate_list(new_points, curr)
    return exts, new_points, graph


def method_2(number_of_points, space_size, seed):
    points = create_points(number_of_points, space_size, seed)
    distance_mat = distance_matrix(points)
    graph = [[] for j in range(len(points))]
    exteriors = find_exterior_polygon(points, True)
    ext = exteriors[:2]
    exts = [ext]
    graph[exts[0][0]].append(exts[0][1])
    graph[exts[0][1]].append(exts[0][0])
    new_points = eliminate_list([each for each in range(len(points))], exts[0])
    lenx = len(new_points)
    for _ in range(lenx):
        exts, new_points, graph = asd(points, new_points, exts, exteriors, graph, distance_mat)
    print(exts)
    # graph = add_exterrior_polygon(points, graph)
    plot_graph(points, graph)





def minimum_deviation_line(points, line, distance_mat):
    lenp = len(points)
    min_dev = float('inf')
    min_index = 0
    for i in range(lenp):
        if i != line[0] and i != line[1]:
            dev = deviation_amount_with_index(line[0], line[1], i, distance_mat)
            if dev < min_dev:
                min_dev = dev
                min_index = i
    return min_index, min_dev



def inner_method(points, ext, graph, distance_mat):
    lenx = len(ext)
    general_min_dev = float('inf')
    mem = 0
    for i in range(lenx):
        done = False
        if i == lenx - 1:
            first = ext[i]
            second = ext[0]
        else:
            first = ext[i]
            second = ext[i + 1]
        first_dev, dev_1 = minimum_deviation_line(points, [first, second], distance_mat)
        second_dev, dev_2 = minimum_deviation_line(points, [first, first_dev], distance_mat)
        tot_dev = dev_1 + dev_2
        temp_mem = [first, second, first_dev]
        if second_dev == second:
            done = True
        if tot_dev < general_min_dev and done:
            general_min_dev = tot_dev
            mem = temp_mem

    graph[mem[2]].append(mem[0])
    graph[mem[0]].append(mem[2])
    ext.pop(ext.index(mem[1]))
    return ext, graph







number_of_points = 10
space_size = 100
seed = 0


method_1(number_of_points, space_size, seed)

# method_2(number_of_points, space_size, seed)
