lst1 = ["a", "b", ["ab", "ba"]]
lst2 = lst1[:]

print("lst1 = {} lst2 = {}".format(lst1, lst2))
print("Shallow copy done.\nChanging the sublist of lst2")
lst2[2][1] = "d"
print("lst1 = {} lst2 = {}".format(lst1, lst2))

from copy import deepcopy
lst1 = ["a", "b", ["ab", "ba"]]
lst2 = deepcopy(lst1)
print("Deepcopy copy done.\nChanging the sublist of lst2")
lst2[2][1] = "d"
print("lst1 = {} lst2 = {}".format(lst1, lst2))
