mutable_collection = ['Tim', 10, [4, 5]]
immutable_collection = ('Tim', 10, [4, 5])

# Reading from data types are essentially the same:
print(mutable_collection[2])    # [4, 5]
print(immutable_collection[2])  # [4, 5]

# Let's change the 2nd value from 10 to 15
mutable_collection[1] = 15

# This fails with the tuple ( tuple is not muttable)
immutable_collection[1] = 15

#change the list with append a number
immutable_collection[2].append(6)
print(immutable_collection[2])

#change to default
immutable_collection[2] = [4,5]