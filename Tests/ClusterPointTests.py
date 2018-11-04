import unittest
from ClusterPoint import ClusterPoint, ClusterPoints


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


class ClusterPointsTests(unittest.TestCase):
    @staticmethod
    def create_test_cluster_points():
        point1 = ClusterPoint(1, 2)
        point2 = ClusterPoint(2, 1)
        point3 = ClusterPoint(3, 3)
        point4 = ClusterPoint(4, 3)
        point5 = ClusterPoint(5, 1)
        point6 = ClusterPoint(6, 1)
        return ClusterPoints([point1, point2, point3, point4, point5, point6])

    def test_cluster_ids(self):
        points = self.create_test_cluster_points()
        self.assertEqual([1, 2, 3], points.cluster_ids())

    def test_points_count(self):
        points = self.create_test_cluster_points()
        self.assertEqual(3, points.points_count(1))

    def test_points_counts(self):
        points = self.create_test_cluster_points()
        self.assertEqual({1: 3, 2: 1, 3: 2}, points.points_counts())

    def test_points(self):
        points = self.create_test_cluster_points()
        self.assertEqual(ClusterPoints([ClusterPoint(1, 2)]), points.points(2))

    def test_equality(self):
        points1 = self.create_test_cluster_points()
        points2 = self.create_test_cluster_points()
        self.assertEqual(points1, points2)
