let studentMap = new Map(
    [
        ["aliosha", 9],
        ["tite", 2],
        ["lamzo", 10],
    ]
)
console.log(studentMap["aliosha"])
console.log(studentMap.has["tite"])
console.log(studentMap.delete["lamzo"])


let mySet = new set(
    [1,2,3,4,5,6,7,8,9]
)
console.log(mySet.size)
console.log(mySet.add(10))
console.log(mySet.delete(3))


const users = new Map(
    [
        [1, "nika"],
        [2, "lamzo"],
        [3, "tite"],
        [4, "aliosha"]
]
);
console.log("user ids:");
for (let id of users.keys()) {
    console.log(id);
}
console.log("user names:");
for (let name of users.values()) {
    console.log(name);
}
console.log("user pairs:");
for (let entry of users.entries()) {
    console.log(entry);
}


const numSet = set(
    [1,2,3,4,5,6]
)
let sum = 0;
for (let num of numSet) {
    sum += num;
}
console.log(sum);


