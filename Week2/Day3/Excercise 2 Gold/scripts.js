// //exc1
// let building = {
//   numberLevels: 4,
//   numberOfAptByLevel: {
//     1: 3,
//     2: 4,
//     3: 9,
//     4: 2,
//   },
//   nameOfTenants: ["Sarah", "Dan", "David"],
//   numberOfRoomsAndRent: {
//     Sarah: [3, 990],
//     Dan: [4, 1000],
//     David: [1, 500],
//   },
// };

// console.log(building["numberLevels"]);
// console.log(building["numberOfAptByLevel"]["1"]);
// console.log(building["numberOfAptByLevel"]["3"]);
// console.log(building["nameOfTenants"][1]);
// let d = building["nameOfTenants"][1];
// console.log(building["numberOfRoomsAndRent"][d][0]);

// let sum =
//   building["numberOfRoomsAndRent"]["Sarah"][1] +
//   building["numberOfRoomsAndRent"]["David"][1];

// if (sum > building["numberOfRoomsAndRent"]["Dan"][1]) {
//   building["numberOfRoomsAndRent"]["Dan"][1] +=
//     building["numberOfRoomsAndRent"]["David"][1];
// }

// console.log(building["numberOfRoomsAndRent"]["Dan"][1]);

//exc2

let numbers = [123, 8409, 100053, 333333333, 7];

for (let k of numbers)
  if (k % 3 == 0) {
    console.log(k + " is divisible by 3");
  } else {
    console.log(k + " is NOT divisible by 3");
  }

//exc3 Playing With Numbers
let age = [20, 5, 12, 43, 98, 55];

let sum = 0;
for (let i of age) {
  sum += i;
}
console.log(sum);

let j = 0;
let max = 0;
while (j < age.length) {
  if (age[j] > max) {
    max = age[j];
  }
  j++;
}
console.log(`the maximum no. is ${max}`);
