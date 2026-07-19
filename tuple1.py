t1=()
print(t1)
t2=tuple() #constructor
print(t2)
t3=(10,12,45,0)
print(t3[2])
print(type(3))

t4=("BCA",36,35,True )
print(t4[-2])

#Slicing in tuples
#tuple[start:stop:step]

t5=(10,20,30,40,50,60)
print(t5[:])
print(t5[2:3])
print(t5[:5])
print(t5[-1:-6])
print(t5[::2])

#count
#index
print(t5.count(30))
print(t5.index(30))

print("*"*45)
print(len(t5))
print(max(t5))
print(min(t5))
print(sum(t5))
print(sorted(t5))
print(20 in t5)
print(20 not in t5)
