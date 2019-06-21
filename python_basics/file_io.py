# Appending lines to a file
fh = open("sample.txt", "a")
fh.write("To write or not to write\nthat is the question!\n")
fh.close()

# Read all lines of a file as a list
poem = open("sample.txt").readlines()
print(poem)

# Read all lines of a file
poem = open("sample.txt").read()
print(poem)
