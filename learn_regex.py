# import re
# line = "Learn Python through tutorials on javatpoint"
# match_object = re.match( r'.w* (.w?) (.w*?)', line, re.M|re.I)  

# if match_object:
#     print("match object group : ", match_object.group())
#     print("match object 1 group : ", match_object.group(1))
#     print("match object 2 group : ", match_object.group(2))
# else:
#     print("There isn't any match!!")

# import re  
  
# line = "Learn Python through tutorials on javatpoint";  
  
# search_object = re.search( r' .*t? (.*t?) (.*t?)', line)  
# if search_object:  
#     print("search object group : ", search_object.group())  
#     print("search object group 1 : ", search_object.group(1))  
#     print("search object group 2 : ", search_object.group(2))  
# else:  
#     print("Nothing found!!") 

import re  
  
line = "Learn Python through tutorials on javatpoint"

match_object = re.match(r'through', line, re.M|re.I)
if match_object:
    print("match object group : ", match_object_group())
else:
    print("There isn't any match")

search_object = re.search( r' .*t? ', line, re.M|re.I)  
if search_object:  
    print("search object group : ", search_object.group())  
else:  
    print("Nothing found!!")  