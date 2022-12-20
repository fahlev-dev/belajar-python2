Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    

# Creating an empty Dictionary   
Dict = {}   
print("Empty Dictionary: ")   
print(Dict)   
  
# Creating a Dictionary   
# with dict() method   
Dict = dict({1: 'Java', 2: 'T', 3:'Point'})   
print("\nCreate Dictionary by using  dict(): ")   
print(Dict)   
  
# Creating a Dictionary   
# with each item as a Pair   
Dict = dict([(1, 'Devansh'), (2, 'Sharma')])   
print("\nDictionary with each item as a pair: ")   
print(Dict)  

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print("Name: %s" %Employee["Name"])
print("Age: %d" %Employee["Age"])
print("Salary: %d" %Employee["salary"])
print("Company: %s" %Employee["Company"])

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

# Creating a Dictionary   
Dict = {1: 'JavaTpoint', 2: 'Peter', 3: 'Thomas'}   
# Deleting a key    
# using pop() method   
pop_ele = Dict.pop(3)   
print(Dict)  

