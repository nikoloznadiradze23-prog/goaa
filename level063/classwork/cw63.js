// let btn = document.querySelector("button")
// function handleSomething(e){
//     if(e.key == 'e' || e.key === 'E'){
//     console.log("pressed key")
//     }
// }

// let characterLimit = 200;
// function mcl (){
//     let cm = inputField.value;
//     let msl = currentMassage.lenght;
//     if(msl < cm){
//         sP.style.color = 'red'
//         sP.textContent = "limit:"
//     }
//     else{
//         sP.style.color = 'green'
//         sP.textContent = 'LIMIT MAX'
//     }
// }


// let button = document.querySelector("button")
// function press(){
//     console.log("pressed")
// }
// function up(){
//     console.log("off")
// }
// btn.addEventListener()


let images = [
    "https://static-cse.canva.com/blob/1210661/10SimplewaystoenhanceyourimageFeaturedImage1.jpg"
]


const nextbtn = document.getElementById(n);
const prevbtn = document.getElementById(p);
const image = document.querySelector('img');
image.src = image[1]
image.src = images[currentImageIndex]
nextbtn.onclick = function () {
    if (currentImageIndex > image.lenght - 1){
        currentImageIndex = 0
    }
    image.src = image[currentImageIndex]
    currentImageIndex++;
}
prevbtn.onclick = function(){
    if(currentImageIndex = image.lenght - 1){
        currentImageIndex = 0
    }
    image.src = image[currentImageIndex]
    currentImageIndex++;
}