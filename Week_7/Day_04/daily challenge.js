const usernames = [];
gameInfo.forEach(user => {
    usernames.push(user.username + "!");
});
console.log(usernames); // ["john!", "becky!", "susy!", "tyson!"]

const winners = [];
gameInfo.forEach(user => {
    if (user.score > 5) {
        winners.push(user.username);
    }
});
console.log(winners); // ["becky", "susy"]


let totalScore = 0;
gameInfo.forEach(user => {
    totalScore += user.score;
});
console.log(totalScore); // 71
