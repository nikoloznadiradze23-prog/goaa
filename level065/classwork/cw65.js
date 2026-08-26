// const form = document.querySelector("form")
// let accounts = []
// const userField = form.elements.username;
// const emailField = form.elements.email;
// const passwordField = form.elements.password;
// let loggedUser = "";
// function loadData (){
//     let saveData = localStorage.getItem("username")
//     id (savedData)
// }
// function savedData(){
//     localStorage.setItem("Username", user);
//     localStorage.setItem("email", email);
//     localStorage.setitem("Password", password)
// }
// function check(){
//     if (loggedUser){
//         document.body.removeChild(form)
//         let header = document.createElement("h1")
//         header.textContent = "welcome" + loggedUser
//         document.body.appendChild(header)
//     }
// }
// function loadInfo(){
//     let saveData = localStorage.getItem("Accounts")
//     accounts = saveData
// }
// loadInfo(accounts)
// function updateStorage(accounts, account){
//     localStorage.setItem("Accounts", JSON.stringify(accounts))
// }
// function handleSubmit (e, randomNumber){
//     e.preventDefault()
//     let username = userField.value;
//     let email = emailField.value;
//     let password = passwordField.value;
//     if(username.lenght <= 8){
//         alert("username invalid")
//         return
//     }
//     if(password.lenght <=6){
//         alert ("small pasword")
//         return
//     }
//     let account = {
//         username: username,
//         email: email,
//         password: password,
//     }
//     for(let i = 0; i < accounts.length; i++){
//         if (email === accounts[i].email) {
//             alert("acc alredy exsists")
//             return
//         }
//     }
//     loggedUser = username
//     account.push(account)
//     console.log(accounts)
//     alert("account created")
// }


let balance = 200
console.log(`balance ${balance}$`)
function varTest(){
    let x = 1;

    if(true){
        let x = 2
        console.log(X)
    }
    console.log(x)
    
}
const cars = ["range", "jaguar", "mersc", "aston","ferrari"]

for(let x of cars){
    console.log(index)
}
for(let index of cars){
    console.log(index)
}