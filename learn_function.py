def square(num):
    """
    This function computes the square of the number
    """
    return num**2

object_ = square(9)
print("The square of the number is: ", object_)

# Defining a function
def a_function(string):
    "This prints the value of length of string"
    return len(string)

# Calling the function we defined
print("Length of the string Function is: ", a_function("Functions"))
print("Length of the string Pythong is: ", a_function("Python"))

def square(my_list):
    """This function will find the square of items in list"""
    squares = []
    for I in my_list:
        squares.append(I**2)
    return squares

# calling the defined function
list_ = [45,52,13]
result = square(list_)
print("Squares of the list is: ", result)

# Python code to demonstrate the use of default arguments  
# defining a function  
def function( num1, num2 = 40 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
   
   
# Calling the function and passing only one argument  
print( "Passing one argument" )  
function(10)  
  
# Now giving two arguments to the function  
print( "Passing two arguments" )  
function(10,30)

# Python code to demonstrate the use of keyword arguments  
  
# Defining a function  
def function( num1, num2 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
  
# Calling function and passing arguments without using keyword  
print( "Without using keyword" )  
function( 50, 30)     
      
# Calling function and passing arguments using keyword  
print( "With using keyword" )  
function( num2 = 50, num1 = 30)  

# Python code to demonstrate the use of default arguments  
  
# Defining a function  
def function( num1, num2 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
  
# Calling function and passing two arguments out of order, we need num1 to be 20 and num2 to be 30  
print( "Passing out of order arguments" )  
function( 30, 20 )     
  
# Calling function and passing only one argument  
print( "Passing only one argument" )  
try:  
    function( 30 )  
except:  
    print( "Function needs two positional arguments" )  

# Python code to demonstrate the use of variable-length arguments  
   
# Defining a function  
def function(*args_list):
    ans = []
    for I in args_list:
        ans.append(I.upper())
    return ans

# passing args argument
object = function("Python", "Function", "Tutorial")
print(object)

# defining function
def function(**kargs_list):
    ans = []
    for key, value in kargs_list.items():
        ans.append([key,value])
    return ans

# passing kwargs argument
object = function(First = "Python", Second = "Functions", Third = "Tutorial")  
print(object)  

# Defining a function  
lambda_ = lambda argument1, argument2: argument1 + argument2;  
  
# Calling the function and passing values  
print( "Value of the function is : ", lambda_( 20, 30 ) )  
print( "Value of the function is : ", lambda_( 40, 50 ) )  