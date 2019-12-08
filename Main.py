
# K-Means algorithm

import pandas as pd
import matplotlib.pyplot as plt
# scikit-learn.org/stable/index.html
from sklearn.cluster import KMeans
import numpy as np
from K_Means_Alg import KMeansAlg


def main():
    setup_data_set_console_view()
    data = user_choose_data_set()

    print(data.head(10))

    x, y = user_choose_x_y_attributes()

    x_data = data[x]
    y_data = data[y]
    # print(x_data)

    # make (x, y) pairs..
    # point_pairs = np.array(list(zip(x_data, y_data)))
    # print(point_pairs)

    # user chooses K
    k = user_chooses_k()
    iterations = user_chooses_i()

    alg = KMeansAlg(x_data, y_data, k, iterations)
    alg.run_algorithm()


    # # --------------THIS NEEDS TO BE IMPLEMENTED-------------------
    # # define KMeans object using K
    # kmeans = KMeans(n_clusters=k)
    #
    # # process kernel length, width pairs
    # kmeans.fit(point_pairs)
    #
    # # define and print centroid locations
    # centroids = kmeans.cluster_centers_
    # # print(centroids)
    #
    # labels = kmeans.labels_
    # # print(labels)
    # # -------------------------------------------------------------
    #
    # # process each record
    # # "(g)reen(.) style
    # colors = 5 * ["g.", "r.", "c.", "b.", "y.", "m.", "k."]
    #
    # # plot and show KMeans grouping
    # for i in range(len(point_pairs)):
    #     plt.plot(point_pairs[i][0], point_pairs[i][1], colors[labels[i]], markersize=6, label='_nolegend_')
    #
    # plt.plot(centroids[0][0], centroids[0][1], 'k+', markersize=14, label='Centroid')
    # for i in range(1, k):
    #     plt.plot(centroids[i][0], centroids[i][1], 'k+', markersize=14)
    #
    # plt.xlabel('Length of Kernel')
    # plt.ylabel('Width of Kernel')
    # plt.title('Seed Kernel (Length vs. Height) [KMeans = 2]')
    # # plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.00001))
    # plt.show()


def setup_data_set_console_view():
    # the commands below allow the data set to be visible in the terminal output
    # without being compressed with '...'
    pd.set_option('display.width', 350)
    pd.set_option('display.max_columns', 30)
    pd.set_option('display.max_rows', 500)


def user_choose_data_set():
    data_set = ''
    data_sets = {
        1: 'training_data.csv',
        2: 'test_data.csv'
    }
    user_choice = '-1'
    while not (user_choice == '0' or user_choice == '1'):
        user_choice = input("\nWhich data set? Training or Test?\n\t1. Training\n\t2. Test\n>> ")
        data_set = data_sets.get(int(user_choice), "Try Again")
    return pd.read_csv(data_set)


def user_choose_x_y_attributes():
    attributes = {
        1: "REGION-CENTROID-COL",
        2: "REGION-CENTROID-ROW",
        3: "INTENSITY-MEAN",
        4: "RAWRED-MEAN",
        5: "RAWBLUE-MEAN",
        6: "RAWGREEN-MEAN",
        7: "EXRED-MEAN",
        8: "EXBLUE-MEAN",
        9: "EXGREEN-MEAN",
        10: "VALUE-MEAN",
        11: "SATURATION-MEAN",
        12: "HUE-MEAN"
    }
    user_choice_y = '-1'
    while True:
        print(
            "\n\t1: REGION-CENTROID-COL"
            "\n\t2: REGION-CENTROID-ROW"
            "\n\t3: INTENSITY-MEAN"
            "\n\t4: RAWRED-MEAN"
            "\n\t5: RAWBLUE-MEAN"
            "\n\t6: RAWGREEN-MEAN"
            "\n\t7: EXRED-MEAN"
            "\n\t8: EXBLUE-MEAN"
            "\n\t9: EXGREEN-MEAN"
            "\n\t10: VALUE-MEAN"
            "\n\t11: SATURATION-MEAN"
            "\n\t12: HUE-MEAN"
        )
        user_choice_x = input("\nChoose an attribute for X >> ")
        if not is_digit(user_choice_x):
            continue
        elif 0 < int(user_choice_x) < 13:
            user_choice_y = input("Choose an attribute for Y >> ")
            if not is_digit(user_choice_y):
                continue
            elif 0 < int(user_choice_y) < 13:
                break
    x_attribute = attributes.get(int(user_choice_x))
    y_attribute = attributes.get(int(user_choice_y))
    print(f'x: {x_attribute} | y: {y_attribute}\n')
    return x_attribute, y_attribute


def user_chooses_k():
    while True:
        user_choice = input("Choose a value for K >> ")
        if not is_digit(user_choice):
            continue
        elif int(user_choice) > 0:
            break
    return int(user_choice)


def user_chooses_i():
    while True:
        user_choice = input("Choose the number of iterations >> ")
        if not is_digit(user_choice):
            continue
        elif int(user_choice) > 0:
            break
    return int(user_choice)


# https://stackoverflow.com/questions/28279732/how-to-type-negative-number-with-isdigit
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
