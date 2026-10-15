# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
with open("../images/feep.pgm","r") as infile:
    infile.readline()
    dimensions = infile.readline().split()
    width = dimensions[0]
    height = dimensions[1]
    max_gray_value = infile.readline().strip()
print(f"Dimensions: {width} x {height} pixels")
print(f"Max Gray Value: {max_gray_value}")