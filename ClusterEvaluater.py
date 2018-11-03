from filereader import FileReader


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
        return 0;


class JaccardSimilarity:
    @staticmethod
    def evaluate():
        return 0;