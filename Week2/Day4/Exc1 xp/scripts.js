// //Exc1
// // function infoAboutMe() {
// //   console.log(`DUmmy sentence`);
// // }

// // infoAboutMe();

// //Exc2

// // function infoAboutPerson(personName, personAge, personFavoriteColor) {
// //   console.log(
// //     `your name is ${personName} age is ${personAge} and fav colour is ${personFavoriteColor}`
// //   );
// // }
// // infoAboutPerson("David", 45, "blue")
// // infoAboutPerson("Josh", 12, "yellow")

// //Exc3

// // function infoAboutPerson(
// //   personName,
// //   personAge,
// //   personFavoriteColor,
// //   personHobbies
// // ) {
// //   console.log(
// //     `your name is ${personName} age is ${personAge} and fav colour is ${personFavoriteColor}. Hobbies are `
// //   );
// //   for (let i in personHobbies) {
// //     console.log(personHobbies[i]);
// //   }
// // }

// // infoAboutPerson("David", 45, "blue", ["tennis", "painting"]);
// // infoAboutPerson("Josh", 12, "yellow", [
// //   "videoGame",
// //   "hanging out with friends",
// //   "playing cards",
// // ]);

// //Exercise 2 : Keyless Car

// // function checkDriverAge(age) {
// //   if (age < 18) {
// //     console.log("Sorry, you are too young to drive this car. Powering off");
// //   } else if (age > 18) {
// //     console.log("You are old enough to drive, Powering On. Enjoy the ride!");
// //   } else {
// //     console.log(
// //       "Congratulations on your first year of driving. Enjoy the ride!"
// //     );
// //   }
// // }

// // checkDriverAge(18);

// //Exercise 3: Odd Or Even

// function checkNumber() {
//   for (i = 1; i < 101; i++) {
//     if (i % 2 == 0) {
//       console.log(`${i} is an even number`);
//     } else {
//       console.log(`${i} is an odd number`);
//     }
//   }
// }
// checkNumber();

//Exercise 4: Find The Numbers Divisible By 23

// function isDivisible(n) {
//   let sum = 0;
//   console.log(`all the number divisible by ${n} are`);

//   for (i = 1; i < 500; i++) {
//     if (i % n == 0) {
//       console.log(`${i}`);
//       sum += i;
//     }
//   }
//   console.log(`their sum is ${sum}`);
// }
// isDivisible(10);

//Exercise 5 : Amazon Shopping

// let amazonBasket = {
//   glasses: 1,
//   books: 2,
//   floss: 100,
// };

// function checkBasket() {
//   let n = prompt("Enter Item");

//   for (let i in amazonBasket) {
//     if (n == i) {
//       console.log("Item present");
//     }
//   }
// }
// checkBasket();

//Exercise 6 : What’s In My Wallet ?

// function changeEnough(amountInWallet, priceOfItem) {
//   let n =
//     0.25 * amountInWallet[0] +
//     0.1 * amountInWallet[1] +
//     0.05 * amountInWallet[2] +
//     0.01 * amountInWallet[3];

//   if (priceOfItem > n) {
//     console.log(true);
//   } else {
//     console.log(false);
//   }
// }
// changeEnough([2, 100, 0, 0], 14.11);
// changeEnough([0, 0, 20, 5], 0.75);

//Exercise 7 : Shopping List

// let stock = {
//   banana: 6,
//   apple: 0,
//   pear: 12,
//   orange: 32,
//   blueberry: 1,
// };

// let prices = {
//   banana: 4,
//   apple: 2,
//   pear: 1,
//   orange: 1.5,
//   blueberry: 10,
// };

// function myBill() {
//   let sum = 0;
//   for (let i in shoppingList) {
//     if (stock[shoppingList[i]] > 0) {
//       sum = sum + prices[shoppingList[i]];
//       stock[shoppingList[i]] -= 1;
//       console.log(
//         `the updated quantity after billing of ${shoppingList[i]} is ${
//           stock[shoppingList[i]]
//         }`
//       );
//     }
//   }
//   console.log(`Total bill is ${sum}`);
// }

// let shoppingList = ["banana", "orange", "apple"];
// myBill();

//Exercise 8 : Tips

// function tip() {
//   let n = parseInt(prompt("Enter Amount"));
//   if (n < 50) {
//     console.log(
//       `Your bill is ${n}, tip amount is ${
//         n * 0.2
//       } and total amount payable is ${n * 1.2}`
//     );
//   } else if (n >= 50 && n <= 200) {
//     console.log(
//       `Your bill is ${n}, tip amount is ${
//         n * 0.15
//       } and total amount payable is ${n * 1.15}`
//     );
//   } else if (n > 200) {
//     console.log(
//       `Your bill is ${n}, tip amount is ${
//         n * 0.1
//       } and total amount payable is ${n * 1.1}`
//     );
//   }
// }
// tip();

//Exercise 9 : Vacations Costs

// function hotelCost() {
//   let n = parseInt(prompt("Enter no. of nights"));
//   return n * 140;
// }
// console.log(hotelCost());

// function planeRideCost() {
//   let loc = prompt("Enter location");
//   if (loc == "London") {
//     return 183;
//   } else if (loc == "Paris") {
//     return 220;
//   } else {
//     return 300;
//   }
// }
// console.log(planeRideCost());

function rentalCarCost() {
  let n = parseInt(prompt("Enter no. of days car needed for rent"));
  if (n > 11) {
    return n * 40 * 0.05;
  } else {
    return n * 40;
  }
}
console.log(rentalCarCost());
