const robots = [ /*... your robots array ...*/ ];

// Function to display all robots
function displayRobots(robotsToDisplay) {
    const container = document.getElementById('robotsContainer');
    container.innerHTML = ''; // Clear previous robots

    robotsToDisplay.forEach(robot => {
        const robotCard = document.createElement('div');
        robotCard.className = 'robot-card';

        robotCard.innerHTML = `
            <img src="${robot.image}" alt="${robot.name}" class="robot-image">
            <div class="robot-name">${robot.name}</div>
            <div>${robot.username}</div>
            <div>${robot.email}</div>
        `;

        container.appendChild(robotCard);
    });
}

// Initial display of all robots
displayRobots(robots);

// Search functionality
const searchBox = document.getElementById('searchBox');
searchBox.addEventListener('input', function() {
    const filteredRobots = robots.filter(robot => 
        robot.name.toLowerCase().includes(searchBox.value.toLowerCase())
    );
    displayRobots(filteredRobots);
});
