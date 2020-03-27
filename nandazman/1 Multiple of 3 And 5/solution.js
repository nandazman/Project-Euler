function multiplesOf3and5(number) {
  let total = 0;
  while(number > 0) {
    number--;
    if(number % 3 || number % 5) {
      total += number;
    }
  }
  return total;
}
  
multiplesOf3and5(1000);
  