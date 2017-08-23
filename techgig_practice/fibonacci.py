#Program to get the fibonacci series of N number


n=input("Enter the N number")
a=0
b=1
for i in range(3,n+1):
    print a
    a,b=b,a+b
