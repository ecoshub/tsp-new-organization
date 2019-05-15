import plot_tools as pt
# import mesurement_tools as mesure
import assistant_algorithms as ass
# import pandas as pd




num_of_points = 10
space_size = 100
seed = 0

points = ass.create_points(num_of_points, space_size, seed)
# distance_mat = mesure.distance_matrix(points)
# for dist in distance_mat:
#     print(max(dist))
# distance_mat = pd.DataFrame(distance_mat)
# print(distance_mat.to_string())

# pt.plot_points(points, True)

# it = line_connections_iter(points, 0)

# for i in it:
#     dev = mesure.deviation_amount(points[i[0]], points[i[1]], points[0])
#     print(i, dev)
#
# pt.plot_all_possibilities(points)
pt.plot_all_possibilities(points)
pt.plot_points(points, True)
# pt.plot_all_start_in_line(points)
