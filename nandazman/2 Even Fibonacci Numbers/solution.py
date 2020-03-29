def fiboEvenSum(n):
  total = 0

  num1 = 1
  num2 = 1

  while num2 < n:
    num2 = num1 + num2
    num1 = num2 - num1

    if num2 % 2 == 0:
      total = total + num2
  
  return total

print(fiboEvenSum(4000000))