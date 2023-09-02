// ex1 : I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)
// ex2 
function displayStudentInfo(objUser){
    const {first, last} = objUser;
    return `Your full name is ${first} ${last}`;
}

//ex3
const usersArray = Object.entries(users);
const modifiedUsersArray = usersArray.map(([user, id]) => [user, id * 2]);

//ex4 : 'object'
//ex5 : //2
//ex6: 1 false, 2/ false 
//object2.number will output 4 because object2 references object1.
//object3.number : 4
//object4.number :   5 
class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

class Mamal extends Animal {
    sound(soundMade) {
        return `${soundMade} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`;
    }
}

const farmerCow = new Mamal('Lily', 'cow', 'brown and white');
console.log(farmerCow.sound('Moooo'));
