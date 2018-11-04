class ClusterPoint:

    def __init__(self, point_id: int, cluster_id: int):
        self.point_id = point_id
        self.cluster_id = cluster_id

    def __eq__(self, other):
        return (self.cluster_id == other.cluster_id) & (self.point_id == other.point_id)


class ClusterPoints(list):
    def __init__(self, items):
        list.__init__(self, items)

    def cluster_ids(self):
        indices = set()
        for point in self:
            indices.add(point.cluster_id)
        return sorted(list(indices))

    def points_count(self, cluster_id: int):
        return len(self.points(cluster_id))

    def points_counts(self):
        counts = dict()
        for cluster_id in self.cluster_ids():
            counts[cluster_id] = self.points_count(cluster_id)
        return counts

    def points(self, cluster_id: int):
        return ClusterPoints([point for point in self if point.cluster_id == cluster_id])

    def intersection(self, other):
        my_point_ids = [point.point_id for point in self]
        other_point_ids = [point.point_id for point in other]
        point_ids = set(my_point_ids).intersection(other_point_ids)
        return ClusterPoints([point for point in self if any(point.point_id == point_id for point_id in point_ids)])



