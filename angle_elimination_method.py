from tools import mesurement_tools as mesure
from tools import plot_tools as pt
from assistant_algorithms import create_points
from assistant_algorithms import add_polygon_to_graph
from assistant_algorithms import graph_balance
from assistant_algorithms import graph_search
from assistant_algorithms import main_route


def elemination_with_certain_angle(points, angle_mat, angle_of_interest):
    lenp = len(points)
    new_graph = []
    for i in range(lenp):
        temp_con = []
        for j in range(lenp):
            tot_res = 0
            for k in range(lenp):
                if i != j and j != k and i != k:
                    center = i
                    seconder = j
                    other = k
                    res, tot = total_deviation(angle_mat, center, seconder, other, angle_of_interest)
                    if res:
                        break
                    else:
                        tot_res += 1
            if tot_res == lenp - 2:
                temp_con.append(j)
        if len(temp_con) < 2:
            el = temp_con[0]
            temp_con = []
            for j in range(lenp):
                tot_res = 0
                for k in range(lenp):
                    if i != j and j != k and i != k and k != el:
                        center = i
                        seconder = j
                        other = k
                        res, tot = total_deviation(angle_mat, center, seconder, other, angle_of_interest)
                        if res:
                            break
                        else:
                            tot_res += 1
                if tot_res == lenp - 3:
                    temp_con.append(j)
            temp_con.append(el)
        new_graph.append(temp_con)
    return new_graph




def total_deviation(angle_mat, center, seconder, other, angle_of_interest):
    res = False

    first_angle = angle_mat[seconder][other] - angle_mat[seconder][center]
    second_angle = angle_mat[center][other] - angle_mat[center][seconder]
    first_angle = abs(first_angle)
    second_angle = abs(second_angle)
    if first_angle > 180:
        first_angle = 360 - first_angle
    if second_angle > 180:
        second_angle = 360 - second_angle
    tot = first_angle + second_angle
    if tot <= angle_of_interest:
        res = True
    return res, tot



def angle_elimination_method(number_of_points, space_size, seed, plot=False):
    angle_of_interest = 60
    points = create_points(number_of_points, space_size, seed)
    distance_mat = mesure.distance_matrix(points)
    angle_mat = mesure.angle_matrix(points)
    graph = elemination_with_certain_angle(points, angle_mat, angle_of_interest)
    graph = add_polygon_to_graph(points, graph)
    graph = graph_balance(graph)
    graph_sol = graph_search(graph, number_of_points)
    dist, route = main_route(points, graph_sol, distance_mat)
    if plot:
        pt.plot_polygon_with_index(points, route)
    return dist
