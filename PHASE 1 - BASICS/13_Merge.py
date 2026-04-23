list1=[]
n1=int(input("Enter numbers for list1: "))
for i in range(n1):
    list1.append(int(input("Enter the values: ")))
list2=[]
n2=int(input("Enter numbers for list2: "))
for i in range(n2):
    list2.append(int(input("Enter the values: ")))

result=list1+list2

result.sort()
print(result)