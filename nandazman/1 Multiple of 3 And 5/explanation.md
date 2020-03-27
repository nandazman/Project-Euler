Find sum of multiple 3 in n number

3 + 6 + 9 + 12 = 30
divide by 3
1 + 2 + 3 + 4 = 10 -> find formula for that
example -> n is 4

sum = (1 + (n - n)) + (1 + (n - n + 1)) + (1 + (n - 2))      + (1 + (n - 1))
sum = (1 + (n - 1)) + (1 + (n - 2))     + (1 + (n - n + 1))  + (1 + (n - n)) #write backward

2sum =  (2 + (n - 1)) + (2 + (n - 1))       + .... + (2 + (n - 1))      + (2 + (n - 1)) #sum
(2 + (n - 1)) -> repeat n times
2sum = n((2 + (n - 1)))
2sum = n(n + 1)
sum = n(n + 1) / 2

n = 4
sum = 4(4 + 1)/2
sum = 10

sum of multiple 3

3sum = 3n(n + 1)/2
3sum = 3*4(4 + 1)/2
3sum = 30