def countone(n):
    count = 0
    while(n):
        count+=1
        n &= (n-1)
    return count
def countFlips (a,b):
    return countone(a^b)
a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
print(countFlips(a, b))

