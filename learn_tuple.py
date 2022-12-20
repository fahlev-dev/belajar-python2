# Python program to show how to create a tuple  
  
# Creating an empty tuple  
# empty_tuple = ()  
# print("Empty tuple: ", empty_tuple)  
  
# # Creating tuple having integers  
# int_tuple = (4, 6, 8, 10, 12, 14)  
# print("Tuple with integers: ", int_tuple)  
  
# # Creating a tuple having objects of different data types  
# mixed_tuple = (4, "Python", 9.3)  
# print("Tuple with different data types: ", mixed_tuple)  
  
# Creating a nested tuple  
# nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))  
# print("A nested tuple: ", nested_tuple) 

# Python program to show how to access tuple elements  
  
# Creating a tuple  

# tuple_ = ("Python", "Tuple", "Ordered", "Collection")

# print(tuple_[0])
# print(tuple_[1])

# # trying to access element index more than the length of a tuple  
# try:
#     print(tuple_[5])
# except Exception as e:
#     print(e)
# # trying to access elements through the index of floating data type  
# try:
#     print(tuple_[1.0])
# except Exception as e:
#     print(e)

# # Creating a nested tuple
# nested_tuple = ("Tuple", [4,6,2,6], (6,2,6,7))

# # Accesing the index of a nested tuple
# print(nested_tuple[0][3])
# print(nested_tuple[1][1])

# Python program to show how negative indexing works in Python tuples  
  
# Creating a tuple  
# tuple_ = ("Python", "Tuple", "Ordered", "Collection") 

# # Printing elements using negative indices  
# print("Element at -1 index: ", tuple_[-1])

# print("Element between -4 and -1 are: ", tuple_[-4:-1])

# Python program to show how slicing works in Python tuples  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")  
  
# Using slicing to access elements of the tuple  
print("Elements between indices 1 and 3: ", tuple_[1:3])

# Using negative indexing in slicing
print("Elements between indices 0 and -4: ", tuple_[:-4])

# Printing the entire tuple by using the default start and end values.
print("Entire tuple: ", tuple_[:])

# Python program to show how to delete elements of a Python tuple  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")  
  
# Deleting a particular element of the tuple
try:
    del tuple_[3]
    print(tuple_)
except Exception as e:
    print(e)

# Deleting the variable from the global space of the program  
del tuple_

# Trying accessing the tuple after deleting it  
try:
    print(tuple_)
except Exception as e:
    print(e)

# Python program to show repetition in tuples  
    
tuple_ = ('Python',"Tuples")  
print("Original tuple is: ", tuple_)  
  
# Repeting the tuple elements  
tuple_ = tuple_ * 3  
print("New tuple is: ", tuple_) 

# Python program to show how to tuple methods (.index() and .count()) work  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")  
  
# Counting the occurrence of an element of the tuple using the count() method  
print(tuple_.count('Ordered'))  
  
# Getting the index of an element using the index() method  
print(tuple_.index('Ordered')) # This method returns index of the first occurrence of the element  

# Python program to show how to perform membership test for tuples  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")  
  
# In operator  
print('Tuple' in tuple_)  
print('Items' in tuple_)  
  
# Not in operator  
print('Immutable' not in tuple_)  
print('Items' not in tuple_)  

# Python program to show how to iterate over tuple elements  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable")  
  
# Iterating over tuple elements using a for loop  
for item in tuple_:  
    print(item)  

# Python program to show that Python tuples are immutable objects  
  
# Creating a tuple  
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", [1,2,3,4])  
  
# Trying to change the element at index 2  
try:  
    tuple_[2] = "Items"  
    print(tuple_)  
except Exception as e:  
    print( e )  
  
# But inside a tuple, we can change elements of a mutable object  
tuple_[-1][2] = 10   
print(tuple_)  
  
# Changing the whole tuple  
tuple_ = ("Python", "Items")  
print(tuple_)  