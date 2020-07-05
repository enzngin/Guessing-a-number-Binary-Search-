# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:14:32 2020

@author: USER
"""

from random import randint
            
def guess_number_pc(upper_bound): 
    a_number = randint(0, upper_bound) #7
    up= upper_bound
    down = 0
    attempts = 0
    print("A: I guess a number from 1 to {upper}".format(upper = upper_bound))
   
    i = True
    while i:
        
        mid = (up+down) / 2 #5
        b_number = mid #9
        attempts = attempts + 1
        
        print("B: your number is: {number}".format(number = b_number))
        if b_number < a_number: 
            print("A: My number is bigger")
            down = mid
        elif b_number > a_number:
            print("A: My number is smaller")
            up = mid
        elif b_number == a_number:
            print("Yeah, that is it!")
            print("Estimated on {number} attempts".format(number = attempts))
            i = False 



guess_number_pc(10)
 
