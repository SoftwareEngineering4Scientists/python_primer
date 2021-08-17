print("The range function:", range(1, 5))

# for runs the code block N times, defined by the range(start, stop)
total = 0
for i in range(1, 5):
    print(total)
    total += i

print("Total sum using for-loop:", total)


# while tests whether i is less than 5 each time it runs the code block
total = 0
i = 1
while i < 5:
    total += i
    i += 1

print("Total sum using while-loop:", total)
