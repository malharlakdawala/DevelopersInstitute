function createCalendar(year, month) {
  let monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  let divClass = document.body.firstElementChild;
  divClass.appendChild(document.createElement("h1")).textContent =
    "Calendar for " + monthNames[month - 1] + " " + year;

  let table = document.createElement("table");
  divClass.appendChild(table);

  let tableRow = document.createElement("tr");
  table.appendChild(tableRow);

  tableRow.appendChild(document.createElement("th")).textContent = "Sunday";
  tableRow.appendChild(document.createElement("th")).textContent = "Monday";
  tableRow.appendChild(document.createElement("th")).textContent = "Tuesday";
  tableRow.appendChild(document.createElement("th")).textContent = "Wednesday";
  tableRow.appendChild(document.createElement("th")).textContent = "Thursday";
  tableRow.appendChild(document.createElement("th")).textContent = "Friday";
  tableRow.appendChild(document.createElement("th")).textContent = "Saturday";

  let d = new Date(year, month - 1);
  console.log(d);
  let day = d.getDay();
  console.log(day);

  let lastDay = new Date(year, month, 0).getDate();
  console.log(lastDay);

  let count = -day + 1;
  for (let j = 0; j < 6; j++) {
    let week = table.appendChild(document.createElement("tr"));

    for (let i = 0; i < 7; i++) {
      let firstDay = document.createElement("td");
      week.appendChild(firstDay);
      if (count < 1 || count > lastDay) {
        firstDay.textContent = ".";
      } else {
        firstDay.textContent = count;
      }

      count += 1;
    }
  }
}

createCalendar(2021, 11);
