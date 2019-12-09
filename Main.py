
# K-Means algorithm
import pandas as pd
from K_Means_Alg import KMeansAlg


def main():
    setup_data_set_console_view()
    data = user_choose_data_set()

    print(data.head(10))

    x, y = user_choose_x_y_attributes(data)

    x_data = data[x]
    y_data = data[y]
    # print(x_data)

    # user chooses K
    k = user_chooses_k()
    iterations = user_chooses_i()

    alg = KMeansAlg(x_data, y_data, k, iterations, x, y)
    alg.run_algorithm()


def setup_data_set_console_view():
    # the commands below allow the data set to be visible in the terminal output
    # without being compressed with '...'
    pd.set_option('display.width', 350)
    pd.set_option('display.max_columns', 30)
    pd.set_option('display.max_rows', 500)


def user_choose_data_set():
    while True:
        data_set = input('Enter a filename (with extension): ')
        try:
            csv_input = pd.read_csv(data_set)
        except FileNotFoundError:
            print(f'\n{data_set} is not a valid filename. Make sure you typed the filename correctly WITH the extension.')
            print('Also, make sure the file is located in this working directory.\n')
        else:
            return csv_input


# def user_choose_data_set():
#     data_set = ''
#     data_sets = {
#         1: 'training_data.csv',
#         2: 'test_data.csv'
#     }
#     user_choice = '-1'
#     while not (user_choice == '1' or user_choice == '2'):
#         user_choice = input("\nWhich data set? Training or Test?\n\t1. Training\n\t2. Test\n>> ")
#         data_set = data_sets.get(int(user_choice), "Try Again")
#     return pd.read_csv(data_set)


def user_choose_x_y_attributes(data_set):
    # read first line of csv file with attribute names..
    attribute_dict = {}
    num = 1
    for attr in data_set.keys():
        attribute_dict[num] = attr
        num = num + 1
        # print(attr)
    print(len(attribute_dict))

    user_choice_y = '-1'
    while True:
        print()
        for num, name in attribute_dict.items():
            print(f'\t{num}: {name}')

        user_choice_x = input("\nChoose an attribute for X >> ")
        if not is_digit(user_choice_x):
            continue
        elif 0 < int(user_choice_x) < len(attribute_dict) + 1:
            user_choice_y = input("Choose an attribute for Y >> ")
            if not is_digit(user_choice_y):
                continue
            elif 0 < int(user_choice_y) < len(attribute_dict) + 1:
                break
    x_attribute = attribute_dict.get(int(user_choice_x))
    y_attribute = attribute_dict.get(int(user_choice_y))
    print(f'x: {x_attribute} | y: {y_attribute}\n')
    return x_attribute, y_attribute


# def user_choose_x_y_attributes(data_set):
#     # read first line of csv file with attribute names..
#     for attr in data_set.keys():
#         print(attr)
#     print(len(data_set.keys()))
#
#     attributes = {
#         1: "REGION-CENTROID-COL",
#         2: "REGION-CENTROID-ROW",
#         3: "VEDGE-MEAN",
#         4: "VEDGE-SD",
#         5: "HEDGE-MEAN",
#         6: "HEDGE-SD",
#         7: "INTENSITY-MEAN",
#         8: "RAWRED-MEAN",
#         9: "RAWBLUE-MEAN",
#         10: "RAWGREEN-MEAN",
#         11: "EXRED-MEAN",
#         12: "EXBLUE-MEAN",
#         13: "EXGREEN-MEAN",
#         14: "VALUE-MEAN",
#         15: "SATURATION-MEAN",
#         16: "HUE-MEAN"
#     }
#     user_choice_y = '-1'
#     while True:
#         print(
#             "\n\t1: REGION-CENTROID-COL"
#             "\n\t2: REGION-CENTROID-ROW"
#             "\n\t3: VEDGE-MEAN"
#             "\n\t4: VEDGE-SD"
#             "\n\t5: HEDGE-MEAN"
#             "\n\t6: HEDGE-SD"
#             "\n\t7: INTENSITY-MEAN"
#             "\n\t8: RAWRED-MEAN"
#             "\n\t9: RAWBLUE-MEAN"
#             "\n\t10: RAWGREEN-MEAN"
#             "\n\t11: EXRED-MEAN"
#             "\n\t12: EXBLUE-MEAN"
#             "\n\t13: EXGREEN-MEAN"
#             "\n\t14: VALUE-MEAN"
#             "\n\t15: SATURATION-MEAN"
#             "\n\t16: HUE-MEAN"
#         )
#         user_choice_x = input("\nChoose an attribute for X >> ")
#         if not is_digit(user_choice_x):
#             continue
#         elif 0 < int(user_choice_x) < 17:
#             user_choice_y = input("Choose an attribute for Y >> ")
#             if not is_digit(user_choice_y):
#                 continue
#             elif 0 < int(user_choice_y) < 17:
#                 break
#     x_attribute = attributes.get(int(user_choice_x))
#     y_attribute = attributes.get(int(user_choice_y))
#     print(f'x: {x_attribute} | y: {y_attribute}\n')
#     return x_attribute, y_attribute


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
