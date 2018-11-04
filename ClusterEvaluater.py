from filereader import FileReader
from ClusterPoint import ClusterPoint, ClusterPoints
from math import log, sqrt


class ClusterEvaluator:
    def __init__(self, strategy, file_reader: FileReader):
        self.strategy = strategy
        self.file_reader = file_reader

    def evaluate(self, partitions_path: str, clusters_path: str) -> float:
        partitions = self.file_reader.read_file_to_cluster_points(partitions_path)
        clusters = self.file_reader.read_file_to_cluster_points(clusters_path)
        return self.strategy.evaluate(partitions, clusters)


class NormalizedMutualInformation:
    @staticmethod
    def evaluate():
        return 0


class JaccardSimilarity:
    def evaluate(self, partitions: ClusterPoints, clusters: ClusterPoints):
        tp = self.true_positive(partitions, clusters)
        fn = self.false_negative(partitions, clusters)
        fp = self.false_positive(partitions, clusters)
        return tp/(tp + fn + fp)

    @staticmethod
    def true_positive(partitions: ClusterPoints, clusters: ClusterPoints):
        combinations = 0
        for partition_id in partitions.cluster_ids():
            for cluster_id in clusters.cluster_ids():
                combinations += len(partitions.points(partition_id).intersection(clusters.points(cluster_id)))**2
        combinations -= len(partitions)
        return combinations/2

    def false_negative(self, partitions: ClusterPoints, clusters: ClusterPoints):
        return self.sum_of_pairs(partitions) - self.true_positive(partitions, clusters)

    def false_positive(self, partitions: ClusterPoints, clusters: ClusterPoints):
        return self.sum_of_pairs(clusters) - self.true_positive(partitions, clusters)

    @staticmethod
    def sum_of_pairs(cluster_points: ClusterPoints):
        combinations = 0
        for cluster_id in cluster_points.cluster_ids():
            cluster_count = cluster_points.points_count(cluster_id)
            combinations += cluster_count * (cluster_count - 1)
        return combinations / 2
