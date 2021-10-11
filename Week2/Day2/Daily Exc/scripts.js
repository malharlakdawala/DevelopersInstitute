let sentence = "This dinner is not that bad ! You cook well";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
console.log(wordBad, wordNot);

if (wordBad > wordNot && wordBad > 0 && wordNot > 0) {
  let newsentence =
    sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);

  console.log(newsentence);
} else {
  console.log(`Original Sentence: ${sentence}`);
}
