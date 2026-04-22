#Python Fundamentals:(Assignment-2)
#Question1
'''salary=int(input("Enter your salary:"))
if(salary<30000):
    tax=(salary*5)/100
    finalsal=salary - tax
    print("5% Tax",finalsal)
elif(salary>=30000 and salary<70000):
    tax=(salary*15)/100
    finalsal=salary - tax
    print("15% Tax", finalsal)
else:
    tax=(salary*25)/100
    finalsal=salary - tax
    print("25% Tax",finalsal)'''
#Question2
'''
def even(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)
    return(a,b)
print(even(7,23))'''


num=int(input("Enter the num:"))
digit=[]
while num>0:

    ans=(int(num%10))
    num//=10
    print(ans)