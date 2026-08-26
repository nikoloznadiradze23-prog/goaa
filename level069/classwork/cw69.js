// let myArr = [1,2,3,4,5,6,7,8]
// let mySet = new set(myArr)
// mySet.add(7)
// mySet.delete(5)
// console.log(mySet)
// console.log(mySet.has(1))
// mySet.clear()


// let myMap = new Map(
//     [
//         ["username", "nika"],
//         ["aleko", 22]
//     ]
// )
// console.log(myMap["username"])
// console.log(myMap)
// console.log(myMap.delete(22))
// console.log(myMap.has("user"))


// const a = () => {console.log("a")}
// const b = () => {console.log("a")}
// let testObjects = {
//     [a]: a,
//     [b]: b
// }
// console.log(testObjects)


// const promise = new Promise((resolve, reject) => {
//     let num = 7777777;
//     setTimeout(() => {

//     }, 2222)
//     if(num === 77777777){
//         resolve("chchchchhautare wyneturi?");
//     } else{
//         reject("manqqqqqqqqqqqana mmmmmmachukes var g g g aaa?");
//     }
// })
// console.log(promise)


function fetchinfo(){
    let promise = fetch("")
    promise
        .then(Response => response.json())
        .then(data => renderinfo(data))
        }