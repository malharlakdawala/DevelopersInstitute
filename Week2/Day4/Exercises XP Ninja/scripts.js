//Exercise 3 : Is Palindrome?
function palindrome(str) {
  for (let i = 0; i < str.length; i++) {
    if (str[i] !== str[str.length - i - 1]) {
      return false;
    }
  }
  return true;
}

console.log(palindrome("343"));

// //Exercise 5: Unique Elements
// Write a JS function that takes an array and returns a new array with only unique elements.

// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]

function uniqueElement(ary) {
  let k = [];
  for (let i = 0; i < ary.length; i++) {
    if (ary[i] !== ary[i + 1]) {
      k.push(ary[i]);
    }
  }
  return k;
}

console.log(uniqueElement([1, 2, 3, 3, 3, 3, 4, 5]));
