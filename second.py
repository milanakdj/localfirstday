# collision and cohesiveness
#from one modules to another we use a import

#syntax import nameoftheoperation


import math
import time
import random

# pi=math.pi

# a=math.sin(pi)
# print(a)

# to print every  5 second hello

# while True:
#     print('hello')
#     time.sleep(5)


# to generate a random number 


# while True:
#     n=random.random()# to generate a random number in the range 0 to 5
#     o=random.randint# between 0 to 20
#     print(n)
#     print(o)
#     time.sleep(5)


#another way to get the function 


from random import randint
import datetime

while True:
    n=randint(10,20)

    now=datetime.datetime.today()
    da=datetime.date.today  #for more search python date time
    print(now)
    print(n)
    time.sleep(5)


    #jan 1 1970 is the timestamp
    #timestand look
    #will start to overflow in the 2038



#file manipulation; never forget to close the file after using the file

#with as syntax

#open to open the file
# second argument to open in what type 

#file=open('filename.txt','w')

#with open('filename.txt','w')as file:



