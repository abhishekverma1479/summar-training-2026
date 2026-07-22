s = {10,20,30}
print(s)

s.add(100)
print(s)

s.update([50,60,80])
print(s)

s.remove(100)
print(s)

s.discard(120)
x=s.pop()
print("popped element", x)
print(s)

x=s.pop() #remove random
print("remove random",x)


s.clear()#clear all alement
print(s)

s1={32,22,33,44,55}#deep copy
s2=s1
s2.add(300)
print(s1)
print(s2)

s2=s1.copy()#salo copy
s2.add(400)
print(s1)
print(s2)

#built in function
s3={67,78,48,76,65}
print(len(s3))
print(min(s3))
print(max(s3))
print(sum(s3))
s4={False,0,-6}
print(any(s4))
s5={0,3,5}
print(all(s5))

print(s3)

#set operation
#union s1 U s2
s1={1,4,6,5,8,6}
s2={1,4,6,8,90,67}

print(s1.union(s2))

#intersection
print(s1.intersection(s2))

#difference

print(s1.difference(s2))
print(s2.difference(s1))