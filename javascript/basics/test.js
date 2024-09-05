// let a = 10; // 11, 12, 13
// let b = "20";
// let c = 80 // 81, 82
// console.log((++a) + (+b++) + (+c++) - (+a++)); //11 + 21 + 80 - 12 //100
// console.log(++a + -b + +c++ - -a++ + +a); 
// console.log(--c + +b + --a * +b++ - +b * a + --a - +true) ;

let a = "Elzero Web School"

// output must be -> Zero
console.log(a.slice(2, 6).charAt(0).toUpperCase())

// output must be -> HHHHHHHH
console.log(a.charAt(a.indexOf('h')).toUpperCase().repeat(8))

// output must be -> //["Elzero"]
console.log(a.split(" ", 1))

// output must be -> // Elzero school
console.log(a.substr(0, 6) + a.substr(10))

// output must be first and last characters are small and the rest of the characters 
console.log(a[0].toLowerCase() + a.slice(1, -1).toUpperCase() + a.charAt(-1).toLowerCase())
