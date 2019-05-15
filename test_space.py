import plot_tools as pt
import assistant_algorithms as ass
import mesurement_tools as mesure


def graph_solution(points, seperation):
    all_perms = []
    for k in range(len(points)):
        for rev in range(2):
            per = ass.triple_permutation(seperation[k][0], k, seperation[k][1])
            first_perms = []
            for p in per:
                if rev == 0:
                    p = list(reversed(p))
                first_perms.append([*p])
            len_loop = len(points) - len(first_perms[0])
            for _ in range(len_loop):
                other = []
                perm = first_perms
                for i in range(len(perm)):
                    mid = perm[i][-2]
                    last = perm[i][-1]
                    if mid in seperation[last][0]:
                        for j in range(len(seperation[last][1])):
                            if seperation[last][1][j] not in perm[i]:
                                other.append([*perm[i], seperation[last][1][j]])
                    elif mid in seperation[last][1]:
                        for j in range(len(seperation[last][0])):
                            if seperation[last][0][j] not in perm[i]:
                                other.append([*perm[i], seperation[last][0][j]])
                first_perms = other
            all_perms.append(first_perms)
    return all_perms


def graph_method(num_point, space_size, seed, plot=False):
    points = ass.create_points(num_point, space_size, seed)
    angle_mat = mesure.angle_matrix(points)
    distance_mat = mesure.distance_matrix(points)
    seperation = ass.angle_seperation_with_max(points, angle_mat)
    print(seperation)
    sol_list = graph_solution(points, seperation)
    # print(sol_list[i])
    # tot = 0
    for i in range(num_point):
        min_dist, route = ass.main_route(points, sol_list[i], distance_mat)
        print(min_dist)
    #     if min_dist == float('inf'):
    #         tot += 1
    # return tot

    pt.plot_points(points, space_size, False)
    # return min_dist


num_point = 11
space_size = 100
seed = 41






graph_method(num_point, space_size, seed)

# for i in range(100):
#     tot = graph_method(num_point, space_size, i)
#     if tot == num_point:
#         print('here', i)


points = ass.create_points(num_point, space_size, seed)
angle_mat = mesure.angle_matrix(points)
for ang in angle_mat:
    print(ang)
# seperation = ass.angle_seperation_with_max(points, angle_mat)
# print(seperation)
# pt.plot_points(points, space_size, True)
pt.plot_all_start_in_line(points)
