s1="hello"
s2="welcome to home"
s3="""i went to watch the movie
inside a maal, where a found my ex with someone-else"""

name="abhishek verma"
print(s1)
print(s2)
print(s3)
print(name,"goel",sep='-')

for ch in name:
    print(ch[0],end='-')
print()

print(name[2])
print(name[-2])

a=[]
a=[1,2,3]
print(a)
    
student_record=[322343,"abhishek verma","bca",59.78]
print(student_record)
    
student_profile=["abhi","bca",[20,30,40]]
print(*student_profile)
count=0

for items in student_profile:
    if isinstance(items, list):
        for x in items:
            print("  ",x)
        else:       
              print(items)
              
              
              