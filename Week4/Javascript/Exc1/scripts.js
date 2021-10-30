// function winBattle(){
//     return true;
// }
// function experiencePoints() {
//     if (winBattle()) {
//         return 10;
//     } else {
//         return 1;
//     }
// }
//
// console.log(experiencePoints())
// let experiencePoints = () => winBattle()? 10:1;
// console.log(experiencePoints())

//Exercise 3 : Colors
// let colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// console.log(colors.includes("Violet"))
//
// colors.forEach(function (item,index){
//     console.log(`${index+1}# Choice of colour is ${item}`)
// })

// colors.forEach(printData)
//
// function printData(item,index){
//         console.log(`${index+1}# Choice of colour is ${item}`)
// }
//Exercise 4 : Colors #2
// let color = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// let ordinal = ["th","st","nd","rd"];
//
// color.forEach(function (item,index){
//     if (index==0){
//         console.log(`${index+1}${ordinal[1]} choice is ${item}`)
//     } else if (index==1){
//         console.log(`${index+1}${ordinal[2]} choice is ${item}`)
//     } else if (index==2){
//         console.log(`${index+1}${ordinal[3]} choice is ${item}`)
//     }else{
//          console.log(`${index+1}${ordinal[0]} choice is ${item}`)
//     }
// })

//Exercise 5 : Is It A String ?
// function isString(str){
//     return (typeof str == "string"?true:false);
// }
// console.log(isString('hello'));
// console.log(isString([1, 2, 4, 0]));

//Exercise 6 : Bank Details
let bankAmount = 1000;
const vat = 0.17;
let details = ["+200", "-100", "+146", "+167", "-2900"];
details.forEach((item,index)=>{
    let element = Number(item)
    element<0?bankAmount=bankAmount+element+element*vat:bankAmount=bankAmount+element;
    console.log(bankAmount)
})
console.log(bankAmount)

