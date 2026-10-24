'''
    num1=float(input("enter number1 : "))
    num2=float(input("enter number2 : "))
    print(num1/num2)
    
    c="my name is suzie"
    if "hamid" in c :
        print("name exist!")
    elif "reza" in c :
        print("rza hst")
    elif "Suzie" in c :
        print("suzie sag hast")
    else: 
        print("does not ")
except:
    print("error happened!")
else:
    print("no error found!")
finally:
    print("the end of an era")
    
try:
 print("Welcome to Amir's self made calculator : ")
 num1=float(input("enter number1 : "))
 num2=float(input("enter number2 : "))
 op=input("tell me your operator : ")  
 if "+" in op:
    print(num1+num2)
 elif "-" in op:
    print(num1-num2)
 elif "*" in op:
    print(num1*num2)
 elif "/" in op:
    print(num1/num2)
except:
    print("wrong input!")
p="my name is Hamid anc yours is javad"
if "hamid".upper() in p.upper() :
    print("ex")
else: 
    print(" no")
    
try:
    a=float(input("siskjdiwos"))
    b=float(input("uihf3whd"))
    c=input("huefje")
    if c== "+":
     print(a+b)
    elif c== "-":
     print(a-b)
    elif c== "*":
     print(a*b)
    elif c== "/":
     print(a/b)
    else:
     print("wrong operatopr")
except ZeroDivisionError:
    print("0 error")
except ValueError:
    print("value error"
grfu3ufienwjdxnjweybgfcredbhcrwhbcrbhr
int(len(ar))
#print(ar.find("loop"))
#print("gr" is ar)
print(ar.index("jwey"))
print("grfu3ufienwjdxnjweybgfcredbhcrwhbcrbh" is ar)
a="edrftvghbjuygtfrdetg"
print("gh" in a)
cukfhekrnckkrelkcmlkelkmlkjlkec
print("
cukfhekrnckkrelkcmlkelkmlkjlkec" is ar)
ar="dont you gel sorry for gel please dont gel gel gel gel"
#print(ar.count("gel"))
#print(ar.find("gel"))
#print(ar.replace("gel","kir"))
phrase=(input("please enter your phrase : "))
phrase=phrase.upper()
if "BAD" in phrase:
    print(phrase.replace("BAD","..."))
    print("the text was edited ! ")
else:
    print("no bad word found !")
ar="some news about ...."
print(ar.capitalize())
print(ar.title())
user=input("enter user : ")
password=input("enter pass : ")
user=user.strip()
password=password.strip()
if (user=='admin' or user=='reza') and (password=="123" or password=='456'):
        print("login")
else:
    print("invalid")
username=input("enter username : ")
password=input("enter password : ")
username=username.strip()
password=password.strip()
if (username=="ali" or username=="reza") and (password=='123' or password=='456'):
    print("Login")
else:
    print("wrong stuff")
a=12
b=21
if a==b:
    print("OK")
else:
 print("NO")

print("ok") if a==b else print("no")
print("yes") if 3==3 else print("no")
a=12
b=21
print("=") if a==b else print("a bigga") if a>b else print("b bigga")
a=12
b=21
if a==b:
    print("=")
else:
    if a>b:
        print("a big")
    else:
     print("B big")
print("=") if a==b else print("a bigga") if a>b else print("b bigga")
data=[12,15,17,'reza','ali']
#print(data.count(333))
print(data.index(17))
data.append("333")
data.insert(2,33)
data=[12,15,17,12]
i=0
for x in data:
    if x==12:
        del data[i]
    i=i+1
print(data)
grades = [12, 18, 15, 20, 12, 17, 20]
grades.append(19)
grades.insert(2,10)
grades.remove(12)
print(grades)
if 20 in grades:
    print("20 exits!")
for x in grades:
    print(x)
p=0
for y in grades:
    if y==12:
        print(p)
    p=p+1
classes = [
    [12, 18, 15],
    [20, 17, 14],
    [10, 19, 16]
]
print(classes[2][1])
'''