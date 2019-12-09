# This is the K Mean algorithm implementation
import numpy as np
from random import uniform
from math import sqrt
from sys import maxsize
from sys import exit
import matplotlib.pyplot as plt
from time import sleep


class KMeansAlg:
    def __init__(self, x_data, y_data, k_centroids, iterations, x_axis, y_axis):
        self.x = x_data
        self.y = y_data
        self.k = k_centroids
        self.iter = iterations
        self.current_iter = 0
        self.x_min = min(x_data)
        self.x_max = max(x_data)
        self.y_min = min(y_data)
        self.y_max = max(y_data)
        self.centroid_point_list = []
        self.cluster_objects = []
        # point group dictionary
        self.centroid_point_groups = {}
        # graph labels
        self.x_axis_graph_label = x_axis
        self.y_axis_graph_label = y_axis
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
        self.colors_assigned = False

    # cluster objects to associate color and SSE with cluster data
    class ClusterObject:
        def __init__(self, color_string, cluster_centroid, point_lst):
            self.sum_squared_error = 0
            self.centroid_point = cluster_centroid
            self.point_list = point_lst
            # interpret color string and associate color string
            # colors = 5 * ["g.", "r.", "c.", "b.", "y.", "m.", "k."]
            color_association = {
                'g': "green",
                'r': "red",
                'c': "cyan",
                'b': "blue",
                'y': "yellow",
                'm': "magenta",
                'k': "black"
            }
            self.color = color_association[color_string[0]]
            # calculate SSE...

        # calculated sum squared error for one cluster - takes centroid point and list of cluster points
        def calculate_sum_squared_error(self):
            for point in self.point_list:
                # calculate euclidean distance
                dist = two_dimensional_euclidean_distance(self.centroid_point, point)
                # add to error total
                self.sum_squared_error = self.sum_squared_error + (dist ** 2)

    def run_algorithm(self):
        for i in range(self.iter):
            self.current_iter = i
            self._construct_points_groups()
            # DEBUG
            # print(self.centroid_point_groups)
            self._construct_plot()
            # print cluster objects...
            # reassign attributes of cluster objects
            print()
            cluster_obj_index = 0
            for group in self.centroid_point_groups:
                self.cluster_objects[cluster_obj_index].centroid_point = group
                self.cluster_objects[cluster_obj_index].point_list = self.centroid_point_groups.get(group)
                print(f'color: {self.cluster_objects[cluster_obj_index].color} | '
                      f'cent: {self.cluster_objects[cluster_obj_index].centroid_point} | '
                      f'point list: {self.cluster_objects[cluster_obj_index].point_list}')
                cluster_obj_index = cluster_obj_index + 1
            sleep(1)
            self._recalculate_centroid_positions()
        # calculate SSE and add it to cluster object
        print()
        for obj in self.cluster_objects:
            obj.calculate_sum_squared_error()
            print(f'SSE for {obj.color}: {obj.sum_squared_error}')

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
            try:
                x_average = x_total / num_points
                y_average = y_total / num_points
            except ZeroDivisionError:
                print("\n*** There are clusters with zero points. Restart algorithm. *** EXITING...")
                exit()
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
            # set color
            point_color = colors[i]
            # assign colors to cluster objects here - only do this once
            # ----
            if not self.colors_assigned:
                # construct cluster object and add it to the cluster object list
                # single_dict_item = {self.centroid_point_groups[centroid_key]}
                cluster_obj = self.ClusterObject(point_color, centroid_key, self.centroid_point_groups[centroid_key])
                self.cluster_objects.append(cluster_obj)
            # ----
            for point in self.centroid_point_groups[centroid_key]:
                plt.plot(point[0], point[1], colors[i], markersize=6, label='_nolegend_')
            i = i + 1
            plt.plot(centroid_key[0], centroid_key[1], 'k+', markersize=14)

        self.colors_assigned = True
        plt.xlabel(self.x_axis_graph_label)
        plt.ylabel(self.y_axis_graph_label)
        plt.title(f'Image Segmentation ({self.x_axis_graph_label} vs. {self.y_axis_graph_label}) [K={self.k}] '
                  f'\n\nITERATION = {self.current_iter}', fontsize=10)
        plt.show()


def two_dimensional_euclidean_distance(p1, p2):
    dist = sqrt(((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2))
    return dist
