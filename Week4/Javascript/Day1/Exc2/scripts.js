// Exercise 1: Sum Elements
// let a = [5,7,5,7,98,7,2,6,8]
// let sum = 0
// a.forEach((item)=>{
//     sum=sum+item
// })
// console.log(sum)

// Exercise 2 : Remove Duplicates
// let a = [5,7,5,7,98,7,2,98,6,8,6,8]
// a.forEach((item,index)=>{
//     let temp = a[index];
//     for(i=0;i<a.length-i;i++){
//         console.log(i,item,index)
//         if(temp==a[index+1+i]){
//             console.log(index)
//             a.splice(index+1+i,1)
//         }
//     }
// })
// console.log(a)
// Exercise 3 : Remove Certain Values
// let a = [NaN, 0, 15, false, -22, '',undefined, 47, null]
// for(let i=0;i<a.length;i++){
//     if(isNaN(a[i]) || a[i] === 0 || a[i]=="" || a[i]==undefined){
//         a.splice(i,1);
//     }
// }
// filteredArr = a.filter(function (elem) {
//     return elem !== undefined;
//     return elem !== 0;
// });
// //a.filter(item => item !== undefined)
//
// console.log(filteredArr)
//
// Exercise 4 : Repeat Please !

// function repeat(str,num=1){
// let ans = ""
//     for(let i = 0; i < num; i++){
//         ans += `${str}`;
//     }
//     return ans;
// }
// console.log(repeat("ha",2))
// Exercise 4 : Turtle & Rabbit
const startLine = '     ||<- Start line';
let turtle = '🐢';
let rabbit = '🐇';
function countSpases(str){
    let counter = 0;
    for(char of str){
        if(char == " "){
            counter++;
        }
    }
    return counter;
}


console.log(startLine);
console.log(turtle.padStart(countSpases(startLine) + rabbit.length - 2, " "));
console.log(rabbit.padStart(countSpases(startLine) + turtle.length - 2, " "));

turtle = turtle.trim().padEnd(9, '=');
console.log(turtle);
