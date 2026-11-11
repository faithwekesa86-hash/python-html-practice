thisSet = {'apple', 'banana', 'apple', 'cherry'}
print(thisSet)
myset = {'apple', 'banana', 'true', 1, 3.4}
print(myset)
print(len(myset))
print(type(myset))
for x in myset:
    print(x)
print('banana' in myset)
print('orange' in myset)
print('orange' not in myset)  
myset.add('kiwi')
print(myset) 
tropical = {'papaya',}
myset.update(tropical)
print(myset)
myset.remove('papaya')
print(myset)
myset.discard('banana')
print(myset)
#pop() method removes a random item
myset.pop()
print(myset)
#clear() empties the set
#del() deletes the set completely
for x in myset:
    print(x)
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
#union() returns a new set with all the items from both sets
set3 = set1.union(set2)
print(set3)
set3 = set1 | set2
print(set3)
set5 = {'apple',}
set6 = {'Faith',}
set7 = set1.union(set5, set6)
print(set7)
#union() allows you to join set wit other data types
#update() inserts all items from anoter set
#intersection() returns a new set with duplicates without modifying original sets
set10 = {'money', 'faith',}
set11 = {'faith', 'hope'}
set12 = set10.intersection(set11)
print(set12)
#you can use & operstor as well
set12 = set10 & set11
print(set12)
#intersection_update() keeps duplicates but will change the original set instead
set10.intersection_update(set11)
print(set10)
fruits1 = {"mango", "orange", "banana", "apple"}
fruits2 = {"banana", "apple", "grapes", "watermelon"}
fruits3 = fruits1.intersection(fruits2)
print(fruits3)
print(fruits1)
print(fruits2)
fruits1.intersection_update(fruits2)
print(fruits1)
print(fruits2)
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)
#difference() returns a new set with items that are in first set but not in other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
#you can use -operator instead of difference you will gwt same results
#difference_update() keeps items i the first set that are not in other set but will change original set
set1.difference_update(set2)
print(set1)
print(set2)
#symmetric_difference() keeps elements that are not present in both sets
set3 = set1.symmetric_difference(set2)
print(set3)
#you can use ^ operator instead of assymetrical 
#symmetric_difference_update() keeps elemets that are not present in both sets but change the original set instead of returning a new set
#frozenset- elements cannot be added or removed 
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
