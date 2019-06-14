# Pop and Append
lst = ["a", "b", "c"]
print("The element popped from the list {} is {}".format(lst, lst.pop(2)))
print("The resulting list is ", lst)

print("\nAppending d to the list")
lst.append("d")
print("The list now is ", lst)

# Extend
lst2 = ["e", "f"] # can even be a str or tup
print("Extending {} with {}".format(lst, lst2))
lst.extend(lst2)
print("Extended list is ", lst)

# Remove
print("Removing f from ", lst)
lst.remove("f")
print("After removing ", lst)

# Index
print("The position of b in {} is {}".format(lst, lst.index("b")))

# Insert
print("Inserting x at third position into the list", lst)
lst.insert(3,"x")
print("After insertion", lst)
