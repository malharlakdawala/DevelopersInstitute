let n = parseInt(prompt("Enter no. "));
let flag = 0;
let i = 0;
while (i < n) {
  console.log(`${n - i - 1} bottles of beer on the wall`);
  console.log(`${n - i - 1} bottles of beer`);
  console.log(`Take ${i + 1} down, pass it around`);
  i = i + 1;
  n = n - i;
}
