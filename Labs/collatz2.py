print("Enter a start:")
start = int(input())
print("Enter an end")
end = int(input())
longest = 0
length = 0
for x in range(start,(end+1)):
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
print("Longest Chain is from:", longest)
print ("Length of chain: ",length)
