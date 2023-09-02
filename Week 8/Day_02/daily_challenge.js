// d1 : 
function makeAllCaps(words) {
    return new Promise((resolve, reject) => {
        if (words.every(word => typeof word === 'string')) {
            resolve(words.map(word => word.toUpperCase()));
        } else {
            reject('Not all items in the array are strings!');
        }
    });
}

function sortWords(words) {
    return new Promise((resolve, reject) => {
        if (words.length > 4) {
            resolve(words.sort());
        } else {
            reject('The array does not have more than 4 items!');
        }
    });
}

// d2 : 
function toJs() {
    return new Promise((resolve, reject) => {
        const morseJS = JSON.parse(morse);
        if (Object.keys(morseJS).length === 0) {
            reject('The Morse code object is empty!');
        } else {
            resolve(morseJS);
        }
    });
}

function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
        const userInput = prompt('Enter a word or sentence:').toLowerCase();
        const morseTranslation = [];

        for (let char of userInput) {
            if (morseJS[char]) {
                morseTranslation.push(morseJS[char]);
            } else {
                reject(`The character "${char}" cannot be translated to Morse code!`);
                return;
            }
        }

        resolve(morseTranslation);
    });
}

function joinWords(morseTranslation) {
    const morseString = morseTranslation.join('\n');
    // Displaying on the DOM can vary based on your setup. 
    // Here's a simple example using an alert:
    alert(morseString);
}

// Chaining the functions:
toJs()
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.error(error));

    