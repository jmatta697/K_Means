# This is the K Mean algorithm implementation
import numpy as np
from random import uniform
from math import sqrt
from sys import maxsize
import matplotlib.pyplot as plt


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
            # calculate random point for x and y based on the min and max range
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
        # DEBUG
        print(self.centroid_point_groups)
        # for cent in self.centroid_point_list:
        #     print(self.centroid_point_groups[tuple(cent)])
        print()
        self._construct_plot()
        # -----------------------------------------------------
        self._recalculate_centroid_positions()
        # for cent in self.centroid_point_list:
        #     print(self.centroid_point_groups[tuple(cent)])
        self._construct_points_groups()
        print(self.centroid_point_groups)
        print()
        self._construct_plot()

    def _construct_points_groups(self):
        for pt in self.data_points:
            min_dist = maxsize
            temp_cent = None
            for cent in self.centroid_point_list:
                euclidean_dist = two_dimensional_euclidean_distance(pt, cent)
                if euclidean_dist < min_dist:
                    min_dist = euclidean_dist
                    temp_cent = cent
            self.centroid_point_groups[tuple(temp_cent)].append(pt)

    '''Recalculates centroid positions and resets centroid list and reinitialize point group dict'''
    def _recalculate_centroid_positions(self):
        temp_centroid_point_list = []
        temp_point_group_dict = {}
        # for each point group in the dict...
        for centroid_key in self.centroid_point_groups:
            # loop through each point in the dict value list and get an average point
            # average all x and y values...
            x_total = 0
            x_average = 0
            y_total = 0
            y_average = 0
            num_points = len(self.centroid_point_groups[centroid_key])
            for point in self.centroid_point_groups[centroid_key]:
                x_total = x_total + point[0]
                y_total = y_total + point[1]
            # calculate x coordinate average
            x_average = x_total / num_points
            y_average = y_total / num_points
            temp_centroid_point_list.append([x_average, y_average])
            temp_point_group_dict[tuple([x_average, y_average])] = []
        self.centroid_point_list = temp_centroid_point_list
        self.centroid_point_groups = temp_point_group_dict

    def _construct_plot(self):
        # (g)reen(.)style (this means display the point as a dot in green)
        colors = 5 * ["g.", "r.", "c.", "b.", "y.", "m.", "k."]
        # plot KMeans grouping
        # iterate through each group
        # i is used to index colors - now set to a max of 15 groups
        i = 0
        for centroid_key in self.centroid_point_groups:
            plt.plot(centroid_key[0], centroid_key[1], 'k+', markersize=14)
            # set color
            point_color = colors[i]
            for point in self.centroid_point_groups[centroid_key]:
                plt.plot(point[0], point[1], colors[i], markersize=6, label='_nolegend_')
            i = i + 1
        plt.show()


def two_dimensional_euclidean_distance(p1, p2):
    dist = sqrt(((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2))
    return dist


