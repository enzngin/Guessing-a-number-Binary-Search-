# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 01:14:37 2020

@author: USER
"""

from random import randint
            
def guess_number_pc(upper_bound): 
    pc_number = randint(0, upper_bound)
    print("Hey! I am guessing a number between 1 and {upper}.".format(upper = upper_bound))
   
    
    i = True
    while i:
        a = int(input("Enter your tip: "))
        if a < pc_number: 
            print("My number is bigger")
        elif a > pc_number:
            print("My number is less")
        elif pc_number == a:
            print("Yeah, that is it!")
            i = False 



guess_number_pc(10)
 
