import sys
import random
print("Hello, World!")
print(sys.version)

if 5 > 2:
    print("5 is greater than 2")

x = 5
y = "hello world"
print(x)
print(y)

#This is a comment!
""" 
this 
is 
a 
multiline comment
"""

a = "5"
b = int(a)
print(b)
b = float(a)
print(b)
print(type(a))

x,y,z = "orange","banana","apple"
print(x,y,z)

x=y=z = "orange"
print(x,y,z)

fruits = ["banana","banana","banana"]
x,y,z = fruits
print(x,y,z)

x="python"
y ="is"
z="awesome"
print(x,y,z)

x = "awesome"

def func():
    print("Python is",x)
func()

x="cool"

def func():
    x = "awesome"
    print(x)
func()
print(x)
x = "cool"
def func():
    global x
    x = "awesome"
    print(x)
func()
x = "cool"
print(x)

x1="Hello World"
x2=20
x3=20.5
x4=1j
x5=["a","b","c"]
x6=("a","b","c")
x7=range(6)
x8={"name":"Jack", "age":36}
x9={"a","b","c"}
x10=frozenset({"a","b","c"})
x11=True
x12=b"Hello"
x13=bytearray(5)
x14=memoryview(bytes(5))
x15=None

print(random.randrange(1,10))
print(random.random())
print(random.randint(1,10))

a = "Hello World"
print(a[1])

for x in "apple":
    print(x)

a = "Hello World"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

a = "Hello World"
print(a[2:5:2])
print(a[:2])
print(a[5:])

a = "Hello World"
print(a.upper())
print(a.find("l"))
print(a.split("l"))
a = "hello"
b="world"
print(a+b)

age=36
txt = f"My name is John, and I am {age}"
print(txt)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)

fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)

x = 200
print(isinstance(x, int))

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for x in fruits:
   if "a" in x:
      newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)
newlist=[x.upper() for x in fruits]
print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)