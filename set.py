# empty_set = set()
# my_set = {1, 2, 3, 3, 4, 5}

# print(my_set)

fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits.add("orange")
print(fruits)

fruits.update(["orange", "mango", "grapes"])
print(fruits)
fruits.remove("banana")
print(fruits)

fruits2 = {"apple", "banana2", "cherry2"}

fruits3 = fruits.union(fruits2)
print(fruits3)

fruits4 = fruits | fruits2
print(fruits4)

fruits5 = fruits.intersection(fruits2)
print(fruits5)

fruits6 = fruits & fruits2  # intersection
print(fruits6)

fruits7 = fruits.difference(fruits2)
print(fruits7)

fruits8 = fruits - fruits2
print(fruits8)

fruits9 = fruits.symmetric_difference(fruits2)
print(fruits9)

fruits10 = fruits ^ fruits2
print(fruits10)

# issubset
fruits11 = {"apple", "banana"}
fruits12 = {"apple", "banana", "cherry", "orange", "mango", "grapes"}
print(fruits11.issubset(fruits12))
