let xhr = new XMLHttpRequest();
const getAPI = () => {
    xhr.open('GET', "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
    // xhr.responseType = 'json';
    xhr.send()

    xhr.onload = function () {
        if (xhr.status != 200) {
            console.log(`Error ${xhr.status}:${xhr.statusText}`);
        } else {
            console.log(`Done, got ${xhr.response.length} bytes`)
            let xml = JSON.parse(xhr.response)
            data = xml.data
            let root = document.getElementById('root')
            // for (let i = 0; i < xml["data"].length; i++) {
            //     // console.log(xml["data"][0]["rating"])
            //     let div = document.createElement('div');
            //     let h2 = document.createElement('h2');
            //     // let h4 = document.createElement('h4');
            //     // console.log(xml["data"][i]["bitly_url"])
            //     console.log(xml.data[i].bitly_url)
            //     let n = xml["data"][i]["bitly_url"]
            //     h2.innerText = n
            //     div.appendChild(h2)
            //     root.appendChild(div)

            data.forEach(item => {
                let div = document.createElement('div');
                let img = document.createElement('img');
                img.setAttribute('src', item.images.fixed_height.url);
                div.appendChild(img);
                root.appendChild(div);

            });

        }
    }
}

xhr.onerror = function () {
    console.log("Request Failed")
}


// below 3 are same

// function getAPI {
//
// }
//
// const getAPI = function () {
//
// }
//
// const getAPI = () => {
//
// }