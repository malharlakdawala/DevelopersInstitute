let allBooks = [
  {
    title: " In Search of Lost Time",
    author: "Marcel Proust",
    imagelink:
      "https://d3i5mgdwi2ze58.cloudfront.net/7hqv6ddaqv363p4hadx6lymotow1",
    alreadyRead: true,
  },
  {
    title: " Ulysses",
    author: "James Joyce",
    imagelink:
      "https://d3i5mgdwi2ze58.cloudfront.net/f7nkbyqfsnrrlct3hs01jkrz2vdi",
    alreadyRead: false,
  },
  {
    title: "  Don Quixote",
    author: "Miguel de Cervantes",
    imagelink:
      "https://d3i5mgdwi2ze58.cloudfront.net/kedoaww5u33ka020nxmaxqscpgiz",
    alreadyRead: false,
  },
  {
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    imagelink:
      "https://d3i5mgdwi2ze58.cloudfront.net/m8sdet02cc7mdl8l6jow8cpl7co2",
    alreadyRead: true,
  },
];

let divClass = document.body.firstElementChild;
let newTable = document.createElement("table");
divClass.appendChild(newTable);
newTable.style.border = "1px solid black";

for (let j = 0; j < allBooks.length; j++) {
  let tableRow = document.createElement("tr");
  newTable.appendChild(tableRow);

  let tableData1 = document.createElement("td");
  tableRow.appendChild(tableData1);
  tableData1.textContent = allBooks[j]["title"];
  tableData1.style.border = "1px solid black";

  let tableData2 = document.createElement("td");
  tableRow.appendChild(tableData2);
  tableData2.textContent = allBooks[j]["author"];
  tableData2.style.border = "1px solid black";

  let tableData3 = document.createElement("td");
  tableRow.appendChild(tableData3);
  let img = document.createElement("img");
  img.src = allBooks[j]["imagelink"];
  tableData3.appendChild(img);
  //tableData3.textContent = allBooks[j]["imagelink"];
  tableData3.style.border = "1px solid black";
  img.setAttribute("width", "100px");

  let tableData4 = document.createElement("td");
  tableRow.appendChild(tableData4);
  tableData4.textContent = allBooks[j]["alreadyRead"];
  tableData4.style.border = "1px solid black";
  if (tableData4.textContent == "true") {
    tableData4.style.background = "green";
  } else {
    tableData4.style.background = "red";
  }
}

//2 start

// let table = document.body.firstElementChild;
// for (let i = 0; i < table.getElementsByTagName("tr").length; i++) {
//   table.getElementsByTagName("tr")[i].children[i].style.background = "red";
//   table.getElementsByTagName("tr")[
//     table.getElementsByTagName("tr").length - 1 - i
//   ].children[i].style.background = "red";
// }
