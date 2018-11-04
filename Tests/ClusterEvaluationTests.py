import unittest
from ClusterEvaluator import ClusterEvaluator, JaccardSimilarity, NormalizedMutualInformation
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


class NormalizedMutualInformationTests(unittest.TestCase):
    @staticmethod
    def create_test_cluster_points():
        point1 = ClusterPoint(1, 1)
        point2 = ClusterPoint(2, 1)
        point3 = ClusterPoint(3, 2)
        return ClusterPoints([point1, point2, point3])

    def test_entropy_of_clustering(self):
        points = self.create_test_cluster_points()
        self.assertEqual(NormalizedMutualInformation().entropy_of_clustering(points), 0.6365141682948128)

    def test_cluster_probability(self):
        points = self.create_test_cluster_points()
        nmi = NormalizedMutualInformation()
        self.assertEqual(nmi.cluster_probability(points, 1), 2/3)
        self.assertEqual(nmi.cluster_probability(points, 2), 1/3)

    def test_joint_probability(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 2
        nmi = NormalizedMutualInformation()
        self.assertEqual(nmi.joint_probability(partitions, clusters, 1, 1), 1/3)
        self.assertEqual(nmi.joint_probability(partitions, clusters, 1, 2), 1/3)
        self.assertEqual(nmi.joint_probability(partitions, clusters, 2, 1), 0/3)
        self.assertEqual(nmi.joint_probability(partitions, clusters, 2, 2), 1/3)

    def test_information_term(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 2
        nmi = NormalizedMutualInformation()
        self.assertEqual(nmi.information_term(clusters, partitions, 1, 1), 0.13515503603605478)
        self.assertEqual(nmi.information_term(clusters, partitions, 1, 2), 0)
        self.assertEqual(nmi.information_term(clusters, partitions, 2, 1), -0.09589402415059363)
        self.assertEqual(nmi.information_term(clusters, partitions, 2, 2), 0.13515503603605478)

    def test_mutual_information(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 2
        nmi = NormalizedMutualInformation()
        self.assertEqual(nmi.mutual_information(clusters, partitions), 0.17441604792151594)

    def test_evaluate(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 2
        nmi = NormalizedMutualInformation()
        self.assertEqual(nmi.evaluate(clusters, partitions), 0.2740175421212809)

    def test_evaluate(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        clusters[0].cluster_id = 2
        clusters[1].cluster_id = 2
        nmi = NormalizedMutualInformation()
        self.assertEqual(nmi.evaluate(clusters, partitions), 0)

    def test_evaluate_perfect_match(self):
        partitions = self.create_test_cluster_points()
        clusters = self.create_test_cluster_points()
        nmi = NormalizedMutualInformation()
        self.assertEqual(nmi.evaluate(clusters, partitions), 1)
