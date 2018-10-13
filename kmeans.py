from datapoint import DataVector
from datapoint import DataPoint
import random


class KMeans:
    def __init__(self, data_vector: DataVector, cluster_count: int) -> None:
        if not isinstance(data_vector, DataVector):
            raise TypeError(f"Parameter data_vector has to be of type DataVector")
        self.data_vector = data_vector
        self.minimum = data_vector.min_point
        self.maximum = data_vector.max_point
        self.clusters = self.initialize_clusters(cluster_count)

    @property
    def cluster_count(self):
        return len(self.clusters.data_points)

    def initialize_clusters(self, count: int):
        clusters = DataVector()
        for cluster_number in range(count):
            point = DataPoint()
            for dimension in range(self.data_vector.dimension):
                random_value = random.uniform(self.minimum.value(dimension+1), self.maximum.value(dimension+1))
                point.add_dimension(random_value)
            clusters.add_point(point)
        return clusters

    @staticmethod
    def closest_cluster_index(clusters: DataVector, point: DataPoint) -> int:
        distances = list()
        for cluster in clusters.data_points:
            distances.append(point.distance(cluster))
        return distances.index(min(distances))

    def cluster_points(self, clusters: DataVector) -> list:
        clustered_points = list()
        for iii in range(len(clusters.data_points)):
            clustered_points.append(DataVector())

        for point in self.data_vector.data_points:
            clustered_points[self.closest_cluster_index(clusters, point)].add_point(point)

        return clustered_points

    def improve_clusters(self, clusters: DataVector) -> DataVector:
        point_clusters = self.cluster_points(clusters)
        new_clusters = DataVector()
        for point_cluster in point_clusters:
            new_clusters.add_point(point_cluster.center_point)
        if new_clusters == clusters:
            return clusters
        return self.improve_clusters(new_clusters)

    def run(self):
        self.clusters = self.improve_clusters(self.initialize_clusters(self.cluster_count))
