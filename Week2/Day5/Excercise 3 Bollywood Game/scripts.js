function checkInput() {
  //This function is for checking input bollywood name from player 1
  let str = prompt(
    "Player 1: Enter Name of the movie you want other person to guess"
  );
  if (str.length >= 8) {
    return str;
  } else {
    alert("Player 1: Length less than 8 characters, try again");
    checkInput();
  }
}

function playerTwoInput() {
  //This function is for checking input character from player 2

  let charp2 = prompt("Player 2: Enter the character you want to guess");
  if (charp2.length > 2) {
    prompt("Enter only 1 character");
    playerTwoInput();
  } else {
    return charp2;
  }
}

function bollywood() {
  let newstr = checkInput();
  console.log(newstr);
  let charp2in = "";
  let newstrp = "*".repeat(newstr.length);
  let newstrpary = [];
  console.log(`Player 2, the movie to guess for you is: ${newstrp}`);
  //Declaring 3 variables, 1 taking bollywood name as is, second taking character, 3rd is managing output with **
  for (let i = 3; i > -1; i--) {
    charp2in = playerTwoInput();
    if (newstr.includes(charp2in)) {
      //checking if character exisits in string?
      newstrpary = newstrp.split("");
      for (let j = 0; j < newstr.length - 1; j++) {
        newstrpary[newstr.indexOf(charp2in, j)] = charp2in;
        //replacing ** with character, wherever they find
      }
      newstrp = newstrpary.join("");
      console.log(
        `Congratulations, your character ${charp2in} is in the bollywood name, the new clue is ${newstrp}, total chances left are ${i}`
      );

      if (newstrp === newstr) {
        console.log(
          `WINNER, hurray you guessed the movie correctly with name ${newstrp}`
        );
        return;
      }
    } else {
      console.log(
        `${charp2in} is not in the bollywood name, the clue is ${newstrp} total chance left are ${i}`
      );
    }
  }
  console.log("Player 2: You are out of chances!");
}

bollywood();
/*
make function 1--> validation of input movie -- input string, length minimum 8

take input from player 2 -> send to function 2 for checking

make function 2 --> pass string and the character --> check character in string, 
and print the positions
*/

//   `Congratulations, your character ${charp2in} is in the bollywood name, the new clue is ${newstrp}, total chances left are ${i} `
// );
