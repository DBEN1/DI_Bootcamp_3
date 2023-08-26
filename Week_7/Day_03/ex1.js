// ex 1 
// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

// #1.1
// Prediction: The alert will display "inside the funcOne function 3"

// #1.2
// Prediction: If 'a' is declared with 'const', there will be an error when trying to reassign its value inside the if block.

// #2
let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1
// Prediction: 
// First alert will display "inside the funcThree function 0"
// Second alert will display "inside the funcThree function 5"

// #2.2
// Prediction: If 'a' is declared with 'const', there will be an error when trying to reassign its value in funcTwo.

// #3
function funcFour() {
    window.a = "hello";
}

function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1
// Prediction: The alert will display "inside the funcFive function hello"

// #4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}

// #4.1
// Prediction: The alert will display "inside the funcSix function test"

// #4.2
// Prediction: Declaring 'a' with 'const' inside funcSix won't change the outcome.

// #5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// #5.1
// Prediction:
// First alert will display "in the if block 5"
// Second alert will display "outside of the if block 2"

// #5.2
// Prediction: Declaring 'a' with 'const' won't change the outcome as the two 'a' variables are in different scopes.

//ex 2 
const winBattle = () => true;
const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);

//ex 3 
const isString = value => typeof value === 'string';
console.log(isString('hello')); 
console.log(isString([1, 2, 4, 0]));

// ex 4 
const sum = (a, b) => a + b;

// ex 5 
// Function declaration
function kgToGrams(kg) {
    return kg * 1000;
}
console.log(kgToGrams(2));

// Function expression
const kgToGramsExpression = function(kg) {
    return kg * 1000;
}
console.log(kgToGramsExpression(2));

// One line comment: Function declaration can be hoisted and can be used before it's defined, while function expression cannot.

// Arrow function
const kgToGramsArrow = kg => kg * 1000;
console.log(kgToGramsArrow(2));

// ex 6 
(function(numChildren, partnerName, geoLocation, jobTitle) {
    document.body.innerHTML += `You will be a ${jobTitle} in ${geoLocation}, and married to ${partnerName} with ${numChildren} kids.`;
})(2, 'Alice', 'Paris', 'Developer');


// ex 7
(function(userName) {
    const navbar = document.getElementById('navbar');
    navbar.innerHTML += `<div>Welcome ${userName} <img src="path_to_profile_picture.jpg" alt="${userName}'s profile picture"></div>`;
})('John');

// ex 8 
// Part I
function makeJuice(size) {
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        document.body.innerHTML += `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}.`;
    }
    addIngredients('apple', 'banana', 'orange');
}
makeJuice('large');

// Part II
function makeJuice(size) {
    const ingredients = [];
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }
    function displayJuice() {
        document.body.innerHTML += `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
    }
    addIngredients('apple', 'banana', 'orange');
    addIngredients('grape', 'mango', 'pineapple');
    displayJuice();
}
makeJuice('medium');
