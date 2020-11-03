// JavaScript Document
//if statements
let a = 10, b = 20, c = 30;

if(a === 10) {
	console.log('a is equal to 10')
};

if (a === 10 && b === 10){
	console.log('a is equal to 10')
} else {
	console.log("One of these are not true.")
};

if (a < 10){
	console.log('a is less than 10')
} else if(a < 20) {
	console.log('a is less than 20')
} else {
	console.log('a is larger than 20')
};

//ternary statement

a == 10 ? 'yes' : 'no'

let result = a === 10 ? 'yes!' : 'Guess Again!';

//switch statement

let vaule = 1;

switch(vaule) {
	case 20:
		console.log('value is equal to 20')
		break;
	case 10:
		console.log('value is equal to 10')
		break;	
	case 50:
		console.log('value is equal to 50')
		break;	
	default:
		console.log('I really don\'t know.')
};


//Write a program that will declare a variable named "value".
//Have an if, if else, else statement that compares that value.
//using ternary.
//compare if one number is greater than another.
//set the value of a variable named 'result' to 'higher' if the first number is higher and lower if the first number is lower.
//Using switch.
//set a variable named = 'temp' and give it a value between -20 & 110.
//Have cases for sub 0, 30, 50, 75, 80, 90, and above.
//Have a hex color for each level going from blue to red.
//print out the color that represents the range.

const value = 'knowledge';

if(vaule === 'learning') {
	console.log(`${value} is power.`)
} else if (value === 'knowledge') {
	console.log(`${value} is power.`)
} else {
	console.log('Somthing ain\'t right.')
}

let num = 23;
let num2 = 24;
let goat = num < num2 ? 'Jumpman, Jumpman, Jumpman' : 'Kobe!';



let temp = 86;
switch(true) {
	case temp < 0:
		console.log('#0000FF')
		break;
	case temp < 30:
		console.log('#0080FF')
		break;
	case temp < 50:
		console.log('#00FF80')
		break;	
	case temp < 75:
		console.log('#FFFF00')
		break;	
	case temp < 80:
		console.log('#FF8000')
		break;	
	case temp < 90:
		console.log('#FF3333')
		break;	
	default:
		console.log('#FF3399')
				
}



					
					