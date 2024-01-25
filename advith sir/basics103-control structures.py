# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:46:53 2023

@author: rites
"""

#control Structures

score=50

if score>60:
    print('you are Qualified')
else:
    print('you are not Qualified')    

score=70
Edu='Btech'

if score>60 and Edu == 'Btech':
    print('you are Qualified')
else:
    print('you are not Qualified')  


score=70
Edu='Btech'

if score>60 and (Edu == 'Btech' or Edu == 'Bcom'):
    print('you are Qualified')
else:
    print('you are not Qualified')  
    
#if -elif -else
score = 70
Edu = 'Bcom'

 
if score>60 and Edu == 'Btech':
    print('You can apply for Data scienties')
elif score >60 and Edu == 'Bcom':
    print('You can apply for jr.analyst')
else:
    print('Better luck next time')    
    
# Nested if 

status = 'nonIndian'
Gender= 'Female'
age=22
if (status == 'Indian'):
    if(Gender== 'Male'):
        if(age>21):
            print('you are qualified for army')
        else:
            print('thanks for interest try next year')
    elif (Gender== 'Female'):
        if(age>21):
            print('You are qualified for airfore ')
        else:
            print('thanks for interest try next year')
else:
    print('You are invalid criteria')            

#==========================================================



