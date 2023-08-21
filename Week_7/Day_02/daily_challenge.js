document.getElementById("libform").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get the values from the input fields
    let noun = document.getElementById("noun").value;
    let adjective = document.getElementById("adjective").value;
    let person = document.getElementById("person").value;
    let verb = document.getElementById("verb").value;
    let place = document.getElementById("place").value;

    // Check if any of the values are empty
    if (!noun || !adjective || !person || !verb || !place) {
        alert("Please fill in all fields!");
        return;
    }

    // Generate the story
    let story = `${person} was walking through ${place} when they saw a ${adjective} ${noun}. They decided to ${verb} it.`;
    document.getElementById("story").innerText = story;
});

// Bonus: Shuffle the story
let stories = [
    (noun, adjective, person, verb, place) => `${person} went to ${place} to buy a ${adjective} ${noun} and then decided to ${verb} it.`,
    (noun, adjective, person, verb, place) => `In ${place}, ${person} saw a ${noun} that was extremely ${adjective} and started to ${verb} it.`,
    (noun, adjective, person, verb, place) => `${person} ${verb} the ${adjective} ${noun} all around ${place}.`
];

document.getElementById("lib-button").addEventListener("click", function() {
    let noun = document.getElementById("noun").value;
    let adjective = document.getElementById("adjective").value;
    let person = document.getElementById("person").value;
    let verb = document.getElementById("verb").value;
    let place = document.getElementById("place").value;

    let randomStory = stories[Math.floor(Math.random() * stories.length)];
    document.getElementById("story").innerText = randomStory(noun, adjective, person, verb, place);
});
