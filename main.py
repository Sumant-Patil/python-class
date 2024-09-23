# identifiers
# firstly it should start with alphabet
# it can contain alph,numeric,and one special char '_'

# data types
# fundamental(int ,float,bool,complex,str,bytes)  and advanced(list ,tuple,set,dictionary)
# no datatype name char in python

# int can be stored in decimal,binary,octal,hexa
# in complex data we can use this int types in real part only

# re usability

# immutability ,mutability,re-usability (are for data types)
# in python every thing is object
# immutability (can not do overriding)
# every data type is immutable

# type casting
# int(),bool(),float(),str(),bool()

# we can convert any type to integer except complex type
# if we want to convert string to int type ,string must contain valid int of base 10

# float to complex not possible
# string to float can be possible but it must contain valid data type or literal

# bool conversion
# when you convert any data type into the bool you will not get any error

# operators with various combination of data types

# arithmetic operator with string
# '+' is used  to concatenate two strings
# '*' is used to make multiple time of the same string
# when we compare two str we compare each literal and for < or > we compare till we get desired result

# logical operators
# x and y --> return x if x is false otherwise y is evaluated
# x or y --> return x if x is true otherwise y is evaluated
# note  in python there is no word like ternary operator in python

# special data types
# range is a special data type

# none

# a = None
# print( a )
# print( id(a))

# multiple assignment in python
# a,b=34,None
# a,b=b,a
# print(a,b)

# advanced data type
# list,tuple,dictionary,set
# if we want to represent a group of values as a single entity where insertion order required to be preserve
# #and duplicates are allowed then we should go for list data type

# heterogeneous elements are allowed
# duplicates are allowed
# growable in nature values should be in closed with square brackets
# in python indexing starts from zero
# list is mutable in nature

# tuple
# it  is a immutable list

# slicing

# s="naman"
# print(s==s[::-1])

# dictionary
# which stores the values in the java scripts form( key value pairs )

# control statement
# if elif else
# looping statement
# transfer statement ---> break,continue ,pass
# looping statement
# for and while loop only
# for else
# while else

# how to target container
# list tuple dictionary

# l=['rahul','dub','vau','ey']
# t=(1,2,3)
# d={'name':"vas",'age':8}
# for i in d.items():
#    print(i)

# unpacking
# list unpacking
# name ,age =('rahul',78)
# print(name)
# print(age)

# set data types
# string is a collection of char datat types


# s=input("enter")
# s1=s2=output=""
# for x in s:
#    if x.isalpha():
#       s1+=x
#   else:
#       s2+=x
# for x in sorted(s1):
#   output+=x
# for x in sorted(s2):
#  output+=x

# print(output)
# d = input("please enter data ")
# d1 = d.split(" ")
# print('@'.join(d1))
# isdigit()

# isalpha()
# isalnum()
# islower()

# print(chr(128589))

# tuple
# slicing and indexing is applied on tuple .
# tuple is immutable .
# some important fun of tuple .
# len ,count,index,sorted,min, max

# tuple unpacking
# there is no word like tuple comprehension
# n= int(input("range"))
# t =(i**2 for i in range(n))
# print(t)
# print(type(t))

# set does not have or support indexing and slicing
# if you want to represent a single entity then we should go for the sets
# in sets duplicate are not allowed
# in sets insertion order is not present but sorting can be done
# the element of set can be heterogeneous
# set objects are mutable
# there are certain operation can be performed on the set union ,intersection (copy ,pop ,remove ,discard).all function can be used with set.
# union operation
# difference
# membership operator is applicable on set

# set comprehension
# t =(i**2 for i in range(n))
# print(t)
# print(type(t))

# t={i**2 for i in range(5)}
# s={5,6,1,7}
# print(t.union(s))
# print(t.intersection(s))
# print(t-s)

# write a program to count vowel in str


# w = input(" enter str ")
# s = set(w)
# v= {'a','e','i','o','u'}
# print(s&v)

# d={i: i**2 for i in range(5)}
# d.setdefault(5,"vasu")
# print(d)
# d.clear,length(no.of items), d.get(key)->returns value corresponding to given key,d.get(key,"default value you want")
# set default
# wap to find no of occurrence of each letter in given string
# wAap to find no of occurrence of each vowel in given string

# print(1,2,3,sep=', ')
# print(1,2,3,end="   ")
# a=12
# print("it is an integer %d or %i "%(a,a))

d = int(input("enter size of 2d matrix ").split(" "))
m = d[0]
n = d[1]
print(type(m))


