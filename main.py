#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f=open('Calc.py')
while True:
    x=float(input('enetr the first number: '))
    symbol=input("please enter your operation symbol[+,-,*,/]: ")
    y=float(input('enetr the second number: '))
    if symbol in('+' , '-' , '*' , '/'): 
        try:
            if   symbol == '+':
                add(x,y)
            elif symbol == '-':
                sub(x,y)
            elif symbol == '*':
                mul(x,y)
            elif symbol == '/':
                div(x,y)
        except TypeError:
            print('Please enter a valid input')
        except ValueError:
            print('Please enter a valid input')
        except ZeroDivisionError:
            print('do not divide by zero')          
    else:
        print('please enter a valid symbol [+,-,*,/] ')
       
    do_clac=input('do you want to perform another operation?[y or n]: ')
    if do_clac=='y':
        print('lets perform another operation')
        continue
    elif do_clac=='n':
        print('thank you')
    break
            
            
        
        


# In[ ]:





# In[ ]:




