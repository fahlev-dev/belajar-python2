Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)

Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nAdding other months to the set...");    
Months.add("July");    
Months.add ("August");    
print("\nPrinting the modified set...");    
print(Months)    
print("\nlooping through the set elements ... ")    
for i in Months:    
    print(i)    

Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nupdating the original set ... ")    
Months.update(["July","August","September","October"]);    
print("\nprinting the modified set ... ")     
print(Months);

months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    
print("\nPrinting the modified set...");    
print(months)    
print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)   

months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    
print("\nPrinting the modified set...");    
print(months)    
print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)    

Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving some months from the set...");    
Months.pop();    
Months.pop();    
print("\nPrinting the modified set...");    
print(Months)    

months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.remove("January");    
months.remove("May");    
print("\nPrinting the modified set...");    
print(months)   

Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving all the items from the set...");    
Months.clear()    
print("\nPrinting the modified set...")    
print(Months)    

Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2) #printing the union of the sets     

Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) #prints the intersection of the two sets 

set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2)) #prints the intersection of the two sets    

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1-Days2) #{"Wednesday", "Thursday" will be printed}  

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2)) # prints the difference of the two sets Days1 and Days2    

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a^b  
print(c)  

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a.symmetric_difference(b)  
print(c)  

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday"}    
Days3 = {"Monday", "Tuesday", "Friday"}    
    
#Days1 is the superset of Days2 hence it will print true.     
print (Days1>Days2)     
    
#prints false since Days1 is not the subset of Days2     
print (Days1<Days2)    
    
#prints false since Days2 and Days3 are not equivalent     
print (Days2 == Days3)    

Dictionary = {"Name":"John", "Country":"USA", "ID":101}     
print(type(Dictionary))    
Frozenset = frozenset(Dictionary); #Frozenset will contain the keys of the dictionary    
print(type(Frozenset))    
for i in Frozenset:     
    print(i)    