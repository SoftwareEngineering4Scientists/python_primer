my_list = [1, 2, 3, 4]

prod = 1
for elem in my_list:
    print(prod)
    e_squared = elem ** 2
    prod *= e_squared
    
print("Product of the squares of all elements in my_list:", prod)
