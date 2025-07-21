a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd1 number:"))
if a>=b and a>=c:
    print("The greater no is",a)
elif b>=a and b>=c:
    print("The greater no is",b)
else:
    print("The greater no is ",c)

# max function

print(max(a,b,c))