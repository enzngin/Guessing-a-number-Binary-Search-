# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 07:17:04 2020

@author: USER
"""


def guess_number_pc(upper_bound):
    up= upper_bound
    down = 1
    print("Guess a number between 1 and 10 in your mind.")
    i = True
    while i:
        mid = int((up+down) / 2)
        print("Is the number {number} less (0), equal (1), or greater (2) than your number?".format(number = mid))
        a = int(input("Enter your number: "))
        if a == 0: # bu benimkinden küçük
            down = mid
        elif a == 2:
            up = mid
        elif a == 1:
            print("Computer is done. Your number is {number}".format(number = mid))
            i = False
            
guess_number_pc(10)   

         
          
            
        
        
      
        
        
    
