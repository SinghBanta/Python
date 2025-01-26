#Datatypes in python

# print(type('A'))
# print(type(1))
# print(type(1.2))
# print(type(4j+2))
# print(type('Banta Singh'))

#Print sum 
# a=3
# b=5
# print(2+4)


#Type Conversion
# a=20
# b=20.10
# print(a+b)

#Type Casting
# a=20
# b="10"
# c=int(b)
# print(a+b)Give Error
# print(int(a+c))

#Taking input in Python
# password=input() #By default it taking string.But we can type cast it into type which we want
# print("The age of Banta Singh is:",22)


#Another example for the same
# name=int(input())# Like int we can take float also
# print("The password is:",name)


#Question do sum by taking inputs
# print("Enter value of a")
# a=int(input())
# print("Enter value of b")
# b=int(input())
# sum=a+b
# print("The sum of a and b is:",a+b)


#Area of Sqaure
# print("Enter side of square")
# side=float(input())
# area=side*side
# print(area)


#Average of floting numbers

# print("Enter number a and b")
# a=int(input())
# b=int(input())
# average=(a+b)/2
# print(average)

#if else
# print("Enter a number a")
# a=int(input())
# b=int(input())
# if(a>=b):
#     print('True')
# else:
#     print('False')


#Concatenation in Strings
# a='Banta'
# b='Singh'
# print(a+b) #or you can do that print('Banta'+'Singh')
# print(len(a)) #It will give length of string

#string indexing
# a='Apna_college'
# # a[0]='o' #It will give error because string is immutable
# print(a[0])

#Slicing in string

# str='Apna_college'
# print(str[0:4]) #It will give Apna   
# print(str[1:])  #It will give pna_college 
# print(str[:4])  #It will give Apna
# print(str[2:6]) #It will give na_c

# Negative Idexing in string using slicing
# str='Apple'
# print(str[-1]) #It will give e
# print(str[-3:-1]) #It will give pl


#Inbuilt functions in string

# str='I am Banta Singh'
# print(str.upper())
# print(str.lower())
# print(str.replace('Banta','Santa'))
# print(str.find('am'))
# print(str.split(' ')) #It will split the string by space
# print(str.endswith('gh'))
# print(str.startswith('I'))
# print(str.capitalize())#It will capitalize the first letter of string
# print(str.count('Banta')) #It will count the number of a in string  


#Question WAP to input user’s first name & print its length.

# print("Enter your name")
# first_name=input()
# last_name=input()

# print(len(first_name))

#ifelse
# print("Enter your marks")
# marks=int(input())

# if(marks>=90):
#     print("A")
# elif(marks>=80 and marks<=90):
#     print("B")
# elif(marks>=70 and marks<=80):
#     print("C")
# else:
#     print("D")
    
    
#odd or even 

# print("Enter a number")
# num=int(input())

# if(num%2==0):
#     print("Even number")
# else:
#     print("odd number")


#greatest number

# print("Enter a number")
# num1=int(input())
# num2=int(input())
# num3=int(input())

# greater=max(num1,num2,num3)
# print(greater)

#multiple of seven
# print("Enter a number")
# num=int(input())

# if(num%7==0):
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7")


#List a built in datatype in python which is mutable.

# students=["Arjan","Ajay","Banta","Aryan"]
# students[0]="Ayush"

# print(students)
# print(len(students))

#list slicing

# marks=[90,80,70,60,50]
# print(marks[:4])
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:2])


#list methods

#In ascending order
# list=[60,40,30,12,35]
# list.sort()
# print(list)

#In descending order
# list=[20,34,21,12,14]
# list.sort(reverse=True)
# print(list)

#In reverse order

# list=[20,34,21,12,14]
# list.reverse()
# print(list)

#append add element at end of the list

# list=[20,34,21,12,14]
# list.append(22)
# print(list)


#insert function in 

# list=[20,34,21,12,14]
# list.insert(2,1)
# print(list)


#remove

# list=[20,34,21,12,14]
# list.remove(21)
# print(list)

#pop

# list=[20,34,21,12,14]
# list.pop(1)
# print(list)


#Question

#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# print("Enter your favourite movies")
# movie1=input()
# movie2=input()
# movie3=input()
# movies=[movie1,movie2,movie3]
# print(movies)


# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

# print("Enter a list")
# list=[1,2,3,2,1]
# list1=list.copy()
# list1.reverse()
# if(list==list1):
#     print("Palindrome")
# else:
#     print("not a palindrome")


# WAP to count the number of students with the “A” grade in the following tuple.

# students=['A','B','C','A','A','B','A','C','A','A']
# print(students.count('A'))
# newList=students.copy()
# newList.sort()
# print(newList)

#Example of eval inbuilt function.
# exp1=eval(input("enter any expression: "))
# print(exp1)


#Dictionary also mutable

# dict={
#     "Name":"Banta Singh",
#     "Roll No.":2127959,
#     "Age":22
# }
# dict["Age"]=23 #we update value here
# print(dict)


#nested dictionary

# students={
#     "student1":{
#     "Name":"Banta Singh",
#     "Roll No.":2127959,
#     "Age":22
# }  
# }
# print(students["student1"]["Name"])


#Dictionary methods

# dict={
#     "Name":"Banta Singh",
#     "Roll No.":2127959,
#     "Age":22
# }
# newDict={
#     "Name":"Ajay Kumar",
#     "Roll No.":2127949,
#     "Age":22
# }


# print(dict.keys()) #return all keys
# print(dict.values()) #return all values
# print(dict.items()) #return all items
# print(dict.get("Name")) #return which value you want according to key.
# dict.update(newDict) #to update sum value in dictionary object.
# print(dict)


#set inbuilt datatype in python

# nums = {1, 2, 3, 4}
#set methods
# nums.add(5)
# print(nums)
# nums.pop()
# print(nums)
# nums.clear()
# print(nums)
# nums.remove(1)
# print(nums)


#union and intersection in set

# set={1,2,3,4,5,6,7}
# set1={23,45,6,3,2,1,0}
# set3=set.union(set1)
# print(set3)
# set4=set.intersection(set3)
# print(set4)


# Store following word meanings in a python dictionary :

# meaning={
#     "Table":'“a piece of furniture”,“list of facts & figures”',
#     "cat":"a small animal"
# }
# print(meaning)


# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.

# The provided code snippet is written in Python and demonstrates how to determine the number of unique subjects from a list. The list subjects contains several programming languages, some of which are repeated multiple times. To find out how many unique subjects are present, the code converts the list into a set using the set() function.

# In Python, a set is a collection type that automatically removes duplicate elements, ensuring that all items are unique. By converting the subjects list to a set, any repeated subjects are filtered out, leaving only unique subjects. The variable unique_subjects holds this set of unique programming languages.

#Example
# subjects=["python","java","C++","python","javascript","java","python","java","C++","C"]
# unique_subjects = set(subjects)
# print("No of classrooms needed:", len(unique_subjects))



# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.


# marks={
#     "Maths":int(input("Enter marks of Maths: ")),
#     "Science":int(input("Enter marks of Science: ")),
#     "English":int(input("Enter marks of English: "))
# }
# print(marks)


# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

# In Python, a set is a collection of unique elements. By default, set treats 9 (integer) and 9.0 (float) as the same value because they are considered equal (9 == 9.0 evaluates to True).
# To store them as separate values, you can use a set of tuples or another structure where the type of the value is explicitly stored. Here's an example:

# unique_set = {(9, int), (9.0, float)} #set of tuples 

# # Adding more values
# unique_set.add((10, int))
# unique_set.add((10.0, float))

# print(unique_set)


















    
    
    













