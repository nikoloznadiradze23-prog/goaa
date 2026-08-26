// let nameFielld = "jeff epstein"
// let usr = {
//     [nameField]: "jeff epstein",
//     island: true,
//     balance: 99999999999999999999999999999999999999999999999,
//     deposit:function(){
//         this.balance += amount
//     }
// }
// usr.deposit(9999999999999999999);
// console.log(usr)


// let acc1 = {
//     user: "jeff epstein",
//     Island:true
// }
// let acc2 = {
//     user: "p diddy",
//     grapedBibber:true
// }
// let acc3 = {
//     user: "Donald trump",
//     kidsEaten: 999999999000000000,
// }
// console.log(acc1.Island);
// console.log(acc2.grapedBibber)
// console.log(acc3.kidsEat)


class acc {
    constructor(firstn, lastn, email, password, balance){
        this.firstn = firstn;
        this.lastn = lastn;
        this.balance = 200;
        acc.accounts += 1;
    }
    static log(){
        console.log('${acc.accounts}')
    }
}
let obj = new acc(john, doe)

deposit(){
    console.log(acc.accounts)
}
console.log(obj)