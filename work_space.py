from tools import plot_tools as pt
from tools import assistant_algorithms as ass
# from tools import mesurement_tools as mesure
# from tools import iteration_tools as cal
from math import sqrt



def coff(points):
    coff_vector = []
    for i in range(len(points)):
        coff = sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        # coff = sqrt(points[i][0] ** 2 + points[i][1] ** 2) * (points[i][1] / points[i][0])
        coff_vector.append([coff, i])
    return coff_vector



def normal_dist(vector):
    vector = sorted(vector)
    lenv = len(vector)
    lower = []
    higher = []
    for i in range(0, lenv, 2):
        lower.append(vector[i])
        if i + 1 < lenv:
            higher.append(vector[i + 1])
    higher = list(reversed(higher))
    master = lower + higher
    print(master)


number_of_points = 7
space_size = 20
seed = 0

points = ass.create_points(number_of_points, space_size, seed)
x_es = [points[i][0] for i in range(len(points))]
y_es = [points[i][1] for i in range(len(points))]
print(x_es)
normal_dist(x_es)

pt.plot_points(points, True)
