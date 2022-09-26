'''
name = "Athithya"
age = 25
office = "L&T"

print("My name is",name,".I am",age,"years old and work at",office)
print(f"My name is {name}.I am {age} years old and work at {office}")
print("My name is {}.I am {} years old and work at {}".format(name,age,office))
print("My name is {1}. I am {2} years old and work at {0}".format(office,name,age))
print("My name is {1}. I am {2} years old and work at {0}".format(office,name,age))
print("My name is {n}. I am {a} years old and work at {o}".format(o=office, n=name, a=age))
'''
username = input("Enter username: ")
print(f"username is {username}")
print(type(username))

age=int(input("Enter your age: "))
print(f"age is {age}")
print(type(age))

age=age+10
print(f"age is {age}")