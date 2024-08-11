// strings
// you can put single quotes inside a string that is made using double quotes and vice verca without any requirement from you to use escape character
console.log("mostafa 'abokhadra'")
console.log('mostafa "abokhadra"')
// otherwise use escape character backslash'\'
console.log("mostafa \\	\"abokhadra\"") // mostafa \ "abokhadra"
console.log("mostafa \
			abokadra \
			10.") // in case if you want to fromat your code you can also use the
				  // the escape character.
console.log("mostafa\nabokhadra\n"); // to add new lines

let firstName = "mostafa", lastName = "abokhdara"
console.log(firstName + " " + lastName) //mostafa abokhadra
console.log(firstName, lastName) // mostafa abokhadra

// Template literal strings using backtick ``
console.log(`${firstName} "" // ${lastName}`); // you don't have to scape single \
                                              // or double quotess but you have to escape backslash operator
console.log(`${firstName}
${lastName}`); // this will actually print it in the output in new line
// so you can actually create a whole html element easily using backtick

let myElement = `
	<div>
		<h2>${firstName}<h2>
		<h3>${lastName}<h3>
	</div>
`;
document.write(myElement)