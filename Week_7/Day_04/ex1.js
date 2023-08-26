// ex 1 
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

colors.forEach((color, index) => {
    console.log(`${index + 1}# choice is ${color}.`);
});

// Check if at least one element of the array is equal to the value “Violet”
colors.includes("Violet") ? console.log("Yeah") : console.log("No...");

// ex 2 
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

colors.forEach((color, index) => {
    const order = index < 3 ? ordinal[index + 1] : ordinal[0];
    console.log(`${index + 1}${order} choice is ${color}.`);
});

//ex 3 
// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];
const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result); // ['bread', 'carrot', 'potato', 'chicken', 'apple', 'orange']

// ------2------
const country = "USA";
console.log([...country]); // ['U', 'S', 'A']

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray); // [undefined, undefined]

// ex 4
const users = [...]; // Given array

// 1.
const welcomeStudents = users.map(user => `Hello ${user.firstName}`);
console.log(welcomeStudents);

// 2.
const fullStackResidents = users.filter(user => user.role === 'Full Stack Resident');
console.log(fullStackResidents);

// 3. Bonus
const fullStackLastNames = fullStackResidents.map(user => user.lastName);
console.log(fullStackLastNames);

// ex 5 
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
const combined = epic.reduce((acc, word) => acc + ' ' + word);
console.log(combined);

// ex 6
const students = [...]; // Given array

// Filter students who passed the course
const passedStudents = students.filter(student => student.isPassed);
console.log(passedStudents);

// Bonus
passedStudents.forEach(student => {
    console.log(`Good job ${student.name}, you passed the course in ${student.course}`);
});

