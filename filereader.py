import csv
import datapoint
from ClusterPoint import ClusterPoint


class FileReader:
    def __init__(self, file_path: str, delimiter: object = ",") -> None:

        self.file_path = file_path
        self.delimiter = delimiter

    def read_file_to_data_points(self) -> list():
        with open(self.file_path, mode='r') as open_file:
            csv_reader = csv.reader(open_file, delimiter=self.delimiter)
            data_vector = datapoint.DataVector()
            line_count = 0
            for row in csv_reader:
                point = datapoint.DataPoint()
                for item in row:
                    point.coordinates.append(float(item))
                data_vector.add_point(point)
                line_count += 1
            print(f'Processed {line_count} lines.')
        return data_vector

    def read_file_to_cluster_points(self, path: str) -> list():
        with open(path, mode='r') as open_file:
            csv_reader = csv.reader(open_file, delimiter=self.delimiter)
            cluster_points = list()
            line_count = 0
            for row in csv_reader:
                cluster_point = ClusterPoint()
                for item in row:
                    cluster_point.point_id = int(item[0])
                    cluster_point.cluster_id = int(item[1])
                cluster_points.append(cluster_point)
                line_count += 1
            print(f'Processed {line_count} lines.')
        return cluster_points
