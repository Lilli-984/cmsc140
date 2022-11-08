
print("Please enter a number to start from:")
start = int(input())
print("Please enter how much to count down by:")
difference = int(input())

print("Countdown:")
while start>=0:
    print(start)
    start -= difference
