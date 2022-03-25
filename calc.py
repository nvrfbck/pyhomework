# calculator

# first num
a = input("enter a number please: ")
while not a.isdigit():
    a = input("enter a number please: ")
else:
    a = int(a)
    print("oke its", a)

# action
x = input("please choose what action to perform: ")
while (x != "*") and (x != "/") and (x != "+") and (x != "-"):
    x = input("please choose what action to perform: ")
else:
    print("oke its", x)

# second num
b = input("enter a number please: ")
while not b.isdigit():
    b = input("enter a number please: ")
else:
    b = int(b)
    print("oke its", b)
    
# result
if x == "+":
    result = a + b
elif x == "-":
    result = a - b
elif x == "*":
    result = a * b
else:
    result = a / b

print("your result:", result)
