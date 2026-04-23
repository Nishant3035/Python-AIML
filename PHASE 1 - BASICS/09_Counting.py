
def count(num):
    if num == 0:
        return 1
    digit = 0
    while num > 0 :
        digit+=1
        num//=10
    return digit    


num=int(input("Enter you numbers:"))
print(count(num)) 