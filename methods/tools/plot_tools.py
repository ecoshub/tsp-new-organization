import matplotlib.pyplot as plt
import seaborn as sns
from assistant_algorithms import indices_to_points


def init_plot(points):
    max_x = max(points, key=lambda x: x[0])[0]
    max_y = max(points, key=lambda x: x[1])[1]
    min_x = min(points, key=lambda x: x[0])[0]
    min_y = min(points, key=lambda x: x[1])[1]
    sns.set(style='darkgrid')
    plt.xlim(min_x - 5, max_x + 5)
    plt.ylim(min_y - 5, max_y + 5)
    plt.gca().set_aspect('equal', adjustable='box')
    return max_x, min_x, max_y, min_y


def plot_points(points, show=False):
    max_x, min_x, max_y, min_y = init_plot(points)
    lim = max((max_x - min_x), (max_y - min_y))
    lenp = len(points)
    for i in range(lenp):
        plt.scatter(points[i][0], points[i][1], label=i)
        plt.text(points[i][0] + lim / 100, points[i][1] + lim / 100, i)
    if show:
        plt.show()


def plot_polygon(points, show=False, title=''):
    init_plot(points)
    plot_points(points)
    plt.title(title)
    lenp = len(points)
    for i in range(lenp):
        if i == lenp - 1:
            plt.plot([points[i][0], points[0][0]], [points[i][1], points[0][1]], linewidth=0.75)
        else:
            plt.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]], linewidth=0.75)
    if show:
        plt.show()


def plot_polygon_with_index(points, index_list, title='', show=True):
    init_plot(points)
    plot_points(indices_to_points(points, index_list))
    plt.title(title)
    leni = len(index_list)
    for i in range(leni):
        plt.plot([points[index_list[i % leni]][0], points[index_list[(i + 1) % leni]][0]],
                 [points[index_list[i % leni]][1], points[index_list[(i + 1) % leni]][1]], linewidth=0.75)
    if show:
        plt.show()


def plot_star(center_index, points, show=True):
    init_plot(points)
    plot_points(points)
    lenp = len(points)
    for i in range(lenp):
        if i != center_index:
            plt.plot([points[center_index][0], points[i][0]], [points[center_index][1], points[i][1]], linewidth=0.5)
    if show:
        plt.show()


def plot_star_outter_point(point, points, show=True):
    init_plot(points)
    plot_points(points)
    lenp = len(points)
    for i in range(lenp):
        plt.plot([point[0], points[i][0]], [point[1], points[i][1]], linewidth=0.5)
    if show:
        plt.show()


def plot_all_start_in_line(points):
    init_plot(points)
    lenp = len(points)
    for i in range(lenp):
        plot_points(points)
        for j in range(lenp):
            if i != j:
                plt.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], linewidth=0.5)
        plt.show()


def plot_graph(points, graph):
    init_plot(points)
    plot_points(points)
    plt.title('The Final Graph')
    leng = len(graph)
    for i in range(leng):
        for j in range(len(graph[i])):
            plt.plot([points[i][0], points[graph[i][j]][0]], [points[i][1], points[graph[i][j]][1]], linewidth=0.5)
    plt.show()



def plot_all_possibilities(points):
    init_plot(points)
    plot_points(points)
    plt.title('All Possibilities')
    lenp = len(points)
    for i in range(lenp):
        for j in range(lenp):
            if i != j:
                plt.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], linewidth=0.5)
    plt.show()


def plot_point(points, point):
    init_plot(points)
    plt.plot(point[0], point[1], 'rs')


def plot_cirle(center, rad, points, show=False):
    init_plot(points)
    plot_points(points)
    print(center)
    cir = plt.Circle(center, rad / 2, color='k', linewidth=1, fill=False)
    plt.gcf().gca().add_artist(cir)
    if show:
        plt.show()


def plot_group(points, group_indices, centers, labels):
    init_plot(points)
    leng = len(centers)
    leni = len(group_indices)
    for i in range(leng):
        plot_point(points, centers[i])
    colors = ['lightgreen', 'lightblue', 'yellow', 'orange', 'blue', 'red', 'green', 'darkgrey']
    for i in range(leni):
        plt.scatter(points[group_indices[i]][0], points[group_indices[i]][1], label=0, c=colors[labels[i] % leng])
        plt.text(points[group_indices[i]][0] + 2, points[group_indices[i]][1] + 2, group_indices[i])
    plt.show()
