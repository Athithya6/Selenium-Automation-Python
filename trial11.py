str1 = "Karnataka"
str2 = "Tour 2021"
str3 = 6
str4 = "Karn"
str5 = "athithya.narayan@gmail.com"
str6 = "         Goodfellas   "

print(str1[2])  # printing a character from a string
print(str1[2:7])  # printing a substring of a string
print(str1 + str2)  # concatenating two strings
print("{} {}".format(str1, str3))  # concatenating a string and an integer
print(str4 in str1)  # substring check in main string
t = str5.split(".")  # t is a list containing the parts of str5 separated by a dot
print(t)
print(str6.strip())  # stripping both spaces
print(str6.lstrip())  # stripping left space
print(str6.rstrip())  # stripping right space
