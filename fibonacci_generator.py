#Fibonacci Generator infinite series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Fibonacci Generator
n = int(input("Enter number of terms: "))
x = 0
y = 1
print("Fibonacci Series:")
for i in range(n):
    print(x, end=" ")
    z = x + y
    x = y
    y = z