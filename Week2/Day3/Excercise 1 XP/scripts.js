//Exc1

// let colors = ["red", "blue", "pink", "green", "white"];
// for (let i = 0; i < colors.length; i++) {
//   console.log(`my ${i + 1} choice is color ${colors[i]}`);
// }
// let suffix = ["st", "nd", "rd", "th", "th"];
// for (let i = 0; i < colors.length; i++) {
//   console.log(`my ${i + 1}${[suffix[i]]} choice is color ${colors[i]}`);
// }

//Exc2
// let people = ["Greg", "Mary", "Devon", "James"];
// people.shift();
// console.log("1. " + people);
// people[people.length - 1] = "Jason";
// console.log("2. " + people);
// people.push("Malhar");
// console.log("3. " + people);
// console.log("4. ");
// for (let i = 0; i < people.length; i++) {
//   console.log(people[i]);
// }
// console.log("5. ");
// for (let i = 0; i < people.length; i++) {
//   console.log(people[i]);
//   if (people[i] == "Jason") {
//     break;
//   }
// }
// console.log("6. ");
// let m = people.indexOf("Mary");
// let n = people.indexOf("Malhar");

// let newarray = people.slice(m + 1, n);
// console.log(newarray);
// console.log("7. ");
// console.log(m);
// console.log("8. ");
// console.log(people.indexOf("foo"));
// console.log("9. ");
// let last = people[people.length - 1];
// console.log(last);

// //Exc 3
// let number = parseInt(prompt("Enter Number"));

// while (number < 10) {
//   number = parseInt(prompt("Enter Number greater than 10"));
// }

//Exc 4 Attendance
// let guestList = {
//   randy: "Germany",
//   karla: "France",
//   wendy: "Japan",
//   norman: "England",
//   sam: "Argentina",
// };
// let flag = 0;
// let namestr = prompt("Enter Name");
// for (let k in guestList) {
//   if (namestr === k) {
//     console.log(`i am ${k}, i am from ${guestList[k]}`);
//     flag = 1;
//   }
// }
// if (flag === 0) {
//   console.log("I am a guest");
// }

// //Exc 5 Family
// let family = {
//   father: "Divyang",
//   mother: "Divya",
//   sister: "Nirali",
//   wife: "Sonakshi",
// };
// for (let k in family) {
//   console.log(`in my family, ${k} is ${family[k]}`);
// }

//Exc 6
// let details = {
//   my: "name",
//   is: "Rudolf",
//   the: "raindeer",
// };
// console.log(
//   `${Object.keys(details)[0]} ${Object.values(details)[0]} ${
//     Object.keys(details)[1]
//   } ${Object.values(details)[1]} ${Object.keys(details)[2]} ${
//     Object.values(details)[2]
//   }`
// );

//Exc 7 Secret Group

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
let string = "";

for (let i = 0; i < names.length; i++) {
  string = string.concat(names[i][0]);
}

console.log(`name of secret society is ${string}`);
