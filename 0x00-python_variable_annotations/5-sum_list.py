#!/usr/bin/env python3
"""type-annotated function sum_list which takes a 
list input_list of floats as argument
"""

def sum_list(input_list: list[float]) -> float:
    '''returns their sum as a float
    
    '''

    return float(sum(input_list))