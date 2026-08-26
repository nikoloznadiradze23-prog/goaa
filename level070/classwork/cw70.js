let myArr = [1,2,3,4,5,8,9];

function isEven (num) {
    return num % 2 === 0;
}
let newArr = myArr.map(element => element **2)

let filteredArr = myArr.filter(isEven)

console.log(newArr)

// foreach
let highest = 0
myArr.forEach((num) => {
    if (num > highest) {
        highest = num
    }
})

// reduce
let total = myArr.reduce((preValue, currentValue) => {
    return preValue + currentValue;
})

console.log(total)
export default Accounts, {getAccountFullName};

import Accout from './user.js'
user1 - new Account("nika")
console.log