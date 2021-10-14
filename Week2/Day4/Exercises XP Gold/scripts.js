// //Exercise 1 : Is_Blank

// function isBlank(str) {
//   if (str === "") {
//     return true;
//   } else {
//     return false;
//   }
// }
// console.log(isBlank("sfsda"));

// //Exercise 2 : Abbrev_name
// function abbrevName(name) {
//   name = name.split(" ");
//   let newstr = name[0] + " " + name[1][0] + ".";
//   return newstr;
// }

// console.log(abbrevName("Robin Singh"));

// //Exercise 4 : Omnipresent Value

// function isOmnipresent(arr, val) {
//   for (let i = 0; i < arr.length; i++) {
//     if (!arr[i].includes(val)) {
//       return false;
//     }
//   }
//   return true;
// }
// console.log(
//   isOmnipresent(
//     [
//       [1, 1],
//       [1, 3],
//       [5, 1],
//       [6, 1],
//     ],
//     6
//   )
// );
