people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"]
so_far = 123452345
youngest = ""
# split into different parts
for f in people:
    parts = f.split(" ")
    int_part = int(parts[1])
    if int_part < so_far:
        so_far = int_part
        youngest = parts[0]
print(f"{youngest} - {so_far}")