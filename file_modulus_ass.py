# ----------------------ASSIGNMENT---------------------

# # -------------------------------------------------
# # EXERCISE 1:
# # Open the file "sample.txt" in read mode.
# # Print out the entire file contents.

file = "sample.txt"
try:
    with open(file, "r") as f:
        details = f.read()
except FileNotFoundError:
    with open(file, "w") as f:
        f.write("""This file is a sample. The contents of this file is subject to review.
Once upon a time, in a quiet village,
there lived a curious child who loved to learn.
Every day, they discovered something new,
and shared it with the world.
""")
else:
    print(details)



# # ----------------------------------------------------------

# # EXERCISE 2:
# # Open "sample.txt" again, but this time print only the first line.

with open(file, "r") as f:
    file_line = f.readline()
    print(file_line)
    file_line = f.readline()
    print(file_line)

for line in file_line:
    print(line)


    
    

# # ----------------------------------------------------------

# # EXERCISE 3:
# # Read all the lines in "sample.txt" into a list called lines.
# # Then print the last line in the file.

lines = []
with open(file, "r") as f:
    lines = f.readlines()
print(lines[-1])
    
# # ----------------------------------------------------------

# # EXERCISE 4:
# # Create a new file called "notes.txt" using write mode.
# # Write three lines into it (each ending with a newline):
# #   - "Python file test"
# #   - "We are learning to write files"
# #   - "This is the third line"


with open("notes.txt", "w") as f:
    f.write("""
Python file test\n
We are learning to write files \n
This is the third line \n""")

# # ----------------------------------------------------------

# # EXERCISE 5:
# # Open "notes.txt" again in append mode.
# # Add one more line that says:
# #   "This line was appended."

with open("notes.txt", "a") as f:
    f.write("This line was appended")

# # ----------------------------------------------------------

# # EXERCISE 6:
# # Open "notes.txt" again in read mode.
# # Print all its contents to confirm the new line was appended.

with open("notes.txt", "r") as f:
    contents = f.read()

print(contents)

# # ----------------------------------------------------------

# # EXERCISE 7:
# # Read all lines from "sample.txt".
# # Using a for loop with enumerate, print each line like this:
# #   Line 1: <the line>
# #   Line 2: <the line>
# # Strip out the newline characters when printing.
    
with open(file, "r") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    print(f"Line {idx}: {line}")

# # ----------------------------------------------------------

# # EXERCISE 8:
# # Do the same as Exercise 7, but using a while loop instead of for loop.

with open(file, "r") as f:
    lines = f.readlines()

i = 1
while i < len(lines):
    print(f"Line {i}: {lines[i]}")
    i += 1

    
# # ----------------------------------------------------------

# # EXERCISE 9:
# # Open "notes.txt" in read mode.
# # Count how many lines are in the file and print:
# #   "notes.txt has X lines"

with open("notes.txt", "r") as f:
    lines = f.readlines()

print(f"notes.txt has {len(lines)} lines")
# ----------------------ASSIGNMENT---------------------


# import string