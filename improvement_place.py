from tools import mesurement_tools as mesure


def minimum_deviation_point_to_polygon(points, exterior, distance_mat, new_points, graph):
    main_min = float('inf')
    main_mem = [0, 0, 0]
    lenx = len(exterior)
    lenp = len(new_points)
    for i in range(lenp):
        min_side = float('inf')
        mem_side = [0, 0, 0]
        for j in range(lenx):
            dev = mesure.deviation_amount_with_index(exterior[j % lenx], exterior[(j + 1) % lenx], new_points[i], distance_mat)
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





# points = ass.create_points(10, 100, 0)
# angle_mat = mesure.angle_matrix(points)
# lenp = len(points)
