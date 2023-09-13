//ex1 
// products.js
const products = [
    { name: 'Laptop', price: 1000, category: 'Electronics' },
    { name: 'Shirt', price: 20, category: 'Apparel' },
    // ... other products
  ];
  module.exports = products;
  
  // shop.js
  const products = require('./products.js');
  
  function findProduct(productName) {
    return products.find(product => product.name === productName);
  }
  
  console.log(findProduct('Laptop'));
  console.log(findProduct('Shirt'));

  //ex2 
  // data.js
export const persons = [
    { name: 'John', age: 25, location: 'NY' },
    { name: 'Jane', age: 30, location: 'LA' },
    // ... other persons
  ];
  
  // app.js
  import { persons } from './data.js';
  
  function averageAge() {
    const totalAge = persons.reduce((acc, person) => acc + person.age, 0);
    return totalAge / persons.length;
  }
  
  console.log(averageAge());

  //ex3 
  // fileManager.js
const fs = require('fs');

function readFile(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

function writeFile(filePath, content) {
  fs.writeFileSync(filePath, content);
}

module.exports = { readFile, writeFile };

// app.js
const { readFile, writeFile } = require('./fileManager.js');

const content = readFile('Hello World.txt');
writeFile('Bye World.txt', 'Writing to the file');

//ex4 
// todo.js
export class TodoList {
    constructor() {
      this.tasks = [];
    }
    add(task) {
      this.tasks.push({ task, completed: false });
    }
    complete(taskName) {
      const task = this.tasks.find(t => t.task === taskName);
      if (task) task.completed = true;
    }
    list() {
      return this.tasks;
    }
  }
  
  // app.js
  import { TodoList } from './todo.js';
  
  const todo = new TodoList();
  todo.add('Buy milk');
  todo.add('Go to gym');
  todo.complete('Buy milk');
  console.log(todo.list());

//ex 5 
// math.js
module.exports = {
    add: (a, b) => a + b,
    multiply: (a, b) => a * b,
  };
  
  // app.js
  const _ = require('lodash');
  const math = require('./math.js');
  
  console.log(math.add(5, 3));
  console.log(math.multiply(5, 3));
  console.log(_.max([1, 2, 3, 4, 5]));
//ex 6
// app.js
const chalk = require('chalk');

console.log(chalk.blue('Hello world!'));
//ex 7 
// copy-file.js
const fs = require('fs');

const content = fs.readFileSync('source.txt', 'utf8');
fs.writeFileSync('destination.txt', content);

// read-directory.js
const fs = require('fs');

const files = fs.readdirSync('.');
console.log(files);
