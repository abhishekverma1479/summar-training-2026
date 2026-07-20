numbers=[x for x in range(4)]
print(numbers)

numbers2=[x*x for x in range(4)]

print(numbers2)

even=[x for x in range(10) if x%2==0]
print(even)

odd=[x for x in range(10) if x%2!=0]
print(odd)

words=["gonda","babhnan","basti"]

upperwords=[words.upper() for words in words]
print(upperwords)

lengths=[len(words) for words in words]
print(lengths)


longwords=[len(words) for words in words if len(words)>6]
print(longwords)
