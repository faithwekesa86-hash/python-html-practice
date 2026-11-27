thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white"]
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
thisdict = dict(name = "faith", age = 19, course = "BBIT")
print(thisdict)
print(thisdict['name'])
x = thisdict['name']
print(thisdict.get('name'))
print(thisdict.keys())
thisdict['hobby'] = 'singing'
print(thisdict)
print(thisdict.values())
thisdict['name'] = 'wekesa'
print(thisdict)
print(thisdict.values())
x = thisdict.items()
print(x)
thisdict['age'] = 20
print(x)
print(thisdict)
newdict = {
    'color': 'red',
    'hobby': 'singing',
    'country': 'kenya'
}
print(newdict)
if 'country' in newdict:
    print('yes, "country" is one of the keys in newdict')
newdict['color'] = 'blue'
print(newdict)
newdict.update({'hobby': 'dancing'})
print(newdict)
newdict['county'] = 'nairobi'
print(newdict)
newdict.update({'bestfriend': 'none'})
print(newdict)
newdict.pop('bestfriend')
print(newdict)
newdict.popitem()
print(newdict)
for x in newdict:
    print(x)
    for x in newdict.values():
        print(x)
for x in newdict.keys():
    print(newdict)
for x, y in newdict.items():
    print(x, y)   
mydict = newdict.copy()
print(mydict) 
mydict = dict(newdict) 
print(mydict)  
myfamily = {
    'child1' : {
        'name' : 'blake',
        'age' : 3
    },
    'child2': {
        'name' : 'blaire',
        'age' : 5
    },
    'child3' : {
        'name' : 'zawadi',
        'age' : 6
    }
}
print(myfamily)
child1 = {
    'name' : 'blake',
    'age' : 3
}
child2 = {
    'name' : 'blaire',
    'age' : 5
}
child3 = {
    'name' : 'zawadi',
    'age' : 6
}
myfmily = {
    'child1' : child1,
    'child2' : child2,
    'child3' : child3
}
print(myfamily['child1']['name'])
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y]) 
          
        