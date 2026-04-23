nums=[4, -2, 7, 3, -5, 1]
count=0
totalsum=0
for i in nums:
    totalsum+=i
    count+=1

avg = totalsum/count
print(avg)