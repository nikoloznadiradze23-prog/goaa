const person ={
    username: "name",
    occupation: "coding",
    interests: ["gaming"],

    get header(){
        return `${username} is ${this.occupation}`
    },
    set interests (value){
        this.interests.unshift(value)
    }
}
console.log(person.header)
person.interests = "ethical hacking";


class sq{
    constructor(){
        this.width = this.width;
        this.height = this.height;
    }
    get area(){
        return this.width * this.height
    }
    set area(ar){
        this.height = Math.sqrt(ar);
        this.width - this.height;
    }
}
