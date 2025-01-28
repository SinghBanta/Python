#Question on string.

#take a input as string and then count how many lowercase ,uppercase and digit's count.

# sent=input("Enter a string: ")

# This below  lines uses a generator expression within the sum() function to count the number of lowercase letters in the string sent. The generator expression iterates over each character c in the string and checks if it is lowercase using the islower() method. If the character is lowercase, it yields 1, and the sum() function adds up all the 1s to get the total count of lowercase letters, which is stored in the variable lower_case.

# lower_case=sum(1 for c in sent if c.islower())
# upper_case=sum(1 for c in sent if c.isupper())
# digit_count=sum(1 for c in sent if c.isdigit())

# print("Lowercase letter: ",lower_case)
# print("Uppercase letter: ",upper_case)
# print("No of digit in sentence:",digit_count)


#Another way to do same problem.

# sent = input("Enter a string: ")
# lower = 0
# upper = 0
# digit = 0

# for i in sent:
#     if i.islower():
#         lower += 1
#     elif i.isupper():
#         upper += 1
#     elif i.isdigit():
#         digit += 1

# print("Lowercase letters:", lower)
# print("Uppercase letters:", upper)
# print("Number of digits:", digit)



#take string as input and then count no. of lowercase,uppercase and digit in string
# sent = input("Enter a string: ")

# start_hello = False
# end_hello = False

# for i in range(len(sent) - 4):
#     if sent[i:i+5].lower() == 'hello':
#         if i == 0:
#             start_hello = True
#         if i == len(sent) - 5:
#             end_hello = True

# if start_hello and end_hello:
#     print("The string starts with 'hello' as well as ends with 'hello'")
# elif start_hello:
#     print("The string starts with 'hello' or 'Hello'.")
# elif end_hello:
#     print("The string ends with 'hello' or 'Hello'.")
  
  
#Another way to do same problem

# sent = input("Enter a string: ").casefold()
# if sent.startswith('hello') and sent.endswith('hello'):
#     print("The string starts with 'hello' as well as ends with 'hello'")
# elif sent.startswith("hello") :
#     print("The string starts with 'hello'")
# elif sent.endswith("hello"):
#     print("The string ends with 'hello'.")  
       
       
#take string as input and see that is 'a' present  in string and it's count.
# str = input("Enter a string: ")
# count_a = 0

# for char in str:
#     if char == 'a':
#         count_a += 1
# if count_a > 0:
#     print(f"The string contains 'a' and it appears {count_a} times.")
# else:
#     print("The string does not contain 'a'.")
    
    
    
#Another way to do same problem.
# str=input("Enter a string: ")
# if 'a' in str:
#     count_a = str.count('a')
#     print(f"The string contains 'a' and it appears {count_a} times.")
# else:
#     print("The string does not contain 'a'.")





        
        
        
        














        
