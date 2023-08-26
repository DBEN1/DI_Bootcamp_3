function areAnagrams(str1, str2) {
    // Helper function to process and sort string
    function processAndSort(s) {
        return s.replace(/\s+/g, '').toLowerCase().split('').sort().join('');
    }

    return processAndSort(str1) === processAndSort(str2);
}

// Test cases
console.log(areAnagrams("Astronomer", "Moon starer")); // true
console.log(areAnagrams("School master", "The classroom")); // true
console.log(areAnagrams("The Morse Code", "Here come dots")); // true
console.log(areAnagrams("Hello", "World")); // false
