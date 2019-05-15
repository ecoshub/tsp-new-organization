from tools.mesurement_tools import corner_point
from tools.mesurement_tools import get_center
from tools.mesurement_tools import calculate_angle
from random import seed as sd
from random import sample


def create_points(point_num, space_size, seed):
    sd(seed)
    x_es = [i + 1 for i in range(space_size)]
    y_es = [i + 1 for i in range(space_size)]
    sel_x = sample(x_es, point_num)
    sel_y = sample(y_es, point_num)
    points = list(zip(sel_x, sel_y))
    return points


def find_exterior_polygon(points, with_indices=False):
    starting_index = corner_point(points)
    selected_index = starting_index
    selected = points[selected_index]
    center = get_center(points)
    exterior_polygon = []
    stop = True
    while(stop):
        min_angle = float('inf')
        index = 0
        first_lines_angle = calculate_angle(selected, center) + 180
        for i in range(len(points)):
            if i != selected_index:
                second_lines_angle = calculate_angle(selected, points[i])
                delta_angle = (second_lines_angle - first_lines_angle) % 360
                if delta_angle < min_angle:
                    min_angle = delta_angle
                    index = i
        selected_index = index
        selected = points[selected_index]
        if with_indices:
            exterior_polygon.append(selected_index)
        else:
            exterior_polygon.append(selected)
        if selected_index == starting_index:
            stop = False
    return exterior_polygon


def exterior_polygon_circular(points, cir_sort, return_index=False):
    lenp = len(cir_sort[0])
    befour = corner_point(points)
    last = cir_sort[befour][0]
    stop = True
    ext_index = []
    ext_points = []
    ext_index.append(befour)
    ext_index.append(last)
    ext_points.append(points[befour])
    ext_points.append(points[last])
    while(stop):
        index = cir_sort[last].index(befour)
        if index == lenp - 1:
            befour = last
            last = cir_sort[last][0]
        else:
            befour = last
            last = cir_sort[last][index + 1]
        if ext_index[0] == last:
            stop = False
            if return_index:
                return ext_index
            else:
                return ext_points
        else:
            ext_index.append(last)
            ext_points.append(points[last])
    return -1


def circular_sort(points, angle_mat):
    len_ang = len(angle_mat)
    cir_sort = [[0 for each in range(len_ang - 1)] for each in range(len_ang)]
    for i in range(len_ang):
        new_row = []
        for j in range(len_ang):
            new_row.append([angle_mat[i][j], j])
        new_row = sorted(new_row)
        for j in range(1, len_ang):
            cir_sort[i][j - 1] = new_row[j][1]
    return cir_sort


def max_angle_differences(diff_list):
    sorted_diffs = sorted(diff_list, key=lambda x: x[2], reverse=True)
    maxes = sorted([sorted_diffs[0][3], sorted_diffs[1][3]])
    list_1 = []
    list_2 = []
    for i in range(len(diff_list)):
        if i >= maxes[0] and i < maxes[1]:
            list_1.append(diff_list[i][1])
        else:
            list_2.append(diff_list[i][1])
    return [list_1, list_2]


def angle_seperation_with_max(points, angle_mat):
    len_ang = len(angle_mat)
    seperation = []
    for i in range(len_ang):
        new_row = []
        for j in range(len_ang):
            new_row.append([angle_mat[i][j], j])
        new_row = sorted(new_row)
        jumps = []
        for j in range(1, len_ang):
            if j == len_ang - 1:
                delt_ang = new_row[1][0] - new_row[j][0]
                delt_ang = delt_ang % 360
                delt = [new_row[j][1], new_row[1][1], delt_ang, j - 1]
            else:
                delt_ang = new_row[j + 1][0] - new_row[j][0]
                delt_ang = delt_ang % 360
                delt = [new_row[j][1], new_row[j + 1][1], delt_ang, j - 1]
            jumps.append(delt)
        jumps = max_angle_differences(jumps)
        seperation.append(jumps)
    return seperation


def angle_seperation(points, angle_mat):
    len_ang = len(angle_mat)
    seperation = []
    for i in range(len_ang):
        new_row = []
        for j in range(len_ang):
            new_row.append([angle_mat[i][j], j])
        new_row = sorted(new_row)
        jumps = []
        for j in range(1, len_ang):
            if j == len_ang - 1:
                delt_ang = new_row[1][0] - new_row[j][0]
                delt_ang = delt_ang % 360
                delt = [new_row[j][1], new_row[1][1], j - 1, delt_ang]
            else:
                delt_ang = new_row[j + 1][0] - new_row[j][0]
                delt_ang = delt_ang % 360
                delt = [new_row[j][1], new_row[j + 1][1], j - 1, delt_ang]
            jumps.append(delt)
        seperation.append(jumps)
    return seperation


def eliminate_list(main_list, elimination_list):
    new_list = []
    for el in main_list:
        if el not in elimination_list:
            new_list.append(el)
    return new_list


def main_route(points, sol_list, distance_mat):
    lens = len(sol_list)
    min_dist = float('inf')
    for i in range(lens):
        lenss = len(sol_list[i])
        temp_dist = 0
        for j in range(lenss):
            temp_dist += distance_mat[sol_list[i][j % lenss]][sol_list[i][(j + 1) % lenss]]
        if temp_dist < min_dist:
            min_dist = temp_dist
            main_route = sol_list[i]
    return min_dist, main_route


def graph_search(graph):
    leng = len(graph)
    possible_routes = [[0, graph[0][i]] for i in range(len(graph[0]))]
    for _ in range(leng - 2):
        final = []
        for i in range(len(possible_routes)):
            after = possible_routes[i][-1]
            curr = possible_routes[i]
            temp = []
            for j in range(len(graph[after])):
                if graph[after][j] not in curr:
                    temp.append([*curr, graph[after][j]])
            for j in range(len(temp)):
                final.append(temp[j])
        possible_routes = final
    return possible_routes


def add_polygon_to_graph(polygon, graph):
    lenx = len(polygon)
    for i in range(lenx):
        befour = polygon[(i - 1) % lenx]
        after = polygon[(i + 1) % lenx]
        if after not in graph[polygon[i]]:
            graph[polygon[i]].append(after)
        if befour not in graph[polygon[i]]:
            graph[polygon[i]].append(befour)
    return graph


def graph_balance(graph):
    leng = len(graph)
    for i in range(leng):
        for j in range(len(graph[i])):
            if i not in graph[graph[i][j]]:
                graph[graph[i][j]].append(i)
    return graph


def indices_to_points(points, index_list):
    new_list = []
    leni = len(index_list)
    for i in range(leni):
        new_list.append(points[index_list[i]])
    return new_list
