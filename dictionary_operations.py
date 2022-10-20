#creation
myDict = dict()
secondDict = { }
engToSpanish = {
    "one": "uno",
    "two": "dos",
    "three": "tres"
}
# print(engToSpanish["one"]) # O(1) complexity

# #insert/update
# myDict = {
#     'name': 'Eddy',
#     'age': 26
# }
# myDict['age'] = 27 #O(1) space and time complexity 
# myDict['address'] = "120 Helmholdt Street" #O(1) time complexity; amortized O(1) space complexity (could be O(n) if dictionary size limit reached)
# print(myDict)

# #traversal
# def traverseDict(dict):
#     for key in dict:              #O(n) time complexity, O(1) space complexity
#         print(key, dict[key])

# traverseDict(myDict)

# #search for element
# def searchDict(dict, value):
#     for key in dict:                   #O(n) time complexity, O(1) space complexity
#         if dict[key] == value:
#             return key, value
#     return "The value does not exist."

# print(searchDict(myDict, 27))

# #delete/remove element
# # Time complexity: amortized O(n)
# #Space complexity: O(1)
# print(myDict.pop('name'))
# print(myDict)
# print(myDict.popitem())
# print(myDict.clear())

# myDict = {
#     'name': 'Eddy',
#     'age': 26
# }

# del myDict['age']
# print (myDict)

if 'uno' in engToSpanish.values(): #O(n) time complexity
    print(True)

print(all(myDict))
myDict['falsey'] = False
print(myDict)
print(all(myDict)) 
