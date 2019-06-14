# -*- coding: utf-8 -*-

my_dict = {"a":1, "b":2}
print(my_dict)
print("Append a key value pair")
my_dict["c"] = 3
print(my_dict)

print("\nIs a in Dict?", "a" in my_dict)
print("\nIs f in Dict?", "f" in my_dict)

print("\nPopping an item from ", my_dict)
my_dict.pop("c")
print("After popping", my_dict)

my_dict["c"] = 3
print("\nUsing popitem on ", my_dict)
my_dict.popitem()
print("After popping", my_dict)

trainings = {"course1":{"title":"Python Training Course for Beginners", 
                        "location":"Frankfurt", 
                        "trainer":"Steve G. Snake"},
             "course2":{"title":"Intermediate Python Training",
                        "location":"Berlin",
                        "trainer":"Ella M. Charming"},
             "course3":{"title":"Python Training",
                        "location":"München",
                        "trainer":"Monica A. Snowdon"}
             }

trainings2 = trainings.copy()

trainings["course2"] = {"title":"Perl Seminar for Beginners",
                         "location":"Ulm",
                         "trainer":"James D. Morgan"}
print(trainings2["course2"])

# Merging Dictionaries
knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
print("Dict1 = ", knowledge)
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
print("Dict2 = ", knowledge2)
print("Merging the dictionaries")
knowledge.update(knowledge2)
print("After merge ", knowledge)

# Iterating over keys and values of Dictionaries
d = {"a":123, "b":34, "c":304, "d":99}
print("The dictionary value is ", d)
for key in d:
   print(key)
for value in d.values():
   print(value)

# Lists from dictionaries
w = {"house":"Haus", "cat":"", "red":"rot"}
print("The dictionary is ", w)
items_view = w.items()
items = list(items_view)
print("The list of items is ", items)
keys_view = w.keys()
keys = list(keys_view)
print("The list of keys is ",keys)
values_view = w.values()
values = list(values_view)
print("The list of values ",values)

# Dictionaries from lists
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
print("Two lists are ", dishes, countries)
country_specialities_iterator = zip(countries, dishes)
country_specialities = list(country_specialities_iterator)
country_specialities_dict = dict(country_specialities)
print("Dictionary derived from the lists is ", country_specialities_dict)
