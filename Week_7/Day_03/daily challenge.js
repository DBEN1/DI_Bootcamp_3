const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
};

const cloneGroceries = () => {
    // Copy the client variable
    let user = client;

    // Change the client variable to "Betty"
    client = "Betty";
    // The user variable will still be "John" because primitive types (like strings) are passed by value in JavaScript.

    // Create a variable named shopping that is equal to the groceries variable
    let shopping = groceries;

    // Change the value of the totalPrice key to 35$
    shopping.totalPrice = "35$";
    // The totalPrice in the groceries object will also change to "35$" because objects are passed by reference in JavaScript.

    // Change the value of the paid key to false
    shopping.other.paid = false;
    // The paid key in the groceries object will also change to false because objects are passed by reference in JavaScript.

    console.log("User:", user); // Expected output: "John"
    console.log("Client:", client); // Expected output: "Betty"
    console.log("Groceries Total Price:", groceries.totalPrice); // Expected output: "35$"
    console.log("Shopping Total Price:", shopping.totalPrice); // Expected output: "35$"
    console.log("Groceries Paid:", groceries.other.paid); // Expected output: false
    console.log("Shopping Paid:", shopping.other.paid); // Expected output: false
};

// Given data
let client = "John";
const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        paid: true,
        meansOfPayment: ["cash", "creditCard"]
    }
};

// Invoke the cloneGroceries function
cloneGroceries();
