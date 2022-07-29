// let fs = require('fs');
// fs.readFile('text.txt', 'utf-8', function (err, data) {
//     if (err) {
//         console.error(err)
//         return
//     }
//     console.log(data);
// });
//
// console.log("-----Restaurant Menu---------", '\n',);
//read file

users = "hello how are you, new file getting generated"

let fs = require('fs');
// fs.appendFile(`newfile.txt`,users, function (err, data) {
//     if (err) {
//         console.error(err)
//         return
//     }
//     console.log(users);
// });

fs.unlink(`newfile.txt`, function (err, data) {
    if (err) {
        console.error(err)
        return
    }
    console.log(users);
});



// fs.writeFile('newfile.txt', users, function (err, data) {
//     if (err) {
//         console.error(err)
//         return
//     }
//     console.log(users);
// });

