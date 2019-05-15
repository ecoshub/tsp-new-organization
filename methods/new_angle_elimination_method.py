from tools.iteration_tools import point_iterator
from tools.iteration_tools import line_iterator
from tools.mesurement_tools import angle_matrix
from tools.mesurement_tools import distance_matrix
from assistant_algorithms import create_points
from assistant_algorithms import graph_balance
from assistant_algorithms import graph_search
from assistant_algorithms import main_route
from assistant_algorithms import find_exterior_polygon
from assistant_algorithms import add_polygon_to_graph
from tools.plot_tools import plot_polygon_with_index


def has_tolerable_deviation(center, other, target, distance_mat, angle_mat, angle_of_interest):
    if distance_mat[center][other] > distance_mat[center][target]:
        if distance_mat[other][target] < distance_mat[center][other]:
            center_other = angle_mat[center][other]
            center_target = angle_mat[center][target]
            other_center = angle_mat[other][center]
            other_target = angle_mat[other][target]
            other_center_target = abs(center_target - center_other)
            center_other_target = abs(other_center - other_target)
            if other_center_target + center_other_target <= angle_of_interest:
                return True
    return False



def deviation_angle_calculation(points, angle_of_interest, angle_mat, distance_mat):
    main_it = line_iterator(points)
    lenp = len(points)
    graph = [[j for j in range(lenp) if i != j] for i in range(lenp)]
    for main in main_it:
        it = point_iterator(points, main)
        for i in it:
            center = main[0]
            other = main[1]
            target = i
            res = has_tolerable_deviation(center, other, target, distance_mat, angle_mat, angle_of_interest)
            if res:
                if other in graph[center]:
                    graph[center].pop(graph[center].index(other))
                break
        if len(graph[center]) < 2:
            main = (center, graph[center][0])
            it = line_iterator(points, main)
            for i in it:
                res = has_tolerable_deviation(center, i[0], i[1], distance_mat, angle_mat, angle_of_interest)
                if res:
                    break
                else:
                    graph[center].append(i[1])
    return graph




def new_angle_elimination_method(number_of_points, space_size, seed, plot=False):
    angle_of_interest = 60
    points = create_points(number_of_points, space_size, seed)
    distance_mat = distance_matrix(points)
    angle_mat = angle_matrix(points)
    graph = deviation_angle_calculation(points, angle_of_interest, angle_mat, distance_mat)
    exterior = find_exterior_polygon(points, with_indices=True)
    graph = add_polygon_to_graph(exterior, graph)
    graph = graph_balance(graph)
    graph_sol = graph_search(graph)
    dist, route = main_route(points, graph_sol, distance_mat)
    if plot:
        plot_polygon_with_index(points, route)
    return dist


number_of_points = 10
space_size = 100
seed = 202



new_angle_elimination_method(number_of_points, space_size, seed, True)
