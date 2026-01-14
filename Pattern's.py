print("half Pyrimids of stars(*) :" )
n = int(input("Enter a number of rows: "))

# outer loops to handle number of rows
for i in range(n): 
    for j in range(i+1):
        print("*", end="")
    print()