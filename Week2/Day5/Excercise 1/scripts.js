function playTheGame() {
  let r = confirm("Ready to Play the game?");
  if (r == true) {
    alert("Lets Rollll!");
    checkInput();
  } else {
    alert("No problem, Goodbye!");
  }
}
function checkInput() {
  let userNumber = parseInt(prompt("Enter number between 0 and 10"));
  if (userNumber > 10) {
    alert("Sorry the number is higher than 10, Please try again");
    checkInput();
  } else if (isNaN(userNumber)) {
    alert("Sorry Not a number, Please try again");
    checkInput();
  } else {
    let computerNumber = Math.floor(Math.random() * 11);
    console.log(computerNumber);
    test(userNumber, computerNumber);
  }
}

function test(userNumber, computerNumber) {
  let count = 0;
  while (count != 3) {
    if (userNumber === computerNumber) {
      alert("Winner");
      return;
    }
    if (userNumber > computerNumber) {
      userNumber = parseInt(
        prompt("Your number is bigger then the computer’s, guess again")
      );
      count = count + 1;
    } else {
      userNumber = parseInt(
        prompt("Your number is smaller then the computer’s, guess again")
      );
      count = count + 1;
    }
  }
  alert("Out of chances, Bye");
  return;
}
