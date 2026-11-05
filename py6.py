'''
lst=[1,1,3,4]
tp=(1,1,3,4)
print(lst)
print(tp)
st={True,1,1,5,'a',6,"bro"}
st.add("test")
st.remove(5)
st.discard("a")
#st.clear()
#del st
#print(len(st))
st1={1,2,3}
st2={2,3,4}
st1.update(st2)
print(st1)
lst=[4,1,5,5]
st0=set(lst)
print(st0)
st1={1,2,3}
st2={2,3,4}
st3=st1.union(st2)
print(st3)
st4=st1.intersection(st2)
print(st4)
st5=st1.difference(st2)
print(st5)
st1={1,2,3}
for x in st1:
    print(x)
st1={1,6,'a',12}
st2={3,9,1}
if st1&st2:
    print("yes")
else:
    print('no')
st1={1,6,"a",12}
st2={3,9,10}
st3={"a","v",10}
st4=st1|st2|st3
print(st4)
dic={'name':'Jack',"Family":"Black","Age":22}
dic["point"]=25
dic.pop("name")
dic.popitem()
del dic['Age']
dic.clear()
print(dic)
a=[{"name":"Kylie" , "phone": 2312345678},{"name":"Kyle" , "phone": 39876543}]
i='---'
for x in a:
    for y,z in x.items():
        if y=="phone":
            x[y]=i
print(a)
lst1=input("enter your numbers : ").split()
lst2=input("enter your numbers : ").split()
st1=set(lst1)
st2=set(lst2)
if st1&st2:
    print(st1&st2)
else:
    print("no common thing")
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for x in numbers:
    for y in x:
        print(y)
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for x in numbers:
    for y in x:
        if y%2==0:
            print(y)
students = [
    {"name": "Alex", "score": 18},
    {"name": "John", "score": 15},
    {"name": "Emma", "score": 20}
]
for x in students:
    print(x["name"],x["score"])
students = [
    {"name": "Alex", "score": 18},
    {"name": "John", "score": 15},
    {"name": "Emma", "score": 20},
    {"name": "Mike", "score": 12}
]
for x in students:
    if x["score"]>15:
      print(x["score"])
students = [
    {"name": "Alex", "score": 18},
    {"name": "John", "score": 15},
    {"name": "Emma", "score": 20},
    {"name": "Mike", "score": 12}
]
for x in students:
    for y,z in x.items():
        if y=="score" and x[y]>=18:
            print(z)
'''