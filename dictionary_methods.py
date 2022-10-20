myDict = {
    'name': 'Eddy',
    'age': 26,
    'address':'London',
    'education':'master'
}

#Copies dictionary into new variable
myDictTwo = myDict.copy()
myDict['name'] = 'Edy'

newDict = {}.fromkeys([1,2,3], 0)
print(newDict)

print(myDict.get('name'))
print(myDict.items())
print(myDict.keys())
print(myDict.setdefault('name1', 'added'))
print(myDict)
print(myDict.values())
print(myDict.update({}))