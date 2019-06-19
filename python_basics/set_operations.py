# Add element
colours = {"red","green"}
print("Adding yellow to the set", colours)
colours.add("yellow")
print("After adding ", colours)

# Clear the set
cities = {"Stuttgart", "Konstanz", "Freiburg"}
print("Clear the set ", cities)
print("After clearing ", cities)

# Copy the set
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
print("Copy the set more_cities= ", more_cities)
cities_backup = more_cities.copy()
print("The new set cities_backup = ", cities_backup)

# Difference between sets
x = {"a","b","c","d","e"}
y = {"b","c"}
print("The difference betwen {} and {} is {}".format(x, y, x.difference(y)))

# Difference update
x = {"a","b","c","d","e"}
y = {"b","c"}
print("The value of x and y before difference_update is ", x, y)
print("Value of x after difference_update ", x.difference_update(y))

# Discard an element
x = {"a","b","c","d","e"}
print("Discard element a from the set ", x)
x.discard("a")
print("After discard ", x)

# Union and intersection
x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
print("The union of {} and {} is {}".format(x, y, x|y))
print("The intersection of {} and {} is {}".format(x, y, x&y))

# Disjoint, subset and superset
x = {"a","b","c"}
y = {"c","d","e"}
print("Are {} and {} disjoint sets?".format(x, y, x.isdisjoint(y)))
y = {"d","e","f"}
print("Are {} and {} disjoint sets?".format(x, y, x.isdisjoint(y)))
x = {"a","b","c","d","e"}
y = {"c","d"}
print("Is {} a subset of {}?".format(x, y, x.issubset(y)))
print("Is {} a subset of {}?".format(y, x, y.issubset(x)))
print("Is {} a superset of {}?".format(x, y, x.issuperset(y)))
print("Pop an element from ",x)
x.pop()
print("After pop", x)
