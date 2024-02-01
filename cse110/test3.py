
#smallest = 1
#t = [2,4,5,7,7,100,8,9]

#for i in t:
#    if i > smallest:
#        smallest = i
#print(smallest)
#y = 3


items = []
item = ""

while item.lower() !=  "quit":
    item = input("Enter the items of the shopping list (type: quit to finish) ")
    if item.lower() !="quit":
        items.append(item)
        
    else:
        print("The shopping list is:\n")
        for i in items:
            print(i)
    
print("The shopping list with indexes is:\n")
for j in range(len(items)):
    shopping = items[j]
    print(f"{j+1}. {shopping}")

replace = int(input("Which index of item would you like to change?\n"))
new = input("New item: ")
print()
items[replace - 1] = new


print("The shopping list with indexes is:\n")

for k in range(len(items)):
    an_another_item = items[k]
    print(f"{k + 1} . {items[k]}")












        