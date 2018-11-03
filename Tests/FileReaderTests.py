import unittest
from filereader import FileReader
from ClusterPoint import ClusterPoint


class FileReaderTests(unittest.TestCase):

    def read_file_test(self):
        file_reader = FileReader("data/partitions.txt")
        cluster_points = file_reader.read_file_to_cluster_points()
        self.assertIsInstance(cluster_points, list)
        self.assertGreater(len(cluster_points), 1)
        self.assertEqual(cluster_points[0].point_id, 1)
        self.assertEqual(cluster_points[0].cluster_id, 2)
        for cluster_point in cluster_points:
            self.assertIsInstance(cluster_point, ClusterPoint)
