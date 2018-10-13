import csv
import datapoint


class FileReader:
    def __init__(self, file_path: str, delimiter: object = ",") -> None:

        self.file_path = file_path
        self.delimiter = delimiter

    def read_file_to_data_points(self) -> list():
        with open(self.file_path, mode='r') as open_file:
            csv_reader = csv.reader(open_file, delimiter=self.delimiter)
            points = list()
            line_count = 0
            for row in csv_reader:
                point = datapoint.DataPoint()
                for item in row:
                    point.coordinates.append(float(item))
                points.append(point)
                line_count += 1
            print(f'Processed {line_count} lines.')
        return points
