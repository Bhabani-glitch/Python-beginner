#List
a = ["Bhabani", "Bhuyan",10, 0.25]
print(a[1])
print(a[1:])
print(a[::-1])
b=[10,20,"youtube"]
c=a+b
c1=[a,b]
print(c)
print(c1)
b.insert(3,"genda")
print(b)
a.remove(10)
print(a)
b.append(70)
print(b)
b.pop(2)
print(b)
del b[3:]
print(b)
b.extend([20,50,56])
print(b)
d=[10,20,30,50]
print(min(d))
print(sum(d))
d.sort()
print(d)
##Tuple
t=(10,"bhabani",20,23)
t1=[10,"bhabani",20,23]
#t[1]=50 immutable
print(t[-1])
print(len(t))
print(dir(t))
import sys
print(sys.getsizeof(t))
print(sys.getsizeof(t1))
t=tuple("bhabani")
print(t)
t=()
print(t)
t=(1,2,3)
t1=(4,5,6)
t2=(t,t1)
t3=t+t1
print(t2)
print(t3)
t=tuple("bhabani")
print(t)
del t
#print(t)
##Set
a={}
print(a)
a={1,4,7,7,"bhabani"}
print(a)
a=set("bhabani")
print(a)
a.add(11)
a.update([45,25,65])
print(a)
a.remove(11)
a.discard('a')
print(a)
a.pop()
print(a)
a.clear()
print(a)
a={1,5,8,5}
b=a.copy()
print(b)
#Frozen Set
s={1,4,3,5}
s1=frozenset(s)
print(s1)
s.add(14)
print(s)
print(s1)
#frozen set is immutable data type
#Dictionary
d={}
d={1:"bhabani", 2:"bhuyan", 5:30}
print(d)
d1={"bhabani":20, "bhuyan":26,'youtube':"babu"}
print(d1)
d2={1:[1,2,5], 2:'hello'}
print(d2)
d3=dict({4:'hello', 2:52})
print(d3)
d4=dict([(1,'for'),(2,'bhabani')])
print(d4)
#nested dictionary
d5={1:"babu", 2:60, 3:{1:"sankar",6:70}}
print(d5)
d5[4]="key"
print(d5)
d5[3]="changed"
print(d5)
d5['yoyo']=30
print(d5)
print(d5[3])
print(d5.get(3))
del d5['yoyo']
print(d5)
d5={1:"babu", 2:60, 3:{1:"sankar",6:70}}
print(d5[3][6])
del d5[3][6]
print(d5)
d5.pop(2)
print(d5)
d5.popitem()
print(d5)
d5.clear()
print(d5)
d6=d.copy()
print(d6)
print(d6.keys())
print(d6.items())
#string-immutable
#array-mutable