class ClusterPoint:

    def __init__(self, point_id: int, cluster_id: int):
        self.point_id = point_id
        self.cluster_id = cluster_id

    def __eq__(self, other):
        return self.cluster_id == other.cluster_id & \
               self.point_id == other.point_id
