import csv
import pprint
'''
Write a Python program to read a given CSV file as a dictionary. Feel free to read
any CSV of your choice.
'''
def csv_to_dict(path):      
    return list(csv.DictReader(open(path, 'r')))

#invokinf the function
print(csv_to_dict('./sample.csv'))

#You can use pprint to print out cleaner and more beautiful outputs with new lines.

#pprint.pprint(csv_to_dict('./sample.csv'))