from tools.mesurement_tools import angle_matrix
from tools.mesurement_tools import distance_matrix
from assistant_algorithms import create_points
from assistant_algorithms import angle_seperation
from assistant_algorithms import graph_balance
from assistant_algorithms import graph_search
from assistant_algorithms import main_route
from tools.plot_tools import plot_polygon_with_index



def harmonic_mean_angle_seperation(angle_sep):
    all_seperations = []
    for i in range(len(angle_sep)):
        tot_har = 0
        count = 0
        leni = len(angle_sep[i])
        for j in range(leni):
            if angle_sep[i][j][3] <= 180:
                if angle_sep[i][j][3] != 0:
                    tot_har += 1 / float(angle_sep[i][j][3])
                count += 1
        tot_har = float(count) / tot_har
        row_seperation = []
        temp = []
        for j in range(leni):
            if angle_sep[i][j][3] < tot_har:
                temp.append(angle_sep[i][j][1])
            else:
                if len(temp) > 0:
                    row_seperation.append(temp)
                    temp = []
                    temp.append(angle_sep[i][j][1])
                else:
                    temp.append(angle_sep[i][j][1])
            if j == leni - 1:
                if angle_sep[i][j][3] > tot_har:
                    if angle_sep[i][0][3] > tot_har:
                        row_seperation.append([angle_sep[i][j][1]])
                    else:
                        row_seperation[0].append(angle_sep[i][j][1])
                else:
                    if angle_sep[i][0][3] > tot_har:
                        row_seperation[-1].append(angle_sep[i][j][1])
                    else:
                        row_seperation[-1].append(angle_sep[i][j][1])
                        row_seperation[0] = [row_seperation[0][0], *row_seperation[-1]]
        all_seperations.append(row_seperation)
    return all_seperations



def find_min_dist(center, seperation_list, distance_mat):
    lens = len(seperation_list)
    if lens == 1:
        return seperation_list[0]
    else:
        min_dist = float('inf')
        min_po = 0
        for i in range(lens):
            dist = distance_mat[center][seperation_list[i]]
            if dist < min_dist:
                min_dist = dist
                min_po = seperation_list[i]
        return min_po


def elemination_with_nearst(points, seperation, distance_mat):
    lens = len(seperation)
    new_graph = []
    for i in range(lens):
        new_row = []
        for j in range(len(seperation[i])):
            new_row.append(find_min_dist(i, seperation[i][j], distance_mat))
        new_graph.append(new_row)
    return new_graph


def mean_angle_elemination_method(number_of_points, space_size, seed, plot=False):
    points = create_points(number_of_points, space_size, seed)
    angle_mat = angle_matrix(points)
    distance_mat = distance_matrix(points)
    angle_sep = angle_seperation(points, angle_mat)
    seperation = harmonic_mean_angle_seperation(angle_sep)
    new_graph = elemination_with_nearst(points, seperation, distance_mat)
    new_graph = graph_balance(new_graph)
    graph_sol = graph_search(new_graph)
    dist, route = main_route(points, graph_sol, distance_mat)
    # pt.plot_graph(points, new_graph)
    if plot:
        plot_polygon_with_index(points, route)
    return dist



number_of_points = 10
space_size = 100
seed = 202

mean_angle_elemination_method(number_of_points, space_size, seed, False)
