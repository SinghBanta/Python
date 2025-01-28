# Question 
# tuple=(10,20,30,40)

# min_val=min(tuple)
# max_val=max(tuple)
# print("Minimum value in Tuple is:",min_val)
# print("Maximum value in Tuple is:",max_val)

# find second maximum

# second_max_val = tuple[-2]
# print("Second maximum value in Tuple is:", second_max_val)


#Nested Tuples

# tup1=(2,4)
# tup2=(3,5)
# nested1=str(tup1)
# nested2=str(tup2)
# nested=nested1+nested2
# print(nested)


#Indexing and slicing in python

# tuple=(1,2,3,4)
# index=tuple[1]
# print(index)

#create nested loop

# tuple=(1,2,3,4,5,6,7,8,9,10)
# for i in range(10):
#     for j in range(3,6):
#         nested_tuple = (tuple[i], tuple[j])
#         print(nested_tuple)
        
        
        
#create a tuple and then repeated ones
# count1=0
# tup=(1,3,4,32,1,1,1)  
# for i in set(tup):
#     if tup.count(i) > 1:
#         print(i * tup.count(i))
        
        


#Assignment Question
# Convert nested tuple into flatter tuple

# To flatten this nested tuple, the code uses a generator expression within the tuple() function. The generator expression item for sublist in nested_tuple for item in sublist iterates over each sublist (inner tuple) in nested_tuple and then iterates over each item in these sublists. This effectively extracts all individual elements from the nested structure and combines them into a single, flat tuple.

# nested_tuple = ((1, 2), (3, 4), (5, 6))
# flat_tuple = tuple(item for sublist in nested_tuple for item in sublist)
# print(flat_tuple)


# Create tuple using for loop from (1-10)

# generated_tuple = tuple(i for i in range(1, 11))
# print(generated_tuple)


# Create nested tuple and find length of longest nested tuple

# nested_tuple = ((1, 2), (3, 4, 5), (6, 7, 8, 9))
# lengths = [len(t) for t in nested_tuple]
# longest_length = max(lengths)
# print("Length of the longest nested tuple is:", longest_length)


# Check if two tuples are anagrams

# def are_anagrams(tup1, tup2):
#     return sorted(tup1) == sorted(tup2)
# tup1 = (1, 2, 3)
# tup2 = (3, 2, 1)
# tup3 = (1, 2, 4)
# print("Are tup1 and tup2 anagrams?", are_anagrams(tup1, tup2))
# print("Are tup1 and tup3 anagrams?", are_anagrams(tup1, tup3))






        





