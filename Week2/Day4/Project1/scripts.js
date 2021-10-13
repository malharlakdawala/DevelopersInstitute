function pet(nameOfPet, colorOfPet, breedOfPet) {
  console.log(
    `my pet is ${nameOfPet}, its color is ${colorOfPet}, and its breed is ${breedOfPet}`
  );
}

function aboutMe(age, favColors) {
  let twiceAge = age * 2;
  console.log(twiceAge);

  console.log(favColors);
}

pet("dog", "black", "Siberian");
aboutMe(25, ["red", "blue", "green"]);
