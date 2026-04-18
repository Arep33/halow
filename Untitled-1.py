print("-------------------------")
print("Masukan jumlah barisnya: ", end=" ")
n = int(input())
print("-------------------------")

a = [0] * (n)


for i in range(0, n - 1 + 1, 1):
    print("Masukan data ke-" , end="" + str(i + 1)+" "+":"+"  ")
    a[i] = int(input())

print()

print("Data sebelum urut: {", end="")
for i in range(n):
    print(a[i], end="")
    if i < n-1:
        print(", ",end="")
print("}")

print()

for j in range(0, n - 2 + 1, 1):
    for k in range(j + 1, n - 1 + 1, 1):
        if a[j] > a[k]:
            tukar = a[j]
            a[j] = a[k]
            a[k] = tukar
            
print("Data setelah urut: {", end="")

for i in range(0, n - 1 + 1, 1):
    print(str(a[i]), end="")
    if i < n - 1:
        print(", ", end="")
        
print("}")
