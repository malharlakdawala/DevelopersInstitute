let userCart = {
  username: "Jhn",
  password: 123,
  isUserSignedIn: true,
  cart: {
    apple: 2,
    banana: 1,
    pear: 5,
  },
  prices: {
    apple: 0.5,
    banana: 0.8646466363,
    pear: 0.2,
  },
};

userCart["lastname"] = "Smith";
userCart["prices"]["pear"] = 0.3;
//let frt = prompt("add fruit");
//let newfrt = frt.toLowerCase();
//console.log(`the price of ${frt} is ${userCart["prices"][newfrt]}`);

userCart["prices"]["banana"] = userCart["prices"]["banana"].toFixed(2);
console.log(userCart["prices"]["banana"]);

if (userCart["isUserSignedIn"]) {
  console.log(
    `your username is ${userCart["username"]} and password is ${userCart["password"]}`
  );
} else {
  console.log("Please Sign In");
}

if (userCart["username"] == "John" && userCart["password"] == 1234) {
  console.log("You are signed In");
} else if (userCart["username"] == "John" || userCart["password"] == 1234) {
  console.log("Your credentials are wrong");
} else {
  console.log("You need to sign in");
}
