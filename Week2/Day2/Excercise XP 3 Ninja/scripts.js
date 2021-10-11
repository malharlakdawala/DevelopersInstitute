//Exercise 1 : Age Difference

const date1 = new Date("7/13/2000");
const date2 = new Date("12/15/2012");
const diffTime = Math.abs(2 * date2 - date1);

const newdat = new Date(diffTime).toLocaleString();

console.log(
  `The date where the elder one will be twice the younger one will be at  ${newdat}`
);
