thisList = ['apple', 'banana', 'cherry']
print(len(thisList))
print(type(thisList))
newList = list(('faith', 'john', 'jane'))
print(newList)
print(newList[2])
print(newList[-2])
oldList = list(('mango', 'orange', 'pineapple', 'grapes', 'kiwi', 'melon', 'cherry'))
print(oldList[2:5])
print(oldList[:4])
print(oldList[3:])
print(oldList[-3:-1])
myList = ['apple', 'mango', 'kiwi', 'melon']
if 'apple' in myList:
    print("yes, 'apple' is present in the list")
myList[0] = 'orange'
print(myList)
myList[1:2] = ['banana', 'cherry']
print(myList)
myList.insert(1, 'coffee')
print(myList)
myList.append('grapes')
print(myList)
tropical = ['papaya', 'passion', 'guava']
myList.extend(tropical)
print(myList)
tuple = ('apple', 'banana', 'cherry')
tropical.extend(tuple)
print(tropical)
myList.remove('orange')
print(myList)
myList.pop(1)
print(myList)
myList.pop()
print(myList)
del myList[0]
print(myList)
del myList[1:4]
print(myList)
for x in myList:
    print(x)
    for i in range(len(myList)):
        print(myList[i])
hisList = ['toyota', 'mazda', 'audi']
i = 0
while i < len(hisList):
    print(hisList[i])
    i = i + 1
    #list comprehension
fruits = ['apple', 'banana', 'cherry']
newList = []
for x in fruits:
    if 'a' in x:
        newList.append(x)
    print(newList)
newList.sort()
print(newList)
theseList = ['banana', 'mango', 'cucumber', 'pineapple', 'kiwi']
theseList.sort(reverse = True)
print(theseList)
thoseList = theseList.copy()
print(thoseList)


