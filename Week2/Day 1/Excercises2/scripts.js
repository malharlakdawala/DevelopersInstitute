//Uncomment each section to run
//Exc 1
/*
console.log("Exc1")
let str1 = prompt("Enter string")
let nstr1 = str1.split(" ");
if (nstr1.indexOf("nemo") > -1) {
    let num = nstr1.indexOf("nemo") + 1;
    alert(num);
} else {
    alert("nemo not found")
}
//Exc 3
console.log("Exc3")
let str1 = prompt("Enter numbers");
let nstr1 = str1.split(",");
var total = 0;
console.log(nstr1)
for (var i in nstr1) {
    total += parseInt(nstr1[i]);
}
console.log(total);
*/
//Exc 4
console.log("Exc4")
//Exc 4
let num = parseInt(prompt("Enter number"));
let str = ["B", "o", "o", "m"];
if (num < 3) {
    str = ["b", "o", "o", "m"];
} else {
    for (let i = 0; i < num - 2; i++) {
        str.splice(1, 0, "o");
    }
}
if (num % 2 == 0) {
    str.push("!");
}
if (num % 5 == 0) {
    for (let i = 0; i < str.length; i++) {
        str[i] = str[i].toUpperCase();
    }
}
console.log(str.join(""));