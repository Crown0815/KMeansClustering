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

    def test_add_point_empty_vector(self):
        vector = DataVector()
        point = DataPoint()
        point.coordinates.append(0)
        point.coordinates.append(0)

        vector.add_point(point)
        self.assertEqual(2, vector.dimension)
        self.assertEqual(point, vector.data_points[0])

    def test_add_point_nonempty_vector_equal_dimension(self):
        vector = DataVector()

        point0 = DataPoint()
        point0.coordinates.append(0)
        point0.coordinates.append(0)

        point1 = DataPoint()
        point1.coordinates.append(3)
        point1.coordinates.append(4)

        vector.add_point(point0)
        vector.add_point(point1)
        self.assertEqual(2, vector.dimension)
        self.assertEqual(point0, vector.data_points[0])
        self.assertEqual(point1, vector.data_points[1])

    def test_add_point_nonempty_vector_too_large_dimension(self):
        vector = DataVector()

        point0 = DataPoint()
        point0.coordinates.append(0)

        point1 = DataPoint()
        point1.coordinates.append(3)
        point1.coordinates.append(4)

        vector.add_point(point0)
        self.assertRaises(ValueError, vector.add_point, point1)

    def test_add_point_nonempty_vector_too_small_dimension(self):
        vector = DataVector()

        point0 = DataPoint()
        point0.coordinates.append(0)
        point0.coordinates.append(0)

        point1 = DataPoint()
        point1.coordinates.append(3)

        vector.add_point(point0)
        self.assertRaises(ValueError, vector.add_point, point1)

    def test_get_values(self):
        vector = DataVector()

        point0 = DataPoint()
        point0.coordinates.append(1)
        point0.coordinates.append(2)

        point1 = DataPoint()
        point1.coordinates.append(3)
        point1.coordinates.append(4)

        vector.add_point(point0)
        vector.add_point(point1)

        self.assertEqual([1, 3], vector.get_values(1))
        self.assertEqual([2, 4], vector.get_values(2))


if __name__ == '__main__':
    unittest.main()
