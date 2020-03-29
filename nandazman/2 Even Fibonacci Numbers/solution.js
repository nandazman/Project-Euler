function fiboEvenSum(n) {
  // You can do it!
  let total = 0;
  let sum = 0;

  let num1 = 1;
  let num2 = 1;
  while(sum < n) {
    sum = num1 + num2;
    num1 = num2;
    num2 = sum;
    if(sum % 2 === 0) {
      total = total + sum;
    }
  }
  return total;
}

fiboEvenSum(10);
