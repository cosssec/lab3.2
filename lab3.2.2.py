'''
This module works with navigation within .json file.
'''
import json


def read_data(path):
    '''
    Opens .json file and returns it as dictionary. 
    '''

    file = open(path, 'r', encoding='UTF-8')
    data = json.load(file)
    return data


# read_data("frienfs_list_Obama.json")


def navigation(data):
    '''
    Navigates through file.
    '''

    if isinstance(data, dict):
        keys = list(data.keys())
        print("Please choose key:")
        print(keys)
        answer = str(input())
        while True:
            if answer in keys:
                data = data[answer]
                return navigation(data)
            else:
                print("Please print correct key:")
                answer = str(input())

    elif isinstance(data, list):
        print(
            f'"Please enter the index of the element of the list youd like to see in range from 0 to {len(data)}"')
        idx = int(input())
        while True:
            if idx in range(0, len(data)+1):
                data = data[idx]
                return navigation(data)
            else:
                print("Please print correct index:")
                idx = int(input())
    else:
        return data


# print(navigation(read_data("example_2.json")))


if __name__ == '__main__':
    print("Hello user! Here you can navigate your json file. Please enter file path:")
    path = str(input())
    print(navigation(read_data(path)))
    print('Thanks, bye!')
