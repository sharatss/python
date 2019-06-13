lst = ["string", 10, 10.0]
print("This is our list: ", lst)
print("First element of the list is: ", lst[0])

tpl = ("string", 10, 10.0)
print("\nThis is our tuple: ", tpl)
print("First element of the tuple is: ", tpl[0])

string = "Python is cool!"
print("\nThe declared string is: ", string)
print("The first six characters of the string are: ", string[0:6])
print("Starting from fifth character: ", string[5:])
print("String without last five characters: ", string[:-5])
print("Print every second(alternate) character: ", string[::2])
print("Print every second(alternate) character in from the first six characters: ", string[0:6:2])

print("\nLength of the list = ", len(lst))
print("Length of the tuple = ", len(tpl))
print("Length of the string = ", len(string))

print("\nConacting two strings")
str_one = "Hello"
str_two = "World"
full_word = str_one + " " + str_two
print("First string = {}\n, Second string = {}\n, Concated string = {}".format(str_one, str_two, full_word))


print("\nConacting two lists")
lst_one = ["L1 element1", "L1_element2"]
lst_two = ["L2 element1", "L2_element2"]
cat_lst = lst_one + lst_two
print("First list = {}\n, Second list = {}\n, Concated list = {}".format(lst_one, lst_two, cat_lst))

print("\nChecking if element in list")
print("Is L1 element1 in the new list? ", "L1 element1" in cat_lst)
print("Is L3 element1 in the new list? ", "L3 element1" in cat_lst)
