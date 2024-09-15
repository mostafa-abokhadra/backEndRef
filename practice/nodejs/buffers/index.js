#!/usr/bin/node
const buffer = Buffer.from("mostafa-abokhadra");
console.log(buffer)
// output: <Buffer 6d 6f 73 74 61 66 61 2d 61 62 6f 6b 68 61 64 72 61>
console.log(typeof(buffer)) // object
console.log(buffer.toJSON())
/*
output:
    {
    type: 'Buffer',
    data: [
        109, 111, 115, 116,  97, 102,
        97,  45,  97,  98, 111, 107,
        104,  97, 100, 114,  97
    ]
    }
*/
console.log(typeof(buffer.toJSON())) // object
console.log(buffer.toString()) // mostafa-abokhadra
buffer.write("my name is mostafa abokhadra")
console.log(buffer.toString())
// output: my name is mostaf