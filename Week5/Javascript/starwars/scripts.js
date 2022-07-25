console.log("hello")
// random_text_div.innerText = "hello how are you";
// yellow_box.appendChild(random_text_div);
// yellow_box.appendChild(random_text_div)
// document.body.appendChild(random_text_div);
// const para = document.createElement("p");
// para.innerText = "This is a paragraph.";
//
// // Append to body:
// document.body.appendChild(para);


let getAPIData = async () => {
    url = `https://www.swapi.tech/api/people/${getRandomArbitrary(1, 83)}`
    result = await fetch(url)
    // console.log("result ", result)
    return await result.json()

}

function getRandomArbitrary(minimum, maximum) {
    return Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
}


let getData = async () => {
    let yellow_box = document.getElementsByClassName("second_box")[0];
    let checkDOM = document.getElementById("para");
    if (checkDOM != null) {
        checkDOM.remove()
    }
    const random_text_div = document.createElement("p");
    random_text_div.setAttribute("id","para")
    response = await getAPIData();

    random_text_div.innerText = `Name is ${response.result.properties.created}
    date is ${response.result.properties.created}`

    console.log("response", response.result.properties.created)
    yellow_box.appendChild(random_text_div)


    // info
}