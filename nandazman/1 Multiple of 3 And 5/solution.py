import math

def multiplesOf3and5(number):
  number = number - 1
  # sum = 1/2 n(n+1)
  # sum of 1,3,4,5, ... , n + 1
  # math.floor(number / 3) to get how many iteration (n)
  sumOfMultiple3 = 3 * math.floor(number / 3) * (math.floor(number / 3) + 1) / 2
  sumOfMultiple5 = 5 * math.floor(number / 5) * (math.floor(number / 5) + 1) / 2
  sumOfMultiple15 =  15 * math.floor(number / 15) * (math.floor(number / 15) + 1) / 2
  return sumOfMultiple3 + sumOfMultiple5 + sumOfMultiple15

  
print(multiplesOf3and5(10))
  