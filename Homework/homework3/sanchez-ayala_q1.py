print("Enter a start:")
start = int(input())
print("Enter an end")
stop = int(input())
def longest_collatz(start, stop):
    longest = 0
    length = 0
    for x in range(start,(stop+1)):
        counter = 0
        num = x
        while x >1:
            if (x % 2) == 0:
                x = int(x/2)
                counter += 1
            else:
                x = int((x*3)+1)
                counter += 1
            if counter > length:
                length = counter
                longest = num
    return longest
a = longest_collatz(start,stop)
print(a)