#helper_functions.py by Stephen Spradling in DS36
#
import numpy as np
import random

#Part 2
#Exercise 1
def random_phrase():
    adv = ['red', 'purple', 'light',
           'heavy', 'clean', 'dirty',
           'cold', 'hot']
    noun = ['cat', 'dog', 'car', 'train',
            'house', 'tree', 'flowers', 'bug']

    return (random.choice(adv) + ' ' + random.choice(noun))

#Testing ouput for Debugging
#print(random_phrase())

#Exercise 2
def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

#Testing output for Debugging
#print(random_float(1, 10))

#Exercise 3
def random_bowling_score():
    return random.randint(0, 301)

#Testing output for Debugging
#print(random_bowling_score())

#Exercise 4
def silly_tuple():
    st = (random_phrase(), round(random_float(1, 5), 1), random_bowling_score())
    return st

#Testing output for Debugging
#print(silly_tuple())

#Exercise 5
def silly_tuple_list(num_tuples):
    stl = []
    for i in range(1, num_tuples + 1):
        stl.append(silly_tuple())
    return stl

#Testing output for Debugging
#print(silly_tuple_list(4))

#Part 3
def num_count(df):
    return df.isnull().sum()

