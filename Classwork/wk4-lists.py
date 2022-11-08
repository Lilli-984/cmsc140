import random
import math

my_classes = ["CMSC140", "ANTH110", "MATH230"]

my_classes[0] = "Advanced Sleeping"

rand_numbers = []
for _ in range(20):
    #rand_numbers = rand_numbers + [random.randint(0,100)]
    rand_numbers.append(random.randint(0,100))

new_list= []
for i in rand_numbers:
    new_list = new_list + [math.sqrt(i)]
print(rand_numbers)
print(new_list)

sqrt()