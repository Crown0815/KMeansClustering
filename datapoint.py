class DataPoint:
    def __init__(self) -> None:
        self.coordinates = list()

    @property
    def dimension(self) -> int:
        return len(self.coordinates)


class DataVector:
    def __init__(self) -> None:
        self.data_points = list()

    def add_point(self, point: DataPoint) -> None:
        if self.dimension() != point.dimension:
            raise ValueError(f"Dimensions do not agree (Vector: {self.dimension}, Point: {point.dimension})")
        self.data_points.append(point)

    def dimension(self) -> int:
        return len(self.data_points[0])

    def get_values(self, dimension: int = 1):
        if dimension > self.dimension():
            raise ValueError(f"Requested dimension ({dimension}) exceeds available dimensions ({self.dimension})")

        dimension_values = list()
        for point in self.data_points:
            dimension_values.append(point.coordinates[dimension])

        return dimension_values



