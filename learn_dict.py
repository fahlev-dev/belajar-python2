# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
# print(type(Employee))    
# print("printing Employee data .... ")    
# print(Employee)    

# # Creating an empty Dictionary   
# Dict = {}   
# print("Empty Dictionary: ")   
# print(Dict)   
  
# # Creating a Dictionary   
# # with dict() method   
# Dict = dict({1: 'Java', 2: 'T', 3:'Point'})   
# print("\nCreate Dictionary by using  dict(): ")   
# print(Dict)   
  
# # Creating a Dictionary   
# # with each item as a Pair   
# Dict = dict([(1, 'Devansh'), (2, 'Sharma')])   
# print("\nDictionary with each item as a pair: ")   
# print(Dict)  

# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
# print(type(Employee))  
# print("printing Employee data .... ")  
# print("Name: %s" %Employee["Name"])
# print("Age: %d" %Employee["Age"])
# print("Salary: %d" %Employee["salary"])
# print("Company: %s" %Employee["Company"])

# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
# print(type(Employee))    
# print("printing Employee data .... ")    
# print(Employee)    
# print("Enter the details of the new employee....");   
# Employee["Name"] = input("Name: ")
# Employee["Age"] = int(input("Age: "))
# Employee["salary"] = int(input("Salary: "))
# Employee["Company"] = input("Company: ")
# print("printing new data")
# print(Employee)

# # Creating a Dictionary   
# Dict = {1: 'JavaTpoint', 2: 'Peter', 3: 'Thomas'}   
# Deleting a key    
# using pop() method   
# pop_ele = Dict.pop(3)   
# print(Dict)  


# phonebook = {
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }

# if "Jake" in phonebook:
#     print("Jake is listed in the phonebook")

# if "Jill" in phonebook:
#     print("Jill is not listed in the phonebook")

# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)

# Dict = dict({1:'Microsoft', 2:'Google', 3:'Facebook'})
# print("\n create dictionary by using dict(): ")
# print(Dict)

# Dict = dict([(4, 'Praneeth'), (2, 'Varma')])
# print("\n Dictionary with each item as a pair: ")
# print(Dict)

# Employee = {"Name":"David", "Age":30, "Salary":55000, "Company":"Google"}
# print(type(Employee))
# print("Printing employee data")
# print("Name: %s" %Employee["Name"])
# print("Age: %s" %Employee["Age"])
# print("Salary: %s" %Employee["Salary"])
# print("Company: %s" %Employee["Company"])


# Employee = {"Name":"John", "Age":29, "Salary":25000, "Company": "Google",}
# for x in Employee.items():
#     print(x)

# dict = {7:"Ayan", 5:"Bunny", 8:"Ram", 1:"Bheem"}
# print(sorted(dict))

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
# dict_demo = dict.copy()
# x = dict_demo.pop(1)
# print(x)

# dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
# # items() method  
# print(dict.items())  

dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
print(dict.values())
