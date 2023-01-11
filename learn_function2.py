# def square(num):
#     return num**2

# object_ = square(6)
# print(object_)

# def a_function(string):
#     return len(string)

# print("Length of the string Function is: ", a_function("Functions"))
# print("Length of the string Python is: ", a_function("Python"))

# def square(item_list):
#     squares = []
#     for I in item_list:
#         squares.append(I**2)
#     return squares

# my_list = [17,52,8]
# my_result = square(my_list)
# print("Square of the list are: ", my_result)

# def function(n1, n2):
#     print("Number 1 is: ", n1)
#     print("Number 2 is: ", n2)

# print("Without using keyword")
# function(50,30)

# print("With using keyword")
# function(n2 = 50, n1 = 30)

# def function(n1, n2):
#     print("Number 1 is: ", n1)
#     print("Number 2 is: ", n2)

# function(30,20)

# print("Passing only one argument")

# try:
#     function(30)
# except:
#     print("Function need two postional arguments")

# def function(*args_list):
#     ans = []
#     for I in args_list:
#         ans.append(I.upper())
#     return ans

# object = function('Python','Functions','Tutorial')
# print(object)

# def function(**kargs_list):
#     ans = []
#     for key,value in kargs_list.items():
#         ans.append([key,value])
#     return ans

# object = function(First = "Python", Second = "Functions", Third = "Tutorial")
# print(object)

# lambda_ = lambda arg1, arg2: arg1 + arg2;

# print("Value of the function is: ", lambda_(20,30))
# print("Value of the function is: ", lambda_(40,50))

# string = "Hello World"
# array = bytes(string,'utf-8')
# print(array)

# string = "Python is a programming language"
# arr = bytearray(string, 'utf-8')
# print(arr)

# def calculateAddition(n):
#     return n+n

# numbers = (1,2,3,4)
# result = map(calculateAddition, numbers)
# print(result)

# a = complex(1)
# b = complex(1,2)
# print(a)
# print(b)

# class Student:
#     id = 101
#     name = "Pranshu"
#     email = "pranshu@gmail.com"

#     def getInfo(self):
#         print(self.id, self.name, self.email)

# s = Student()
# s.getInfo()
# delattr(Student,'course')
# s.getInfo()

# result = dict()
# result2 = dict(a=1, b=2)
# print(result)
# print(result2)

# def filterdata(x):
#     if x > 5:
#         return x

# result = filter(filterdata,(1,2,6))
# print(list(result))

# result = hex(1)

# result2 = hex(342)
# print(result)
# print(result2)

# class Student:
#     id = 0
#     name = ""

#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# student = Student(102,"Sohan")
# print(student.id)
# print(student.name)
# setattr(student, 'email')
# print(student.email)

# class Student:
#     id = 101
#     name = "John"
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# student = Student(1010,"John")
# lst = [12,34,5,6,767]

# print(isinstance(student, Student))
# print(isinstance(lst,Student))

# print(list(range(0)))
# print(list(range(4)))
# print(list(range(1,7)))

# class Rectangle:
#     def __init__(rectangleType):
#         print('Rectangle is a ', rectangleType)

# class Square(Rectangle):
#     def __init__(self):
#         Rectangle.__init__('Square')

# print(issubclass(Square, Rectangle))
# print(issubclass(Square, list))
# print(issubclass(Square,(list,Rectangle)))
# print(issubclass(Rectangle,(list,Rectangle)))
