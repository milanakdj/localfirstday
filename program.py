# # # # # # # # # # # # # # print('Hello, World!')

# # # # # # # # # # # # # # s="hellow\"world\""
# # # # # # # # # # # # # # print(s)


# # # # # # # # # # # # # # i= input('enter a name')

# # # # # # # # # # # # # # print(i)

# # # # # # # # # # # # # # a=[23,35.6,'aarhon',[1,2,3]]

# # # # # # # # # # # # # # print(len(a))


# # # # # # # # # # # # # # twod=[
# # # # # # # # # # # # # #     [1,3],
# # # # # # # # # # # # # #     [0,1]
# # # # # # # # # # # # # # ]



# # # # # # # # # # # # # # print(s[0])


# # # # # # # # # # # # # li =[]

# # # # # # # # # # # # # print(li)

# # # # # # # # # # # # # li.append(45) # add to the end of the list
# # # # # # # # # # # # # li.append(10)
# # # # # # # # # # # # # print(li)


# # # # # # # # # # # # # li=[1,2,3,4,]# you can add the comma and nothing at the end after it


# # # # # # # # # # # # # li.insert(0,3333)


# # # # # # # # # # # # # print(li)



# # # # # # # # # # # # # li.pop() #to remove the last element in the list

# # # # # # # # # # # # # print(li)


# # # # # # # # # # # # # li.remove(3)#removes the selected element from the list


# # # # # # # # # # # # # print(li)




# # # # # # # # # # # # #tuples you can not change the elements

# # # # # # # # # # # # # look into tuples, set and list


# # # # # # # # # # # # #dictionary syntax
# # # # # # # # # # # # # d={"name":"name is this",
# # # # # # # # # # # # # "college":"bla"}
# # # # # # # # # # # # #d.keys()

# # # # # # # # # # # # #d.values()
# # # # # # # # # # # # #d["name"]


# # # # # # # # # # # # d={
# # # # # # # # # # # #     'name':'fdslk',
# # # # # # # # # # # #     'college':'fdsfds'
# # # # # # # # # # # # }


# # # # # # # # # # # # name=d['name']

# # # # # # # # # # # # print (name)


# # # # # # # # # # # # print(d.values)
# # # # # # # # # # # # print(d.items())



# # # # # # # # # # # if 3==3:
# # # # # # # # # # #     print("true")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("not true")



# # # # # # # # # # #boolean gata type

# # # # # # # # # # #True, False ,,, starting characters capital
# # # # # # # # # # #operator types and, or and not



# # # # # # # # # # # Microsoft Windows [Version 10.0.18362.476]
# # # # # # # # # # # (c) 2019 Microsoft Corporation. All rights reserved.

# # # # # # # # # # # C:\Users\user>python
# # # # # # # # # # # Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
# # # # # # # # # # # Type "help", "copyright", "credits" or "license" for more information.
# # # # # # # # # # # >>> True and True
# # # # # # # # # # # True
# # # # # # # # # # # >>> True and False
# # # # # # # # # # # False
# # # # # # # # # # # >>> False or True
# # # # # # # # # # # True
# # # # # # # # # # # >>> not False and True
# # # # # # # # # # # True
# # # # # # # # # # # >>> not(not False and True)
# # # # # # # # # # # False
# # # # # # # # # # # >>> 2=3 and 3>4
# # # # # # # # # # #   File "<stdin>", line 1
# # # # # # # # # # # SyntaxError: can't assign to literal
# # # # # # # # # # # >>> 2==3 and 3>4
# # # # # # # # # # # False
# # # # # # # # # # # >>>




# # # # # # # # # # # look into demorgans theorem

# # # # # # # # # # #not(a and b) = not a or not b



# # # # # # # # # # n=int(input("enter a number"))

# # # # # # # # # # if n==0:
# # # # # # # # # #     print("true is the zero")

# # # # # # # # # # elif n%2==0:
# # # # # # # # # #     print("the entered number is even")
# # # # # # # # # # else:
# # # # # # # # # #     print("not true is that the entered number is even")



# # # # # # # # vowels=["a","e","i","o","u"]


# # # # # # # # ch="i"


# # # # # # # # # if ch in vowels:
# # # # # # # # #     print(True)
# # # # # # # # # else:
# # # # # # # # #     print(False)


# # # # # # # # #terneray operators


# # # # # # # # # int a=n%2==0 ? 1:0;


# # # # # # # # # in python the same things can be done with the following code

# # # # # # # # #print ('yes') if ch in vowels else print('no')

# # # # # # # # print ('yes') if ch in vowels else print ('no')



# # # # # # # # we have a user and a set of number, with odd number is group a and even in group b

# # # # # # # # group="a" if rollno%2==1 else "b"

# # # # # # # # to check whether a number is in a list li=[2,3,4,]
# # # # # # # # if n not in li ; when you want to run the code only when the number is not in the given list





# # # # # # # #looping
# # # # # # # #no do while loop; we can do this with while loop

# # # # # # # # for loop when we extract all the elements

# # # # # # # # while loop is ran when we need the condition to be met



# # # # # # # for i in range(10):
# # # # # # #     print(i)

# # # # # # #for vowels in vowels:
# # # # # # #   print(vowels)

# # # # # # vowels=["a","e"]

# # # # # # string ="my name is this"


# # # # # # for characters in string:
# # # # # #     if characters in vowels: 
# # # # # #         print(characters)



# # # # # while True:    # infinite loops
# # # # #     print('yellow')



# # # # # while input('repeat again?')=="y":
# # # # #     print["hello again"]



# # # # names=["milan","asdf","fds","Fdsafds"]


# # # # for name in names:
# # # #     print('hello', name, "you have a permission to enter")
# # # #     if name=="asdf":
# # # #         continue
# # # #     print("hello")

    



# # # s="this is a sentence. this is another sentence"

# # # print(s.split)


# # # print(s.split('.'))




# # # li=["thsa","tds","FDsafsd"]



# # # f=".".join(li)

# # # print(f)



# # # #raw string


# # # o=r"hello\world"
# # # p="hello\nworld"
# # # print(o)
# # # print(p)




# # # list and we need the squred of the number in the first list

# # # to do this in a single line we can do list comprehension


# # #newli=[x*x for x in li]


# # # to add condition 
# # # if odd then no squaring 
# # #newli=[x*x for x in li, if x%2==1]


# # li=range(10)


# # newli=[x*x for x in li if x%2==1]

# # print (newli)




# # function
#     # takes value does some processing and may and may not return a value

# # no need to specify datatype or return type


# def sum(a,b):
#     return(a+b)


# c=sum(2,4)

# print(c)




#explicit 

def sum(a,b=6):
    return(a+b)


c=sum(2,4)
d=sum(3)
print(sum(b=3))
print(c)
print(d)

