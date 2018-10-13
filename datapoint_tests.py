import unittest
from datapoint import DataPoint
from datapoint import DataVector


class DataPointTests(unittest.TestCase):

    def test_distance(self):
        point0 = DataPoint()
        point0.coordinates.append(0)
        point0.coordinates.append(0)

        point1 = DataPoint()
        point1.coordinates.append(3)
        point1.coordinates.append(4)
        self.assertEqual(5, point0.distance(point1))

    def test_dimension(self):
        point = DataPoint()
        point.coordinates.append(0)
        point.coordinates.append(0)

        self.assertEqual(2, point.dimension)


class DataVectorTests(unittest.TestCase):
    @staticmethod
    def create_test_data_vector(values_list: list):
        data_vector = DataVector()

        for values in values_list:
            point = DataPoint()
            for dimension_value in values:
                point.add_dimension(dimension_value)
            data_vector.add_point(point)
        return data_vector

    def test_add_point_empty_vector(self):
        vector = self.create_test_data_vector([[0, 0]])

        self.assertEqual(2, vector.dimension)
        self.assertEqual([0, 0], vector.data_points[0].coordinates)

    def test_add_point_nonempty_vector_equal_dimension(self):
        vector = self.create_test_data_vector([[0, 0], [3, 4]])

        self.assertEqual(2, vector.dimension)
        self.assertEqual([0, 0], vector.data_points[0].coordinates)
        self.assertEqual([3, 4], vector.data_points[1].coordinates)

    def test_add_point_nonempty_vector_too_large_dimension(self):
        vector = self.create_test_data_vector([[0]])

        point = DataPoint()
        point.coordinates.append(3)
        point.coordinates.append(4)

        self.assertRaises(ValueError, vector.add_point, point)

    def test_add_point_nonempty_vector_too_small_dimension(self):
        vector = self.create_test_data_vector([[0, 0]])

        point = DataPoint()
        point.coordinates.append(3)

        self.assertRaises(ValueError, vector.add_point, point)

    def test_get_values(self):
        vector = self.create_test_data_vector([[1, 2], [3, 4]])

        self.assertEqual([1, 3], vector.get_values(1))
        self.assertEqual([2, 4], vector.get_values(2))

    def test_max_by_dimension(self):
        vector = self.create_test_data_vector([[-1, 2], [3, -4]])

        self.assertEqual(3, vector.max(1))
        self.assertEqual(2, vector.max(2))

    def test_min_by_dimension(self):
        vector = self.create_test_data_vector([[-1, 2], [3, -4]])

        self.assertEqual(-1, vector.min(1))
        self.assertEqual(-4, vector.min(2))

    def test_min_by_dimension(self):
        vector = self.create_test_data_vector([[1, 1], [3, 5]])

        self.assertEqual(2, vector.center(1))
        self.assertEqual(3, vector.center(2))

    def test_extreme_point(self):
        vector = self.create_test_data_vector([[-1, 2], [3, -4], [3, -4]])

        self.assertEqual([3, 2], vector.max_point.coordinates)
        self.assertEqual([-1, -4], vector.min_point.coordinates)

    def test_center_point(self):
        vector = self.create_test_data_vector([[-1, -1], [1, 1], [-2, -2], [2, 2]])

        self.assertEqual([0, 0], vector.center_point.coordinates)


if __name__ == '__main__':
    unittest.main()
