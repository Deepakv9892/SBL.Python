a = []
n = int(input('Enter the number of element:'))
for i in range (0, n):
    element = int(input('Enter the elements '))
    a.append(element)
print (a)

print('******************** Inserting Element **************************')
b = int(input('Enter the position in which you want to add the element:'))
e = int(input('Enter the element:'))
a.insert(b,e)
print(a)

print('******************** Append Element **************************')
c = int(input('Enter the Element to be Appended:'))
a.append(c)
print(a)

print('******************** Remove Element **************************')
d = int(input('Enter the Element to be Removed from the list:'))
a.remove(d)
print(a)

print('******************** Replace Element **************************')
e = int(input('Enter the position of element from the list:'))
f = int(input('Enter the element to be Replaced '))
g = int(input("with"))
a.remove(f)
a.insert(e,g)
print(a)

print('******************** Search Element **************************')
h = int(input('Enter the Element to be Searched from the list:'))
print("Element found at index:", a.index(h))
print(a)

print('******************** Size of Linked List Element **************************')
print(len(a))




