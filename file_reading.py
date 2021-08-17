file_name = "counties_data.csv"
  
# Reading a file using open/close
file = open(file_name,'r')

for line in file:
    print(line, end='')

file.close()


# Reading file using with/as
print("Now to use the with/as method.")

with open(file_name, 'r') as f:

    for l in f:
        print(l, end='')
