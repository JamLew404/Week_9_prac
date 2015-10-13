__author__ = 'Jeffrey'
import csv


def list_of_tuples():
    guitars_list = []
    in_file = open('guitars.csv', 'r', newline='')
    for line in in_file:
        words = line.strip().split(",")
        guitars_list.append(tuple(words))
    print(guitars_list)
    in_file.close()

list_of_tuples()
