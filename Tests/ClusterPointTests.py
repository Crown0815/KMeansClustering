import unittest
from ClusterPoint import ClusterPoint


class ClusterPointTests(unittest.TestCase):

    @staticmethod
    def create_test_cluster_point(point_id: int, cluster_id: int):
        return ClusterPoint(point_id, cluster_id)

    def test_equality(self):
        point1 = self.create_test_cluster_point(1, 2)
        point2 = self.create_test_cluster_point(1, 2)
        self.assertEqual(point1, point2)

    def test_inequality(self):
        point1 = self.create_test_cluster_point(2, 1)
        point2 = self.create_test_cluster_point(1, 1)
        self.assertNotEqual(point1, point2)

        point1 = self.create_test_cluster_point(1, 2)
        point2 = self.create_test_cluster_point(1, 1)
        self.assertNotEqual(point1, point2)
