# .split() breaks a string at specified character into a list of strings

my_string = "Boulder,CO,80304,106392"
my_split_string = my_string.split(",")
print(my_split_string)


# .strip() will remove leading or trailing whitespace

white_str = "   Boulder,CO,80304,106392\n"
strip_split_str = white_str.split(",").strip()
print(strip_split_str)
