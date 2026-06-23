'''
This program allows a user to input car brands and then prints how many times it appears
'''


def get_input():
    '''
    Gets an Input
    '''
    car_color = input('Enter a car manufacturer (or press Enter to finish): ').title()
    return car_color


def get_dictionary():
    '''
    This creates a dictionary and calls the input function
    '''
    #dictionary is made
    global car_dictionary
    flag = True
    while flag:
        car_color = get_input()
        if car_color == "":
            return car_dictionary
            flag = False
        else:
            if car_color in car_dictionary:
                car_dictionary[car_color] += 1
            else:
                car_dictionary[car_color] = 1


def use_dictionary():
    '''
    Sorts and prints dictionary
    '''
    #sorts
    global car_dictionary
    car_dictionary = dict(sorted(car_dictionary.items()))
    #prints
    for key ,value in car_dictionary.items():
        print(f"{key}: {value}")





# routine main
car_dictionary = {}
use_dictionary()
get_dictionary()
