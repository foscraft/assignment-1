'''
Python program to remove duplicates from a list
'''

def drop_duplicates(my_list):
    return list(set(my_list))

#invoke function 
skae_list = ['me','you','we','you','them','them']
print(drop_duplicates(skae_list))