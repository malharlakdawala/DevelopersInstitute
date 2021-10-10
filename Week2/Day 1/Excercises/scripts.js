let me = ["my", "favorite", "color", "is", "blue"];
console.log("The concattenated array is: " + me.concat());
//Exc 2
console.log("Exc 2:")
//Exc 2
let str1 = "mix"
let str2 = "pod"
let newstr1 = str2[0] + str2[1] + str1.slice(2);
let newstr2 = str1[0] + str1[1] + str2.slice(2);
console.log(`${newstr1} ${newstr2}`);
//Exc 3
console.log("Exc 3:")
//Exc 3
let num1 = parseInt(prompt("Enter number 1: "));
let num2 = parseInt(prompt("Enter number 2: "));
sum = num1 + num2;
diff = num1 - num2;
prod = num1 * num2;
div = num1 / num2;
alert("the sum is " + sum + ", the difference is " + diff + ", the product is " + prod + ", division is " + div)