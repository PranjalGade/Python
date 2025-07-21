n=int(input("Enter a number : "))
if n<=0:
    print("Enter positive number")
else:
    print(f"The first {n} natural numbers are :")
    for i in range(1,n+1) :
        print(i)         