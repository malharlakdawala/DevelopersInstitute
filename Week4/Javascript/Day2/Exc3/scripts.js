// Exercise 1 : Menu
let menu = [
  {
    type : "starter",
    name : "Houmous with Pita"
  },
  {
    type : "starter",
    name : "Vegetable Soup with Houmous peas"
  },
  {
    type : "dessert",
    name : "Chocolate Cake"
  }
]

menu.forEach((item,index)=>{
  let a = item["type"].includes("dessert")?true:false
  console.log(a)

})

let vegetarian = ["vegetable", "houmous", "eggs", "vanilla", "potatoes" ]
vegetarian.push(vegetarian)

menu.forEach((item,index,menu1)=>{
 // menu1.push({"vegeterian": true})
  menu[index]["name"].includes(vegetarian.forEach((item)=>{item}))? menu1[index]["vegetarian"]=true :  menu1[index]["vegetarian"]=false
})
console.log(menu)