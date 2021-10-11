//Exc1

let x = 5;
let y = -12;

if (x > y) {
  console.log(`Greater number is: ${x}`);
} else {
  console.log(`Greater number is: ${y}`);
}

//Exercise 2: Chihuahua

let newDog = "Chihuahua";
console.log(`the number of letters in Chihuahua is: ${newDog.length}`);
console.log(`the uppercase of Chihuahua is: ${newDog.toUpperCase()}`);
console.log(`the lowercase of Chihuahua is: ${newDog.toLowerCase()}`);

if (newDog === "Chihuahua") {
  console.log("I love Chihuahuas, it’s my favorite dog breed");
} else {
  console.log("I dont care, I prefer cats");
}

//Exercise 3: Even Or Odd
let num = parseInt(prompt("Enter number to check whether odd or even"));
if (num % 2 === 0) {
  console.log(`${num} is an even number `);
} else {
  console.log(`${num} is an odd number `);
}

//Exercise 4: Group Chat
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if (users.length < 1) {
  console.log(`No users are online`);
} else if (users.length === 1) {
  console.log(`${users[0]} is online`);
} else if (users.length === 2) {
  console.log(`${users[0]} and ${users[1]} are online`);
} else {
  console.log(`${users[0]}, ${users[1]} and ${users.length - 2} are online`);
}
