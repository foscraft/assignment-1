'''
function that finds out if the year is leap and returns false or True.
'''

def find_year(year):
    return year % 4 == 0 and year % 100 !=0 or year % 400 == 0

#invoking the function
print(find_year(2400))