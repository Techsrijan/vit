a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
# nested if else
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")