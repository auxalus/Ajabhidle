def factorial(n):
    
    total = 1
    for i in range(1,n+1):
      total = total * i
    return total

num = int(input())
print(str(num) + "! = " + str(factorial(num)))