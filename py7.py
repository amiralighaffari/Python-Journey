'''
a=12
b=5
c=80
if c>b and c>a :
    print("c the biggest")
elif b>c and b>a :
    print("b the biggest")
else:
    print("a the biggest")
def max ():
    if (a>b>c):
        print("big")
max()
def max(*a):
    sum=0
    for x in a:
        sum=sum+x
    print(sum)
max(12,45,232,121,3434,232)
def max(*a):
    print(sum(a))
max(12,45,232,121,3434,232)
def max(*a):
    sum=0
    for x in a:
        sum=sum+x
    print(sum)
    
    
strlist=input("numbers w , ")
mylist=strlist.split(",")
intlist=[int(x) for x in mylist]
tp=tuple(intlist)
max(*tp)
def max(**a):
    for x,y in a.items():
        print(x,y)
max(name="jack",age=21)
def max(a,b):
    if a>b:
        return a
    else:
        return b
num=max(12,19)
print("maximum is",num)
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def max(a,b):
    if a>b:
        return a
    else:
        return b

largest=max(a,max(b,c))
print(largest)