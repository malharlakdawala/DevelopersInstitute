//Exercise 1 : The World Translator

// let input = prompt("Enter language").toLowerCase();

// switch (input) {
//   case "english":
//     console.log("Hello, the input is English");

//     break;
//   case "french":
//     console.log("Bonjour, the input is French");

//     break;
//   case "hindi":
//     console.log("Salaam, the input is Hindi");

//     break;
//   default:
//     console.log("01110011 01101111 01110010 01110010 01111001");
// }

//Exercise 3 : Verbing
let verb = prompt("Enter Verb");

if (verb.length >= 3 && verb.endsWith("ing") != 1) {
  verb = verb.concat("ing");
  console.log(verb);
} else if (verb.length >= 3 && verb.endsWith("ing")) {
  verb = verb.concat("ly");
  console.log(verb);
} else {
  console.log(verb);
}
