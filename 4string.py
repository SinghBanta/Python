#Methods used in string

#capitalize()

# str="My name is BANTA singh"
# print(str.capitalize())

#casefold(), lower() work same
 
# str="My name IS BANTA singh"
# print(str.casefold())
# print(str.lower())

#casefold(), lower() work same but there is difference between them that is
 
# str = "My name is Banta ßingh"
# print(str.lower())
# print(str.casefold())

#center()

# str="My name is Banta Singh"
# print(str.center(100,"-"))


#count()

# str="hello world"
# print(str.count('o'))

#Alternate way to count

# str="hello world"
# count=0

# for i in range(len(str)):
#     if(str[i] == 'o'):
#         count=count+1
        
# print(count)  


# Count Substring Occurrences with Start and End parameter

# s = "apple banana apple grape apple"
# substring = "apple"

# # Using start and end parameters to count occurrences 
# # of "apple" within a specific range
# res = s.count(substring, 1, 30)  

# print(res)

#encode() 
#This method in Python is used to convert a string into bytes using a specified encoding format. This method is beneficial when working with data that needs to be stored or transmitted in a specific encoding format, such as UTF-8, ASCII, or others

# Encoding a string with UTF-8
# a = "Python is fun!"
# utf8_encoded = a.encode("utf-8")
# print(utf8_encoded)


#Encoding with ASCII and handling errors
# a = "Pythön"
# encoded_ascii = a.encode("ascii", errors="replace")
# print(encoded_ascii)

# Encoding with XML character references
# a = "Pythön"
# encoded_xml = a.encode("ascii", errors="xmlcharrefreplace")
# print(encoded_xml)

# Using backslash escapes
# a = "Pythön"
# encoded_backslash = a.encode("ascii", errors="backslashreplace")
# print(encoded_backslash)


#endswith(suffix, start, end)
# s = "BantasinghBanta"
# res = s.endswith(("Banta", "com", "org"))
# print(res)  # This will print True because 'geeks' is one of the options

# Alternate way to write this endswith() code
# s = "BantasinghBanta"
# suffixes = ("Banta", "com", "org")
# res = any(s[-len(suffix):] == suffix for suffix in suffixes)
# print(res)  # This will print True because 'Banta' is one of the options


#Alternate way to write this startswith() code without using startswith() function.
# s = "BantasinghBanta"
# prefixes = ("Banta", "com", "org")
# result = any(s[:len(prefix)] == prefix for prefix in prefixes)
# print(result)


#s.find(substring, start, end))

# s = "abc abc abc"
# index = s.find("abc", 4)
# print(index)  # This will print 8

#Alternate way to write this find() code without using find() function.
# s = "abc def ghi"

# for i in range(len(s)):
#     if s[i:i+3] == "ghi":
#         print(i)


#Example
# Function Execution: When the function is executed with these arguments, it calculates the sum 1 + 2 + 1 + 7, which equals 11. This result is returned by the function and stored in the variable value.

# def function(a,b,c=1,d=5):

#     return a+b+c+d

# #Driver's code
# value = function(1,2,d=7)
# print(value)
        
               
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



#Question asked by companies like grab,intuit and sprinkler on coding ninja.
# Example :
# Let S = “c1 O$d@eeD o1c”.
# If we ignore the special characters, whitespaces and convert all uppercase letters to lowercase, we get S = “c1odeedo1c”, which is a palindrome. Hence, the given string is also a palindrome.



# def checkPalindrome(str):
#     str=''.join(char.lower() for char in str if char.isalnum())#The ''.join(...) function joins the filtered lowercase characters into a new string.The empty string ('') is the separator, so the characters are combined without any spaces.
#     #The ''.join(...) function joins the filtered lowercase characters into a new string.
#     # The empty string ('') is the separator, so the characters are combined without any spaces.
    
#     l=0
#     r=len(str)-1
    
#     while(l<r):
#         if(str[l]!=str[r]):
#             return False
#         l+=1
#         r-=1
#         return True
    
    
# str= 'c1 O$d@eeD o1c'#it have special character as well as space
# print(checkPalindrome(str))


#Convert uppercase character to lower case using ASCII value.
#lowecase letters range 97-122 and uppercase letter range 65-90
#To convert in lowercase +32 and to convert in uppercase -32

# char=input("Enter a character: ")
# if 'a' <= char <= 'z':
#     char = chr(ord(char)-32)
# elif 'A' <= char <= 'Z':
#     char = chr(ord(char)+32)
# print("Converted character:", char)



#Convert uppercase character to lower case using ASCII value.

# sent = input("Enter a string: ")
# converted_str = ""

# for char in sent:
#     if 'a' <= char <= 'z':
#         converted_str += chr(ord(char) - 32)
#     elif 'A' <= char <= 'Z':
#         converted_str += chr(ord(char) + 32)
#     else:
#         converted_str += char

# print("Converted string:", converted_str)


#Input a string and count vowels,consonent,special chararcter and space.
# str=input("Enter a string")
# special_char_count = 0
# consonant_count = 0
# vowel_count = 0
# space_count = 0

# vowels = "aeiouAEIOU"

# for char in str:
#     if char in vowels:
#         vowel_count += 1
#     elif char.isalpha():
#         consonant_count += 1
#     elif char.isspace():
#         space_count += 1
#     else:
#         special_char_count += 1

# print("Special characters:", special_char_count)
# print("Consonants:", consonant_count)
# print("Vowels:", vowel_count)
# print("Spaces:", space_count)

#take input as string and then convert first character of every word in uppercase.
# def convertString(str):
#     result = ""
#     n = len(str)
#     for i in range(n):
#         if i==0 or str[i-1]==' ':
#             result+=str[i].upper()
#         else:
#             result+=str[i]
#     return result

# str=input("Enter a string: ")
# print(convertString(str))














      
        
        
        
        










        
        
        
        














        
