
with open("sample.txt","w") as f:
    for i in range(5):
        name = input("Enter the name:")
        f.write(name+"\n")

with open ("sample.txt", "r" ) as f:
    data=f.read()
    print(data)