word = "commitment"
A = input("Enter ")
"""for z in word:
    if z.lower() == A.lower():
        print(z.upper(), end = "")
    else:
        print(z.lower(), end = "")"""
print()

for b in word:
    if b.lower() == A.lower():
        print("_", end = "")
    else:
        print(b.lower(), end = "")