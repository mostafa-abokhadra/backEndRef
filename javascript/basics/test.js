let a = 10; // 11, 12, 13
let b = "20";
let c = 80 // 81, 82
console.log((++a) + (+b++) + (+c++) - (+a++)); //11 + 21 + 80 - 12 //100
console.log(++a + -b + +c++ - -a++ + +a); 
console.log(--c + +b + --a * +b++ - +b * a + --a - +true) ;