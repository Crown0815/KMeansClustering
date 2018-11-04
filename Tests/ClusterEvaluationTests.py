import unittest
from ClusterEvaluater import ClusterEvaluator, JaccardSimilarity, NormalizedMutualInformation
from ClusterPoint import ClusterPoint, ClusterPoints


class JaccardSimilarityTests(unittest.TestCase):
    @staticmethod
    def create_test_cluster_points():
        point1 = ClusterPoint(1, 2)
        point2 = ClusterPoint(2, 1)
        point3 = ClusterPoint(3, 2)
        point4 = ClusterPoint(4, 2)
        point5 = ClusterPoint(5, 1)
        point6 = ClusterPoint(6, 1)
        return ClusterPoints([point1, point2, point3, point4, point5, point6])

    def test_true_positive(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 1
        clusters[2].cluster_id = 1
        self.assertEqual(4, JaccardSimilarity().true_positive(partitions, clusters))

    def test_false_positive(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 1
        clusters[2].cluster_id = 1
        self.assertEqual(6, JaccardSimilarity().false_positive(partitions, clusters))

    def test_false_negative(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 1
        clusters[2].cluster_id = 1
        self.assertEqual(2, JaccardSimilarity().false_negative(partitions, clusters))

    def test_evaluate(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 1
        clusters[2].cluster_id = 1
        self.assertEqual(1/3, JaccardSimilarity().evaluate(partitions, clusters))
