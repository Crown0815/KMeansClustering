import datapoint
import random


class KMeans:
    def __init__(self, data_vector: object, cluster_count: int) -> None:
        if not isinstance(data_vector, datapoint.DataVector):
            raise TypeError(f"Parameter data_vector has to be of type datapoint.DataVector")
        self.data_vector = data_vector
        self.cluster_count = cluster_count
        self.minimum = data_vector.min_point
        self.maximum = data_vector.max_point
        self.clusters = self.initialize_cluster_centers()

    def initialize_cluster(self):
        clusters = datapoint.DataVector()
        for cluster_number in range(self.cluster_count):
            point = datapoint.DataPoint()
            for dimension in range(self.data_vector.dimension):
                random_value = random.uniform(self.minimum.value(dimension+1), self.maximum.value(dimension+1))
                point.add_dimension(random_value)
            clusters.add_point(point)
        return clusters

    @staticmethod
    def closest_cluster_index(clusters: object, point: object) -> int:
        distances = list()
        for cluster in clusters:
            distances.append(point.distance(cluster))
        return distances.index(min(distances))

    def cluster_points(self, clusters: object) -> object:
        clustered_points = list()
        for iii in range(len(clusters)):
            clustered_points.append(datapoint.DataVector)

        for point in self.data_vector.data_points:
            clustered_points[self.closest_cluster_index(clusters, point)].add_point(point)

        return clustered_points

    def improve_clusters(self, clusters: object) -> object:
        point_clusters = self.cluster_points(clusters)
        new_clusters = datapoint.DataVector()
        for point_cluster in point_clusters:
            new_clusters.add_point(point_cluster.center_point)
        if new_clusters == clusters:
            return clusters
        return self.improve_clusters(new_clusters)

    def run(self):
        self.clusters = self.improve_clusters(self.initialize_cluster_centers())







print(random.uniform(-100, 100))
