console.log("Exc 1:")
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.splice(0, 1);
console.log("1. After deleting banana the array is: " + fruits);
console.log("2. After sorting, the array is: " + fruits.sort());
fruits.push("kiwi");
console.log("3. After adding kiwi, the array is: " + fruits);
fruits.shift();
console.log("4. After removing apple, the array is: " + fruits);
fruits.reverse();
console.log("5. After reversing, the array is: " + fruits);
//Exc 2
console.log("Exc 2:")
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log("Value of nested array is: " + moreFruits[1][1][0]);