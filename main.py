import filereader


class Main:
    def __init__(self):
        self.file_reader = filereader.FileReader("places.txt")
        self.data_points = self.file_reader.read_file_to_data_points()


main = Main()
print(main.data_points)
