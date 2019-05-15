from tools import mesurement_tools as mesure
from tools import assistant_algorithms as ass
from tools import plot_tools as pt
from sklearn.cluster import KMeans as km


number_of_points = 10
space_size = 100
seed = 344

points = ass.create_points(number_of_points, space_size, seed)
points_indices = [i for i in range(len(points))]
exteriors = ass.find_exterior_polygon(points, with_indices=True)
other_points_indices = ass.eliminate_list(points_indices, exteriors)
other_points = ass.indices_to_points(points, other_points_indices)
print(other_points_indices)


for i in range(2, len(other_points_indices) - 1):
    classifier = km(i)
    classifier.fit(other_points)
    pt.plot_polygon_with_index(points, exteriors, show=False)
    pt.plot_group(points, other_points_indices, classifier.cluster_centers_, classifier.labels_)
# pt.plot_points(points, True)
