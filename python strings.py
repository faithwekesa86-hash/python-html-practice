a = 'hello world'
print(len(a))
txt = 'no one has plans for you'
print('one' in txt)
print('expensive' not in txt)
if 'expensive' not in txt:
    print('no , "expensive" is not present.')
age = 19
txt =f'My name is Faith , I am {age} years old'
print(txt) 
#escape character
txt = 'I love \'love\' so much'  
print(txt) 
txt = 'hi\reveryone'
print(txt)
txt = '\66\56\67\69\68'
print(txt)
x = 9
print(f'the price is {x:.3f} dollars')
print('python'.center(16, "-"))
print("banana".count("a"))
print('hi\tthere'.expandtabs(4))
print('my name is {}'.format('faith'))
print(' '.join(['i', 'love', 'python']))
table = str.maketrans('abc', '123')
print('abc'.translate(table))
x = 5
x>>=3
print(x)
numbers = [1, 2, 3, 4, 5]
if(count := len(numbers)) > 3:
    print(f"list has {count} elements")
num = 6
x = 'weekend' if num > 5 else 'workday'
print(x)
x = 'fri' if num ==5 else 'sat' if num == 6 else 'sun' if num == 7 else 'weekday'
print(x)
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)
