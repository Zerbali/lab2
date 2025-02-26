a=int(input("a="))
b=int(input("b="))
x=1
i=0
j=0
k=0
while x<=2:
    if a==x:
        z=7*a**2-8*x
        i=i+1
    elif x>a:
        z=3*b+7*a*x
        j=j+1
    else:
        z=9*b-14*a
        k=k+1
    x=x+0.1
print(z)
print(i,j,k)  
