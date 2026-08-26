let x = 5;
let y = x;
y = 10;
console.log(x);
// stacks უფრო ჩქარია არ სჭირდება შენახვა და მოქმედების შემდეგ იშლება და ზომა სეზღუდულია
// heaps ნელია შედარებით მექანიკურად იმართება და მეტი მეხსიერება ჭირდება

const num = [1,2,3,4,5,6,7,8]
console.log(num.pop(2));
console.log(num.push(9));
console.log(num.shift());
console.log(num.unshift());
console.log(num.slice(4));
console.log(num.splice(2, 0));


stringi = "stringi da rame ra";
stringi.index("rame");

const cars =["range rover", "jaguar", "mercedes"];
let lastIndex = cars.lastIndexOf("jaguar");


let text = "wadjkabwdijku awpdohawdoipw erti ori sami";
let result = text.includes("erti");


function manualIndexOf(value, arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === value) {
            return i;
        }
    }
    return -1;
}

