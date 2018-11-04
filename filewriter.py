import csv


class FileWriter:
    def __init__(self, file_path: str, delimiter: object = ",") -> None:

        self.file_path = file_path
        self.delimiter = delimiter

    def write_data_clusters_to_file(self, index_clusters: dict):
        with open(self.file_path, mode='w') as open_file:
            csv_writer = csv.writer(open_file,  delimiter=self.delimiter)
            for key, value in index_clusters.items():
                csv_writer.writerow([key, value])

    def write_list_of_rows_to_file(self, lists: list):
        with open(self.file_path, mode='w') as open_file:
            csv_writer = csv.writer(open_file,  delimiter=self.delimiter)
            for row in lists:
                csv_writer.writerow(row)
