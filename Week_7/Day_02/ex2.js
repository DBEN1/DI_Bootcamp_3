// ex 1 
// Part I
setTimeout(function() {
    alert("Hello World");
}, 2000);

// Part II
setTimeout(function() {
    let container = document.getElementById("container");
    let p = document.createElement("p");
    p.textContent = "Hello World";
    container.appendChild(p);
}, 2000);

// Part III
let interval;
let count = 0;

interval = setInterval(function() {
    let container = document.getElementById("container");
    let p = document.createElement("p");
    p.textContent = "Hello World";
    container.appendChild(p);
    count++;

    if (count >= 5) {
        clearInterval(interval);
    }
}, 2000);

document.getElementById("clear").addEventListener("click", function() {
    clearInterval(interval);
});

// ex 2 
function myMove() {
    let elem = document.getElementById("animate");
    let container = document.getElementById("container");
    let pos = 0;
    let widthOfContainer = container.offsetWidth;
    let widthOfElem = elem.offsetWidth;

    let id = setInterval(frame, 1);

    function frame() {
        if (pos >= widthOfContainer - widthOfElem) {
            clearInterval(id);
        } else {
            pos++;
            elem.style.left = pos + "px";
        }
    }
}
