my_list = [1, 2.0, "three", 4]
my_tup = (1, 2.0, "three", 4)
my_set = {1, 2.0, "three", 4}
my_str = "1, 2.0, three, 4"

# Subscripting ordered datatypes
print(my_list[0])      # indexing
print(my_tup[0:2])     # slicing
print(my_str[-8:])     # negative index and slice

# Adding elements
my_list.append(5.0)
print("my_list with new element:", my_list)

# Uniqueness
my_set.add(2.0)
print("my_set didn't change:", my_set)
