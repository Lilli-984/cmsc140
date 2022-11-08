from pathlib import Path
import random

home_dir = "/Users/citlallisanchez"
home_path = Path(home_dir)
print(home_path)


new_path = home_path / "Documents" / "CMSC140"
print(new_path)

path_to_proj = r"/Users/citlallisanchez/CMSC140"
base_path = Path(path_to_proj)
hwk_path = base_path / "Homework" / "Homework 4"
print(hwk_path)

print(Path.cwd())



#Lists and lists iteration

list_of_ints = []
for i in range(100):
    list_of_ints.append(random.randint(20,89))
print(list_of_ints)

for i in range(len(list_of_ints)):
    print(list_of_ints[i])

print("range iteration")
for idx in range(len(list_of_ints)):
    print(f"Element {idx}: {list_of_ints[idx]}")

print("enumerate iteration:")
for idx, elem in enumerate(lists_of_ints):
    print(f"Element {idx}: {elem}")




list_2 =[]
for i in range(20,90):
    list_2.append(i)
print(list_2)

#while/break