// ex1 
function displayNumbersDivisible(divisor = 23) {
    let sum = 0;
    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            console.log(i);
            sum += i;
        }
    }
    console.log("Sum :", sum);
}

// Testing the function
displayNumbersDivisible();
displayNumbersDivisible(3);
displayNumbersDivisible(45);

// ex2 
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0;
    for (let item of shoppingList) {
        if (item in stock && stock[item] > 0) {
            total += prices[item];
            stock[item]--;  // Bonus: decrease the stock
        }
    }
    return total;
}

console.log(myBill());

// ex3
function changeEnough(itemPrice, amountOfChange) {
    const values = [0.25, 0.10, 0.05, 0.01];
    let totalChange = 0;

    for (let i = 0; i < amountOfChange.length; i++) {
        totalChange += values[i] * amountOfChange[i];
    }

    return totalChange >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2, 100, 0, 0]));
console.log(changeEnough(0.75, [0, 0, 20, 5]));
// ex 4
function hotelCost() {
    let nights;
    do {
        nights = parseInt(prompt("How many nights would you like to stay?"));
    } while (isNaN(nights));
    return nights * 140;
}

function planeRideCost() {
    let destination;
    do {
        destination = prompt("Where would you like to go?");
    } while (!destination || typeof destination !== "string");

    switch (destination) {
        case "London":
            return 183;
        case "Paris":
            return 220;
        default:
            return 300;
    }
}

function rentalCarCost() {
    let days;
    do {
        days = parseInt(prompt("How many days would you like to rent the car?"));
    } while (isNaN(days));

    let cost = days * 40;
    if (days > 10) {
        cost *= 0.95;  // 5% discount
    }
    return cost;
}

function totalVacationCost() {
    const hotel = hotelCost();
    const plane = planeRideCost();
    const car = rentalCarCost();

    alert(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}.`);
    return hotel + plane + car;
}

totalVacationCost();

// ex 5
// Retrieve the div and console.log it
let container = document.getElementById("container");
console.log(container);

// Change the name “Pete” to “Richard”
let lists = document.querySelectorAll(".list");
lists[0].children[1].textContent = "Richard";

// Delete the second <li> of the second <ul>
lists[1].removeChild(lists[1].children[1]);

// Change the name of the first <li> of each <ul> to your name
for (let list of lists) {
    list.firstElementChild.textContent = "YourName";
}

// Add a class called student_list to both of the <ul>'s
for (let list of lists) {
    list.classList.add("student_list");
}

// Add the classes university and attendance to the first <ul>
lists[0].classList.add("university", "attendance");

// Add a “light blue” background color and some padding to the <div>
container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

// Do not display the <li> that contains the text node “Dan”
let danLi = document.querySelector("li:contains('Dan')");
if (danLi) danLi.style.display = "none";

// Add a border to the <li> that contains the text node “Richard”
let richardLi = document.querySelector("li:contains('Richard')");
if (richardLi) richardLi.style.border = "1px solid black";

// Change the font size of the whole body
document.body.style.fontSize = "18px";

// Bonus
if (container.style.backgroundColor === "lightblue") {
    alert(`Hello ${lists[0].firstElementChild.textContent} and ${lists[1].firstElementChild.textContent}`);
}

// ex 6
// Change the value of the id attribute from navBar to socialNetworkNavigation
let navDiv = document.getElementById("navBar");
navDiv.setAttribute("id", "socialNetworkNavigation");

// Add a new <li> to the <ul>
let newLi = document.createElement("li");
let newText = document.createTextNode("Logout");
newLi.appendChild(newText);

let ul = navDiv.querySelector("ul");
ul.appendChild(newLi);

// Display the text of the first and last <li> elements
console.log(ul.firstElementChild.textContent);
console.log(ul.lastElementChild.textContent);

// ex7
let allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rowling",
        image: "https://example.com/harrypotter.jpg",
        alreadyRead: true
    },
    {
        title: "The Hobbit",
        author: "J.R.R. Tolkien",
        image: "https://example.com/thehobbit.jpg",
        alreadyRead: false
    }
];

let section = document.querySelector(".listBooks");

for (let book of allBooks) {
    let div = document.createElement("div");
    let titleAuthor = document.createElement("p");
    titleAuthor.textContent = `${book.title} written by ${book.author}`;
    if (book.alreadyRead) {
        titleAuthor.style.color = "red";
    }
    let img = document.createElement("img");
    img.src = book.image;
    img.width = 100;

    div.appendChild(titleAuthor);
    div.appendChild(img);
    section.appendChild(div);
}
