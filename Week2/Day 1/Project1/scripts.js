let addressNumber = 5;
let addressStreet = "Stuart St";
let country = "India";
let global_address = `I live at ${addressNumber}, ${addressStreet}, ${country}`;
console.log(global_address);
let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow'];
console.log(pets[1]);
pets[pets.length] = "horse";
console.log(pets[5]);
console.log(pets.length);
let newpet = prompt("Add a new pet");
pets.push(newpet);
console.log(pets);