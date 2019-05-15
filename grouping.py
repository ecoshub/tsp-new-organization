




# pt.plot_points(points, True)


# def cal_con(node, angle_mat):
#     lena = len(angle_mat)
#     all_tot = []
#     for j in range(lena):
#         second = j
#         tot = 0
#         c = 0
#         for i in range(len(angle_mat)):
#             if i != j:
#                 if i != node and i != second:
#                     first_ang = angle_mat[i][node]
#                     second_ang = angle_mat[i][second]
#                     first_ang = 360 - first_ang
#                     second_ang = 360 - second_ang
#                     delt = second_ang - first_ang
#                     if delt > 180:
#                         delt = 360 - delt
#                     delt = abs(delt)
#                     c += 1
#                     tot += delt
#         print(tot / c)
#         all_tot.append([tot / c, node, second])
#     all_tot = sorted(all_tot, key=lambda x: x[0])
#     print()
#     return (all_tot[1][1], all_tot[1][2])



# def geometric_center(points):
#     tot_x = 1
#     tot_y = 1
#     c = 0
#     for i in range(len(points)):
#         tot_x *= points[i][0]
#         tot_y *= points[i][1]
#         c += 1
#     return tot_x ** (1 / float(c)), tot_y ** (1 / float(c))







# def tot_dist_to_cent(points, center, center_index, labels):
#     dist = 0
#     for i in range(len(points)):
#         if labels[i] == center_index:
#             dist += mesure.euclidian_distance(center, points[i])
#     return dist


# def centers_tots(points, centers, labels):
#     gen_tot = 0
#     for i in range(len(centers)):
#         tot = tot_dist_to_cent(points, centers[i], i, labels)
#         gen_tot += tot
#     return gen_tot



# def cul_with(points, k):
#     cul = km(k)
#     cul = cul.fit(points)
#     centers = cul.cluster_centers_
#     for c in centers:
#         pt.plot_point(points, c)
#     pt.plot_points(points, True)
#     return centers




# def diff_plot(points):
#     list_dist = []
#     for i in range(1, len(points)):
#         cul = km(i)
#         cul = cul.fit(points)
#         centers = cul.cluster_centers_
#         labels = cul.labels_
#         tot = centers_tots(points, centers, labels)
#         list_dist.append(tot)


#     diff = []
#     for i in range(len(list_dist) - 1):
#         diff.append(list_dist[i] - list_dist[i + 1])
#     plt.plot(diff)
#     plt.show()




# def my_cul(points):
#     lenp = len(points)
#     x_sorted = sorted(points, key=lambda x: x[0])
#     y_sorted = sorted(points, key=lambda x: x[1])
#     print(x_sorted)
#     print(y_sorted)
#     x_diff = []
#     y_diff = []
#     for i in range(lenp - 1):
#         x_diff.append(x_sorted[i + 1][0] - x_sorted[i][0])
#         y_diff.append(y_sorted[i + 1][1] - y_sorted[i][1])
#     x_avg = sum(x_diff) / (lenp - 1)
#     y_avg = sum(y_diff) / (lenp - 1)
#     print(x_diff, x_avg)
#     print(y_diff, y_avg)
#     plt.plot(x_diff, label='x diff')
#     plt.plot(y_diff, label='y diff')
#     plt.plot([0, 10], [x_avg, x_avg], label='x avg')
#     plt.plot([0, 10], [y_avg, y_avg], label='y avg')
#     tot_x = 0
#     tot_y = 0
#     for i in range(len(x_diff)):
#         if x_diff[i] >= x_avg:
#             tot_x += 1
#         if y_diff[i] >= y_avg:
#             tot_y += 1
#     print(tot_x, tot_y, tot_x * tot_y)
#     plt.legend()
#     plt.show()









# dist_mat = mesure.distance_matrix(points)



# my_cul(cet)
# cet = cul_with(points, 3)
# print(cet)
# diff_plot(cet)
# cet = cul_with(cet, 2)
# print(cet)
# cet = cul_with(cet, 1)