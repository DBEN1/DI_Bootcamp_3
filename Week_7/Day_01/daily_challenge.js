// Define the planets and their properties
const solarSystem = [
    { name: 'Mercury', color: 'gray', moons: 0 },
    { name: 'Venus', color: 'yellow', moons: 0 },
    { name: 'Earth', color: 'blue', moons: 1 },
    { name: 'Mars', color: 'red', moons: 2 },
    { name: 'Jupiter', color: 'orange', moons: 79 },
    { name: 'Saturn', color: 'gold', moons: 82 },
    { name: 'Uranus', color: 'lightblue', moons: 27 },
    { name: 'Neptune', color: 'blue', moons: 14 }
];

// Get the section where we'll append the planets
const listPlanets = document.querySelector('.listPlanets');

// Create and append each planet and its moons
solarSystem.forEach(planet => {
    // Create planet div
    let planetDiv = document.createElement('div');
    planetDiv.className = 'planet';
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.innerText = planet.name;

    // Create moons for each planet
    for (let i = 0; i < planet.moons; i++) {
        let moonDiv = document.createElement('div');
        moonDiv.className = 'moon';
        
        // Position the moons around the planet using some basic trigonometry
        let angle = (i * 360) / planet.moons; // Distribute moons evenly in a circle
        let x = 70 * Math.cos(angle * (Math.PI / 180));
        let y = 70 * Math.sin(angle * (Math.PI / 180));
        
        moonDiv.style.left = (50 + x) + 'px';
        moonDiv.style.top = (50 + y) + 'px';

        planetDiv.appendChild(moonDiv);
    }

    // Append the planet (with its moons) to the section
    listPlanets.appendChild(planetDiv);
});
