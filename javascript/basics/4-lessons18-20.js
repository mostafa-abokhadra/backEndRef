// if you tried to do some arithmetic operation between a string and a numbre 
//regardless the + operator that act as concatenation operator
// you will get an error of NaN (not a number)
console.log(10 - "string") // NaN 
console.log(10 * "string") // NaN 
// funny fact: typeof NaN is number :)
console.log(2 ** 4) // 16 which is 2 * 2 * 2 * 2
let num = 5;
console.log(++num) // 6
console.log(num++) // 6
console.log(num) // 7
// unary operator + and - is also used as a way of casting strings to number type
// if used with number will not do any thing
console.log(+"100") // 100
console.log(+"-100") // -100
console.log(+"100.50") // 100.50
console.log(+0xff) // 255
console.log(+false) // 0
console.log(+"mostafa") // NaN
console.log(+null) // 0
console.log(-null) // -0
console.log(-"100") // -100
console.log(-"-100") // 100
// or you can use number constructor to convert
console.log(Number("100")) // 100

// type coercion, type casting
let a = "10", b = 20, c = true
console.log(+a + b + c) // 31
console.log(20 - "10") // 10
console.log("10" - 20) // -10
console.log(20 + "10") // 2010
