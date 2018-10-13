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
            cluster_minimum_distance = kmeans.minimum.distance(kmeans.clusters.data_points[index])
            cluster_maximum_distance = kmeans.maximum.distance(kmeans.clusters.data_points[index])
            minimum_maximum_distance = kmeans.minimum.distance(kmeans.maximum)
            self.assertLess(cluster_maximum_distance, minimum_maximum_distance)
            self.assertLess(cluster_minimum_distance, minimum_maximum_distance)

    def test_closest_cluster_index(self):
        test_vector = self.create_test_data_vector()

        kmeans = KMeans(test_vector, 2)

        test_point = datapoint.DataPoint()
        test_point.add_dimension(1.1)
        test_point.add_dimension(2.1)
        test_point.add_dimension(3.1)

        self.assertEqual(0, kmeans.closest_cluster_index(test_vector, test_point))

    def test_cluster_points_one_cluster(self):
        test_vector = self.create_test_data_vector()

        kmeans = KMeans(test_vector, 2)

        test_point = datapoint.DataPoint()
        test_point.add_dimension(1.1)
        test_point.add_dimension(2.1)
        test_point.add_dimension(3.1)
        test_cluster = datapoint.DataVector()
        test_cluster.add_point(test_point)

        self.assertEqual([1.0, 2.0, 3.0], kmeans.cluster_points(test_cluster)[0].data_points[0].coordinates)
        self.assertEqual([3.0, 1.0, 2.0], kmeans.cluster_points(test_cluster)[0].data_points[1].coordinates)
        self.assertEqual([2.0, 3.0, 1.0], kmeans.cluster_points(test_cluster)[0].data_points[2].coordinates)

    def test_cluster_points_two_cluster(self):
        test_vector = self.create_test_data_vector()

        kmeans = KMeans(test_vector, 2)

        test_point0 = datapoint.DataPoint()
        test_point0.add_dimension(1.1)
        test_point0.add_dimension(2.1)
        test_point0.add_dimension(3.1)
        test_point1 = datapoint.DataPoint()
        test_point1.add_dimension(3.1)
        test_point1.add_dimension(1.1)
        test_point1.add_dimension(2.1)
        test_cluster = datapoint.DataVector()
        test_cluster.add_point(test_point0)
        test_cluster.add_point(test_point1)

        self.assertEqual([1.0, 2.0, 3.0], kmeans.cluster_points(test_cluster)[0].data_points[0].coordinates)
        self.assertEqual([2.0, 3.0, 1.0], kmeans.cluster_points(test_cluster)[0].data_points[1].coordinates)
        self.assertEqual([3.0, 1.0, 2.0], kmeans.cluster_points(test_cluster)[1].data_points[0].coordinates)


if __name__ == '__main__':
    unittest.main()