# for loop

# Print number from1 to 100
# for i in range(1,101):
#     print(i)


#Print numbers 100 to 1
# for i in range(100, 0, -1): #This loop starts at 100 and decrements by 1 until it reaches 1 (inclusive). The range function is used with three arguments: start (100), stop (0, exclusive), and step (-1).
#     print(i)


# Print the multiplication table of a number n.
# number=int(input("Enter any number: "))
# for i in range(1,11):
#     print(number, "x", i, "=", number * i)


#Print the elements of the following list using a loop
# fruits = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for i in fruits:
#     print(i)


# Search for a number x in this tuple using loop
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 25

# for i in range(len(tup)):
#     if x == tup[i]:
#         print("Element found at index", i)
#         break
# else:
#     print("Not found")


#Range function in for loop
#This loop starts at 1 and increments by 2 until it reaches 10 (exclusive). The range function is used with three arguments: start (1), stop (10, exclusive), and step (2).

#Example for loop with range function
# for i in range(1, 10, 2):


#while loop
#The while loop is used to execute a block of code repeatedly as long as a specified condition is true. The condition is checked before each iteration, and the loop continues until the condition becomes false.


#sum of first n numbers using while loop
# # Prompt the user to enter a number
# num = int(input("Enter a number"))

# # Initialize the sum to 0
# sum = 0

# # Loop while num is greater than 0
# while (num > 0):
#     # Print the current sum
#     print(sum)
    
#     # Add the current num to the sum
#     sum = sum + num
    
#     # Decrement num by 1
#     num = num - 1

# # Print the final sum of the first n numbers
# print("Sum of first n numbers is:", sum)
    

#WAP to find the factorial of first n numbers. (using for)

# num = int(input("Enter a number"))

# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i  # Multiply the current number with the factorial
#     print(factorial)






