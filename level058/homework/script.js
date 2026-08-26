function Student(name, age, grade, active) {
    this.name = name
    this.age = age
    this.grade = grade
    this.active = active
    this.promote = function() {
    }
}
const maxo = new Student("maxo", 15, 9, true)
const artura = new Student("artura", 16, 10, true)
const gogita = new Student("gogita", 14, 8, false)
maxo.promote()
artura.promote()
gogita.promote()
console.log(maxo, artura, gogita)

class Book {
    constructor(title, author, year, available = true) {
    this.title = title;
    this.author = author;
    this.year = year;
    this.available = available;
    }
    toggleAvailability() {
    this.available = !this.available;
    }
}
const book1 = new Book("V for Vendetta", "alan moore", 1984, true);
const book2 = new Book("Fight Club", "Chuck Palahniuk", 1996, false) 


function Car(brand, model, year, mileage) {
    this.brand = brand
    this.model = model
    this.year = year
    this.mileage = mileage
    this.drive = function() {
    this.mileage += 100
    }
}
const r1 = new Car("range rover", "vogue", 2012, 15000)
const r2 = new Car("range rover", "sport", 2025, 9000)
const j1 = new Car("jaguar", "f type", 2018, 8000)
r1.drive()
r1.drive()
r2.drive()
r2.drive()
j1.drive()
j1.drive()
console.log(r1)
console.log(r2)
console.log(j1)
