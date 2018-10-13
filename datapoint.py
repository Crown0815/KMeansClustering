import math
import numpy as np


class DataPoint:
    def __init__(self) -> None:
        self.coordinates = list()

    @property
    def dimension(self) -> int:
        return len(self.coordinates)

    def distance(self, point: object) -> float:
        distance = 0
        for dimension in range(self.dimension):
            distance += (self.coordinates[dimension] - point.coordinates[dimension])**2
        return math.sqrt(distance)

    def add_dimension(self, value: float):
        self.coordinates.append(value)

    def value(self, dimension: int):
        return self.coordinates[dimension-1]


class DataVector:
    def __init__(self) -> None:
        self.data_points = list()

    def add_point(self, point: DataPoint) -> None:
        if (len(self.data_points) > 0) & (self.dimension != point.dimension):
            raise ValueError(f"Dimensions do not agree (Vector: {self.dimension}, Point: {point.dimension})")
        self.data_points.append(point)

    @property
    def dimension(self) -> int:
        if len(self.data_points) < 1:
            return math.inf
        return len(self.data_points[0].coordinates)

    def max(self, dimension: int = 1):
        return max(self.get_values(dimension))

    def min(self, dimension: int = 1):
        return min(self.get_values(dimension))

    def center(self, dimension: int = 1):
        return np.mean(self.get_values(dimension))

    @property
    def min_point(self) -> object:
        point = DataPoint()
        for dimension in range(len(self.data_points)):
            point.add_dimension(self.min(dimension+1))
        return point

    @property
    def max_point(self) -> object:
        point = DataPoint()
        for dimension in range(len(self.data_points)):
            point.add_dimension(self.max(dimension+1))
        return point

    @property
    def center_point(self) -> object:
        point = DataPoint()
        for dimension in range(len(self.data_points)):
            point.add_dimension(self.center(dimension+1))
        return point

    def get_values(self, dimension: int = 1):
        if dimension > self.dimension:
            raise ValueError(f"Requested dimension ({dimension}) exceeds available dimensions ({self.dimension})")

        dimension_values = list()
        for point in self.data_points:
            dimension_values.append(point.value(dimension))

        return dimension_values



