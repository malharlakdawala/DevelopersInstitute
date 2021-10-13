//Exc1
// function infoAboutMe() {
//   console.log(`DUmmy sentence`);
// }

// infoAboutMe();

//Exc2

// function infoAboutPerson(personName, personAge, personFavoriteColor) {
//   console.log(
//     `your name is ${personName} age is ${personAge} and fav colour is ${personFavoriteColor}`
//   );
// }
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

//Exc3

// function infoAboutPerson(
//   personName,
//   personAge,
//   personFavoriteColor,
//   personHobbies
// ) {
//   console.log(
//     `your name is ${personName} age is ${personAge} and fav colour is ${personFavoriteColor}. Hobbies are `
//   );
//   for (let i in personHobbies) {
//     console.log(personHobbies[i]);
//   }
// }

// infoAboutPerson("David", 45, "blue", ["tennis", "painting"]);
// infoAboutPerson("Josh", 12, "yellow", [
//   "videoGame",
//   "hanging out with friends",
//   "playing cards",
// ]);

//Exercise 2 : Keyless Car

function checkDriverAge(age) {
  if (age < 18) {
    console.log("Sorry, you are too young to drive this car. Powering off");
  } else if (age > 18) {
    console.log("You are old enough to drive, Powering On. Enjoy the ride!");
  } else {
    console.log(
      "Congratulations on your first year of driving. Enjoy the ride!"
    );
  }
}

checkDriverAge(18);
