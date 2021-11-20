d= {'name': 'danile', 'age': 100}

print(d.keys()) #result: all keys ['age', 'name']
print(d.values()) #result: allvalues [100, 'daniele']
print(d.items()) #results: [('age':'100'), ('name': 'danile')] convert to list

#update dict value:
d['name'] = "mike"
print(d) #result: {'age': 100, 'name': 'mike'}
print(d.has_key('name')) #results: True
print(d.has_key('action')) #results: True

if d.has_key('action'):
    d['action'] = "exist and replace"
else: d['action'] = "not exist update"
print(d) #result: {'action': 'not exist update', 'age': 100, 'name': 'mike'}

items = d.items()
print(items[0]) #results: ('age':'100') , tuple
print(type(items[0])) #results: tuple


#challege : count number of chars in string
s = "hello world aaabcw"
dict = {}
for i in s:
    if dict.has_key(i):
        dict[i] += 1
    else: dict[i] = 1
print(dict) #result: {'a': 3, ' ': 2, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 2}
print(dict['a']) #result: 3
