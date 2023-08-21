// ex 1 
// Retrieve the h1 and console.log it
let h1 = document.querySelector("article h1");
console.log(h1);

// Remove the last paragraph in the <article> tag
let lastParagraph = document.querySelector("article p:last-child");
lastParagraph.remove();

// Change the background color of the h2 to red, when it’s clicked on
let h2 = document.querySelector("article h2");
h2.addEventListener("click", function() {
    h2.style.backgroundColor = "red";
});

// Hide the h3 when it’s clicked on
let h3 = document.querySelector("article h3");
h3.addEventListener("click", function() {
    h3.style.display = "none";
});

// Make the text of all the paragraphs, bold when button is clicked
let button = document.createElement("button");
button.textContent = "Bold Text";
button.addEventListener("click", function() {
    let paragraphs = document.querySelectorAll("article p");
    paragraphs.forEach(p => p.style.fontWeight = "bold");
});
document.body.appendChild(button);

// BONUS
h1.addEventListener("mouseover", function() {
    h1.style.fontSize = Math.floor(Math.random() * 100) + "px";
});

let secondParagraph = document.querySelector("article p:nth-child(4)");
secondParagraph.style.transition = "opacity 1s";
secondParagraph.addEventListener("mouseover", function() {
    secondParagraph.style.opacity = 0;
});

// ex2 
let form = document.querySelector("form");
console.log(form);

let fname = document.getElementById("fname");
let lname = document.getElementById("lname");
console.log(fname, lname);

let firstnameInputs = document.getElementsByName("firstname");
let lastnameInputs = document.getElementsByName("lastname");
console.log(firstnameInputs, lastnameInputs);

form.addEventListener("submit", function(event) {
    event.preventDefault();
    if (fname.value && lname.value) {
        let ul = document.querySelector(".usersAnswer");
        let li1 = document.createElement("li");
        li1.textContent = fname.value;
        let li2 = document.createElement("li");
        li2.textContent = lname.value;
        ul.appendChild(li1);
        ul.appendChild(li2);
    }
});

// ex3 
let allBoldItems;

function getBoldItems() {
    allBoldItems = document.querySelectorAll("p strong");
}

function highlight() {
    allBoldItems.forEach(item => item.style.color = "blue");
}

function returnItemsToDefault() {
    allBoldItems.forEach(item => item.style.color = "black");
}

let paragraph = document.querySelector("p");
paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", returnItemsToDefault);
// ex 4 
document.getElementById("MyForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let radius = parseFloat(document.getElementById("radius").value);
    if (!isNaN(radius) && radius > 0) {
        let volume = (4/3) * Math.PI * Math.pow(radius, 3);
        document.getElementById("volume").value = volume.toFixed(2);
    }
});

// ex 5
let h1 = document.querySelector("h1");

h1.addEventListener("click", function() {
    h1.style.color = "green";
});

h1.addEventListener("mouseover", function() {
    h1.style.fontSize = "30px";
});

h1.addEventListener("mouseout", function() {
    h1.style.fontSize = "20px";
});

h1.addEventListener("dblclick", function() {
    h1.style.textDecoration = "underline";
});
