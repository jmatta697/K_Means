# This is the K Mean algorithm implementation
import numpy as np
from random import uniform
from math import sqrt
from sys import maxsize


class KMeansAlg:
    def __init__(self, x_data, y_data, k_centroids, iterations):
        self.x = x_data
        self.y = y_data
        self.k = k_centroids
        self.iter = iterations
        self.x_min = min(x_data)
        self.x_max = max(x_data)
        self.y_min = min(y_data)
        self.y_max = max(y_data)
        self.centroid_point_list = []
        self.centroid_point_groups = {}
        # get random centroid start points
        for i in range(k_centroids):
            new_cent = [0, 0]
            new_cent[0] = uniform(self.x_min, self.x_max)
            new_cent[1] = uniform(self.y_min, self.y_max)
            self.centroid_point_list.append(new_cent)
            self.centroid_point_groups[tuple(new_cent)] = []
        # print(self.centroid_point_list)
        # initialize point group dictionary with initial centroids

        # construct point pairs
        self.data_points = np.array(list(zip(x_data, y_data)))

    def run_algorithm(self):
        self._construct_points_groups()
        for cent in self.centroid_point_list:
            print(self.centroid_point_groups[tuple(cent)])

    def _construct_points_groups(self):
        for i in range(self.iter):
            for pt in self.data_points:
                min_dist = maxsize
                temp_cent = None
                for cent in self.centroid_point_list:
                    euclidean_dist = two_dimensional_euclidean_distance(pt, cent)
                    if euclidean_dist < min_dist:
                        min_dist = euclidean_dist
                        temp_cent = cent
                self.centroid_point_groups[tuple(temp_cent)].append(pt)


def two_dimensional_euclidean_distance(p1, p2):
    dist = sqrt(((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2))
    return dist
