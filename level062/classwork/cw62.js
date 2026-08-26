function OS(){
    let username = "name";
    function IS(){
        username = "NAME"
        console.log(username)
    }
    console.log(username)
    IS()
}
OS()

function OS(){
    let username = "name"
    function IS(){
        for (let i = 0; i < 10; i++){
            username = username.toLocaleLowerCase()
        }
    }
    IS()
    console.log(username)
}

setTimeout(greet, 5000)
function greet(username){
    console.log('welcome ${username}')
}


let count = 0;
function counter(){
    count++;
    console.log(count)
    if(count >= 10)
        clearInterval(counterInterval)
}
const counterInterval = setInterval(counter, 5000)