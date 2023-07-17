# exp=eval(input("enter any matematical expression"))
# print(exp)

# to input list or tuple
'''
l=eval(input("enter the element of list"))
print(l)
print(type(l))


a=input("enter y to start")
print(a)
print(type(a))
print(len(a))
if a[0]=='y':
    print("game start ho gaya hi")
else:
    print("Nahi start hua")'''

a=input("enter y to start")[0]
print(a)
print(type(a))
print(len(a))
if a=='y':
    print("game start ho gaya hi")
else:
    print("Nahi start hua")