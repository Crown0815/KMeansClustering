from filereader import FileReader
from filewriter import FileWriter
from ClusterPoint import ClusterPoints
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
    def evaluate(self, clusters: ClusterPoints, partitions: ClusterPoints):
        mutual_information = self.mutual_information(clusters, partitions)
        entropy_clusters = self.entropy_of_clustering(clusters)
        entropy_partitions = self.entropy_of_clustering(partitions)
        if mutual_information == 0:
            return mutual_information
        return mutual_information / sqrt(entropy_clusters * entropy_partitions)

    def entropy_of_clustering(self, clusters: ClusterPoints):
        entropy = 0
        for cluster_id in clusters.cluster_ids():
            cluster_probability = self.cluster_probability(clusters, cluster_id)
            entropy += cluster_probability * log(cluster_probability)
        return -entropy

    def mutual_information(self, clusters: ClusterPoints, partitions: ClusterPoints):
        mutual_information = 0
        for partition_id in partitions.cluster_ids():
            for cluster_id in clusters.cluster_ids():
                mutual_information += self.information_term(partitions, clusters, partition_id, cluster_id)
        return mutual_information

    def information_term(self, clusters: ClusterPoints, partitions: ClusterPoints, cluster_id: int, partition_id: int):
        joint_probability = self.joint_probability(partitions, clusters, partition_id, cluster_id)
        partition_probability = self.cluster_probability(partitions, partition_id)
        cluster_probability = self.cluster_probability(clusters, cluster_id)
        if joint_probability == 0:
            return joint_probability
        return joint_probability * log(joint_probability / (partition_probability * cluster_probability))

    @staticmethod
    def cluster_probability(cluster_points: ClusterPoints, cluster_id: int):
        return cluster_points.points_count(cluster_id) / len(cluster_points)

    @staticmethod
    def joint_probability(partitions: ClusterPoints, clusters: ClusterPoints, partition_id: int, cluster_id: int):
        shared_points = partitions.points(partition_id).intersection(clusters.points(cluster_id))
        return len(shared_points) / len(partitions)


class JaccardSimilarity:
    def evaluate(self, partitions: ClusterPoints, clusters: ClusterPoints):
        tp = self.true_positive(partitions, clusters)
        fn = self.false_negative(partitions, clusters)
        fp = self.false_positive(partitions, clusters)
        return tp / (tp + fn + fp)

    @staticmethod
    def true_positive(partitions: ClusterPoints, clusters: ClusterPoints):
        combinations = 0
        for partition_id in partitions.cluster_ids():
            for cluster_id in clusters.cluster_ids():
                combinations += len(partitions.points(partition_id).intersection(clusters.points(cluster_id))) ** 2
        combinations -= len(partitions)
        return combinations / 2

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


nmi = ClusterEvaluator(NormalizedMutualInformation(), FileReader("", " "))
jcs = ClusterEvaluator(JaccardSimilarity(), FileReader("", " "))
results = list()
for iii in range(1, 6):
    nmi_result = nmi.evaluate("data/partitions.txt", "data/clustering_"+str(iii)+".txt")
    jcs_result = jcs.evaluate("data/partitions.txt", "data/clustering_"+str(iii)+".txt")
    print("////// "+str(iii)+" ///////")
    print(nmi_result)
    print(jcs_result)
    print()
    results.append([nmi_result, jcs_result])

writer = FileWriter("data/scores.txt", " ")
writer.write_list_of_rows_to_file(results)

