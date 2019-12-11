
# K-Means algorithm
import pandas as pd
from K_Means_Alg import KMeansAlg


def main():
    # sets up data display in console
    setup_data_set_console_view()
    # user chooses data set and a pandas dataset object is created
    data = user_choose_data_set()
    # user can see what the data set looks like
    print(data.head(10))
    # user chooses x and y coordinate attributes (returns strings)
    x, y = user_choose_x_y_attributes(data)
    # gets the chossen data from the attribute columns
    x_data = data[x]
    y_data = data[y]
    # user chooses K
    k = user_chooses_k()
    # user chooses number of iterations
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
        data_set = input('\nEnter a filename (with extension): ')
        try:
            csv_input = pd.read_csv(data_set)
        except FileNotFoundError:
            print(f'\n{data_set} is not a valid filename. Make sure you typed the filename correctly WITH the extension.')
            print('Also, make sure the file is located in this working directory.\n')
        else:
            return csv_input


def user_choose_x_y_attributes(data_set):
    # read first line of csv file with attribute names..
    attribute_dict = {}
    num = 1
    for attr in data_set.keys():
        attribute_dict[num] = attr
        num = num + 1
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


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
