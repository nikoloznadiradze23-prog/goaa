const difficultySelect = document.getElementById("difjficulty");
const modeSelect = document.getElementById("mode");
const start = document.getElementById("start")
const pretest = document.getElementById("pretest")
const testdiv = document.getElementById("test")

function getWords(sentence) {
    const words = sentence.split(" ")
    return words
}

startBtn.addEventListener("click", () => {
    const allTest = tests[difficultySelect.value]

    const randomIndex = Math.floor(Math.random() * 9)
    
    const testObj = allTests[randomIndex];

    const sentence = testObj.text

    const words = getWords(sentence);

    const wordsDiv = document.createElement("div")

    for (let word of words) {
        const newSpan = document.createElement("div")
        newSpan.textContent = word
        wordsDiv.appendChild(newSpan)
    }

    const parent = pretest.parentNode;

    pretest.style.display = 'none'

    const testParagraph = document.createElement("p");

    testParagraph.textContext = testObj.text;
    testParagraph.parentElement = testDiv

    testdiv.appendChild(testParagraph)

})