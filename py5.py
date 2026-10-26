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
t=(12,16,19)
(v,*n)=t
print(n)
numbers = [4, -3, 7, 0, -8, 2, 5, -1]
positives=[x for x in numbers if x>0]
negatives=[x for x in numbers if x<0]
zeros=[x for x in numbers if x==0]
print(len(positives))
print(len(negatives))
print(len(zeros))
numbers = [10, 20, 30, 40, 50, 60, 70]
a=numbers[1:4]
b=numbers[4:]
c=numbers[:3]
numbers=[8, 3, 1, 9, 4, 2]
koochak=sorted(numbers)
print(koochak)
bozorg=sorted(numbers, reverse=True )
print(bozorg)
copi=numbers.copy()
copi.sort(reverse=True)
print(copi)
t = (10, 20, 30, 40, 50)
(a,*b,c)=t
print(a)
print(b)
print(c)
'''