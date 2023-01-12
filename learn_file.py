fileptr = open("file1.txt", "a")

fileptr.write("""
Python has an easy syntax and user-friendly interaction.
""")

fileptr.close()

import os
os.getcwd()

print(os.getcwd())
