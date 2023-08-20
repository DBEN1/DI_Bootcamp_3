const people = ["Greg", "Mary", "Devon", "James"];

people.shift();
const indexJames = people.indexOf("James");
if (indexJames !== -1) {
    people[indexJames] = "Jason";
}
people.push("Dan");
console.log(people.indexOf("Mary"));
const copiedPeople = people.slice(1, 3);
#It returns -1 because "Foo" is not present in the array. The indexOf method returns -1 when the element is not found in the array.
const last = people[people.length - 1];
# Using a loop, iterate through the people array and console.log each person.
for (let person of people) {
    console.log(person);
}
# Using a loop, iterate through the people array and exit the loop after you console.log “Devon”.
for (let person of people) {
    console.log(person);
    if (person === "Devon") {
        break;
    }
}

#ex 2 
const colors = ["blue", "red", "green", "yellow", "purple"];
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}

#ex 3
let number = prompt("Enter a number:");

while (typeof number !== "number" || number < 10) {
    number = parseInt(prompt("Enter a number greater than or equal to 10:"));
}

# ex 4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
};

console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);
console.log(`${building.nameOfTenants[1]} has ${building.numberOfRoomsAndRent.dan[0]} rooms.`);

if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}

#ex 5
const family = {
    father: "John",
    mother: "Jane",
    son: "Jack",
    daughter: "Jill"
};

for (let member in family) {
    console.log(member);
}

for (let member in family) {
    console.log(family[member]);
}

#ex 6
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
};

let sentence = "";
for (let word in details) {
    sentence += `${word} ${details[word]} `;
}
console.log(sentence.trim());

#ex 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let secretName = "";

names.sort().forEach(name => {
    secretName += name[0];
});

console.log(secretName);
