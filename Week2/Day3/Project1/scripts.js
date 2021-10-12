let shopping = ["apple", "watermelon", "pear", "banana"];

for (let i = 0; i < shopping.length; i++) {
  shopping[i] = shopping[i].concat("s");
}
console.log(shopping);

let num = [34, 56, 67, 87];
let total = 0;
for (let i = 0; i < num.length; i++) {
  total = total + num[i];
}
console.log(total);
