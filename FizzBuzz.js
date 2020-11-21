// prompt user for a number then store it in variable 'answer', wrap it in parseInt function to ensure it's a number

let answer = parseInt(prompt("Please enter the number you would like to FizzBuzz up to."));

for (let i = 1; i <= answer; i++) {
	if (i % 3 === 0) && (i % 5 === 0) {
		console.log("FizzBuzz");
	}else if (i % 3 === 0) {
		console.log("Fizz");
	} else {
		console.log(i);
	};
