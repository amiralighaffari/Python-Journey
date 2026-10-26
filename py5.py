'''
lst=[1,2,3,-2,-8,5,3,2]
test=test+lst
test.extend(lst)
print(lst[1:4])
[print(x) for x in lst if x%2==0]
a=[1,2,6,-1,10,0]
b=["A","a","z","D"]
b=a.copy()
a.append("test")
print(b)
b=b+a
a.reverse()
a.sort(reverse=True)
print(a)
b.sort(reverse=True)
print(b)
d=[-1,2,5,-2,0,1]
x=[item for item in d if item>=0]
print(len(x))
y=[item for item in d if item<0]
print(len(y))
a=[1,2]
d=(-1,2,5,-2,0,1)
c=list[d]
b=tuple(a)
print(c)
print(b)
d=(12,)
b=list(d)
b.append("test")
c=tuple(b)
print(c)
'''
t=(12,16,19)
(v,*n)=t
print(n)