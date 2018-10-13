import unittest
from kmeans import KMeans
import datapoint


class DataPointTests(unittest.TestCase):
    @staticmethod
    def create_test_data_vector():
        data_vector = datapoint.DataVector()
        values_list = [[1.0, 2.0, 3.0],
                       [3.0, 1.0, 2.0],
                       [2.0, 3.0, 1.0]]

        for values in values_list:
            point = datapoint.DataPoint()
            for dimension_value in values:
                point.add_dimension(dimension_value)
            data_vector.add_point(point)
        return data_vector

    def test_initialization(self):
        test_vector = self.create_test_data_vector()

        kmeans = KMeans(test_vector, 2)

        self.assertEqual([1.0, 1.0, 1.0], kmeans.minimum.coordinates)
        self.assertEqual([3.0, 3.0, 3.0], kmeans.maximum.coordinates)
        self.assertEqual(2, kmeans.cluster_count)

        for index in range(kmeans.cluster_count):
            cluster_minimum_distance = kmeans.minimum.distance(kmeans.cluster_centers.data_points[index])
            cluster_maximum_distance = kmeans.maximum.distance(kmeans.cluster_centers.data_points[index])
            minimum_maximum_distance = kmeans.minimum.distance(kmeans.maximum)
            self.assertLess(cluster_maximum_distance, minimum_maximum_distance)
            self.assertLess(cluster_minimum_distance, minimum_maximum_distance)


if __name__ == '__main__':
    unittest.main()