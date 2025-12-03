with open("for_loops.py", "r") as f:
    contents = f.read()


print(contents)


# with open("does_not_exist.txt", "w") as f:
#     f.write("""This is a new line added using Python.
# This is the 2nd line.
# And this is the 3rd line.
# """)
    
# with open("new_file.txt", "a") as f:
#     f.write("This line was appended")

# with - context manager


# f = open("does_not_exist.txt", "r")

# contents = f.read()

# print(contents)

# f.close()

# FILE_NAME = "nonexistent_file.py"
# try:
#     with open(FILE_NAME, "r") as f:
#         contents = f.read()
# except FileNotFoundError:
#     with open(FILE_NAME, "w") as f:
#         f.write("")
# else:
#     print(contents)

# FILE_NAME = "qwerty.py"

# contents = None

# try:
#     f = open(FILE_NAME, "r")
#     contents = f.read()
# except FileNotFoundError:
#     print("File not found")
# else:
#     if contents is not None:
#         print("this will not run")
#         f.close()



# with open("for_loops.py", "r") as f:
#     contents = f.readlines()


# for line in contents:
#     print(line)
#     print()
#     print()
#     print()


# with open("nonexistent_file.py", "r") as f:
#     lines = f.readlines()

# print(lines)


# with open("nonexistent_file.py", "r") as f:
#     line = f.readline()
#     print(line)
#     line = f.readline()
#     print(line)
#     line = f.readline()
#     print(line)
#     line = f.readline()
#     print(line)


import os

