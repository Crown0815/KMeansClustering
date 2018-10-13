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
        return self.point_by_func(self.min)

    @property
    def max_point(self) -> object:
        return self.point_by_func(self.max)

    @property
    def center_point(self) -> object:
        return self.point_by_func(self.center)

    def point_by_func(self, func):
        if not isinstance(self.dimension, int):
            raise EnvironmentError("DataVector has no points yet")
        point = DataPoint()
        for dimension in range(self.dimension):
            point.add_dimension(func(dimension + 1))
        return point

    def get_values(self, dimension: int = 1):
        if dimension > self.dimension:
            raise ValueError(f"Requested dimension ({dimension}) exceeds available dimensions ({self.dimension})")

        dimension_values = list()
        for point in self.data_points:
            dimension_values.append(point.value(dimension))

        return dimension_values



