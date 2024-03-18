a=[]
n = int(input("Enter No. of Elements: "))
for i in range (0,n):
   element= int(input("Elements in the stack: "))
   a.append(element)
   print(a)
print("********** Inserting element in the Stack *****************")
g=int(input("Enter Element to be added: "))
a.append(g)
print(a)
print("*********** Deleting element in the Stack **************")

print("\nDeleting First Element: ")
a.pop()
print(a)
print("\nDeleting Second Element: ")
a.pop()
print(a)
print("\nDeleting Third Element: ")
a.pop()
print(a)
print("\nlength of the Stack: ",len(a))
len(a)
print("\n********** Check if Stack is empty or not *********")
if (len == 0):
   print("stack is empty\n")
else:
   print("Stack is Full\n")

print("************ Search for the element ******************")
s=int(input("enter element to be searched: "))
print("Element found at index:", a.index(s))
