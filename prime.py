"""start of script
file name: Python-practice
author: Lakshay
tool: pycharm
created:18/02/2021
"""

'''1. Listing of prime no without using for loop'''
import sympy
print(list(sympy.primerange(0,100)))

'''2.sys module'''
import sys,os
print("you have entered :", sys.argv[1], sys.argv[2],sys.argv[3])
print(os.getcwd())

'''3.os module '''
import os
print(os.getcwd())
print(os.name)
print(os.path)
print(os.access('python_scipting', os.R_OK)
print(os.access('python_scipting', os.W_OK)
print(os.access('python_scipting', os.X_OK)
print(os.listdir("c:\\"))
print(os.rmdir("python_scripting"))
print(os.mkdir('test101'))


'''4.bitwise operator'''
x=int(input('enter 0 or 1 : '))
y=int(input('enter 0 or 1 : '))
print('AND cobdition of',x,'and',y,'is: ',x&y)
print('OR cobdition of',x,'and',y,'is: ',x|y)
print('NOT cobdition of',x,'and',y,'is: ',~x,'and',~y)
print('NOR cobdition of',x,'and',y,'is: ',x^y)


'''end of script'''
