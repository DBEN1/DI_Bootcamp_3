// Create a variable called sentence.
let sentence = "The movie is not that bad, I like it";

// Create a variable called wordNot.
let wordNot = sentence.indexOf("not");

// Create a variable called wordBad.
let wordBad = sentence.indexOf("bad");

// Check if "bad" comes after "not".
if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    sentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
}

console.log(sentence);

sentence = "This dinner is not that bad ! You cook well";
// Expected output: "This dinner is good ! You cook well"

sentence = "This movie is not so bad !";
// Expected output: "This movie is good !"

sentence = "This dinner is bad !";
// Expected output: "This dinner is bad !"
