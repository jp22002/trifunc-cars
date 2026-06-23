def get_input():
    car_color = input('Enter a car manufacturer (or press Enter to finish): ').title()
    return car_color


def get_dictionary():
    '''
    This creates a dictionary and sorts it 
    '''

    car_dictionary = {}
    flag = True
    while flag == True:
        car_color = get_input()
        if car_color == "":
            return car_dictionary
            flag = False
        else:
            if car_color in car_dictionary:
                car_dictionary[car_color] += 1
            else:
                car_dictionary[car_color] = 1


def use_dictionary(car_dictionary):
    car_dictionary = dict(sorted(car_dictionary.items()))

    for key ,value in car_dictionary.items():
        print(f"{key}: {value}")

use_dictionary(get_dictionary())