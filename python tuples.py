thistuple = ('apple', 'banana', 'cherry')
print(thistuple)
thistuple = ('apple',)
print(type(thistuple))
thistuple = ()
print(type(thistuple))
thistuple = tuple(('apple', 'banana',))
print(thistuple)
print(thistuple[0])
print(thistuple[-1])
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[2:5])
print(thistuple[:-3])
if "apple" in thistuple:
   print('Yes, "apple" is in the fruits tuple')
x = ('apple', 'banana', 'cherry')
y = list(x)
y[2] = 'orange'
x = tuple(y)
print(x)
y.append('kiwi')
x = tuple(y)
print(x)
z = ('faith', 'hope', 'love')
x += z
print(x)
m = list(z)
m.remove('hope')
z = tuple(m)
print(z)
fruits = ('apple', 'banana', 'kiwi', 'cherry', 'orange')
(blueberry, *banana, tropical) = fruits
print(blueberry)
print(banana)
print(tropical)
for x in fruits:
   print(x)
y = list(fruits)
for x in ('banana', 'kiwi', 'cherry'):
   y.remove(x)
   fruits = tuple(y)
   print(fruits)
for i in range(len(fruits)):
   print(fruits[i])
y = list(fruits)
y.append('kiwi')
fruits = tuple(y)
print(fruits)
i = 0
while i < len(fruits):
   print(fruits[i])
   i = i + 1
myTuple = fruits * 2
print(myTuple)
cities = ('newyork', 'losangeles')
fruitcity = fruits + cities
print(fruitcity)



