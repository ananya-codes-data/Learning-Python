# Lists and Tuples

# List
# containers to store a set of values of any data type
# unlike strings, lists are mutable i.e., it can be changed

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
# print(friends[0])

# friends[0] = "Grapes"

# print(friends[0])

# lists can be indexed like string
# print(friends[1:4])


# list methods

# in string when we use any method it would result in a new string, we have to print it
# but in list, the list itself gets changed and we don't have to print it

# print(friends)

# friends.append("Ananya")        # add any data at the end of the list

# print(friends)

l1 = [1, 34, 62, 2, 6, 11]

# l1.sort()       # sorting of numerical list in increasing order
# print(l1)

# l1.reverse()
# print(l1)       # reversing the complete list

l1.insert(3, 2210)
print(l1)