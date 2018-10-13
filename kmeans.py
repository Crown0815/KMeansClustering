import datapoint
import random


class KMeans:
    def __init__(self, data_vector: object, cluster_count: int) -> None:
        if not isinstance(data_vector, datapoint.DataVector):
            raise TypeError(f"Parameter data_vector has to be of type {datapoint.DataVector()}")
        self.data_vector = data_vector
        self.cluster_count = cluster_count
        self.minimum = data_vector.min_point
        self.maximum = data_vector.max_point
        self.cluster_centers = self.initialize_cluster_centers()

    def initialize_cluster_centers(self):
        centers = datapoint.DataVector()
        for cluster_number in range(self.cluster_count):
            point = datapoint.DataPoint()
            for dimension in range(self.data_vector.dimension):
                random_value = random.uniform(self.minimum.value(dimension+1), self.maximum.value(dimension+1))
                point.add_dimension(random_value)
            centers.add_point(point)
        return centers


print(random.uniform(-100, 100))
