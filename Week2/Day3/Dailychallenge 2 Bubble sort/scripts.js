const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];
let stringnumber = numbers.join("").toString();
console.log(stringnumber);

//Bonus part - Bubble sort
let newnumber = numbers;
for (let i = 0; i < newnumber.length; i++) {
  for (let j = 0; j < newnumber.length; j++) {
    if (newnumber[j] < newnumber[j + 1]) {
      n = newnumber[j];
      newnumber[j] = newnumber[j + 1];
      newnumber[j + 1] = n;
    }
  }
}
console.log(`sorted array is: ${newnumber}`);
