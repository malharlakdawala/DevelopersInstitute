// Exc1
// let sumNo = (a,b) => a+b;
// console.log(sumNo(5,6))
//
// Exc2
// const addTo = x => y => x + y;
// var addToTen = addTo(10);
// console.log(addToTen(3));

//
// let landscape = function()
// {
//  let result = "";
//  let flat = function(x)
//  {
//    for(let count = 0; count<x; count++)
//    {
//      result = result + "_";
//    }
//  }
//  let mountain = function(x)
//  {
//    result = result + "/"
//    for(let counter = 0; counter<x; counter++)
//    {
//      result = result + "'"
//    }
//    result = result + "\\"
//  }
//
// console.log((4));
// console.log(mountain(4));
// console.log(flat(4))
// return result;
// }
//
// console.log(landscape())
// Exercise 1 : Merge Words
// let mergeWords= (param) => " "+param;
// console.log(mergeWords("hi"))
// let a = mergeWords('There')('is')('no')('spoon.')();
// console.log(a)

let groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

//
// let foodStuff = {...groceries}
// foodStuff.totalPrice="35$"
// //foodStuff.other.payed=false
// console.log(groceries)
// console.log(foodStuff)

//json stringify method
let str = JSON.stringify(groceries)
console.log(str)
let foodStuff1= JSON.parse(str)
foodStuff1.other.payed=false
console.log(groceries)
console.log(foodStuff1)

//copying arrays - don't do direct =, use '...'
// let a = [1,2,3]
// let b=[...a] //try doing let b=a, and see results
// console.log(a)
// console.log(b)
// b[0]=10
// console.log(a)
// console.log(b)