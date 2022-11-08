from re import template
import matplotlib.pyplot as plt

hello = open("hello.txt", 'r+')


file_contents = hello.read()
file_contents_list = hello.readlines()

print(file_contents_list)

hello.write("\nHeres some new content")

hello.close()
""" 
#f (below) can be any variable. f stands for file
with open("hello.txt", 'a') as f:
    file_content = f.readlines()
print(file_content)


#by default, strip will take off any whte space characters, which includes \n and such
with open("hello.txt", 'a') as f:
    file_content = [i.strip() for i in f.readlines()]
print(file_content)
#these are equivalent
for i, val in enumerate(info):
    info[i]= val.strip() """
""" 
names = open('names.txt', 'a')
names.write("\nLilli Sanchez")
names.close

with open('names.txt', 'r') as f:
    info = [i.strip() for i in f.readlines()]

for i in info:
    print(i)
 """

temps = []
hats = []
with open("hats.txt") as f:
    next(f) #skip first line
    for line in f.readlines():
        line = line.strip()  #strip off the white space
        x, y = line.split(" ") #
        temps.append(int(x))
        hats.append(int(y))
print (temps)
print(hats)

plt.plot(temps, hats)
plt.scatter(temps, hats)
plt.show()