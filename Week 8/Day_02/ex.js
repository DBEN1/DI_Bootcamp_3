//ex1
function compareToTen(num) {
    return new Promise((resolve, reject) => {
        if (num <= 10) {
            resolve('The number is less than or equal to 10');
        } else {
            reject('The number is greater than 10');
        }
    });
}
//ex2 
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('success');
    }, 4000);
});

// To test:
promise.then(result => console.log(result));

//ex3 
const resolvedPromise = Promise.resolve(3);
const rejectedPromise = Promise.reject('Boo!');

// To test:
resolvedPromise.then(value => console.log(value));  // Logs: 3
rejectedPromise.catch(error => console.log(error)); // Logs: Boo!
