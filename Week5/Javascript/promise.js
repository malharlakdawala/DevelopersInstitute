//try catch
// console.log('before')
//
// const a = 1
// try {
//     a = 2
// } catch (err) {
//     console.log(err)
//
// }
// console.log("after")

// const p = new Promise((resolve, reject) => {
//     if (false) {
//         resolve("Hello world")
//     } else {
//         reject("error")
//     }
// })
// console.log("malhar")
//
// p.then(result => {
//     console.log(result)
// })
//     .catch(reject => {
//         console.log(reject)
//     })
// console.log("lakdawala")

let compareToTen = num => {
    let p = new Promise((resolve, reject) => {
            if (num > 10) {
                resolve("Number is greater than 10")
            } else {
                reject("Number is less than 10")
            }
        }
    )
    return p
}
compareToTen(5).then(result => {
    console.log(result)
})
    .catch(reject => {
        console.log(reject)
    })
// console.log(compareToTen(12))