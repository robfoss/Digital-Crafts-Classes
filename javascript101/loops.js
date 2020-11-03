// JavaScript Document


//while(expression) {
//	statement
//}

let i = 1;

while(i < 10) {
	console.log(i);
	i++;
}

let num = 10;
for(let i = 0; i < num; i++) {
	console.log(i)
}

let a = 20;
while (a < 100){
	if(a === 25) {
		break;
		console.log(a)
		a++
	}
}

for(let i = 0; i < 20; i++){
	if(!(i % 2 )) continue;//skipping even numbers.
	console.log(i)
}

//Using a while loop add numbers from 1 to 10.
//Using a for loop, count from a number of your choice to another number.
//Using a for loop, start with a number and then divide and replace that number by each number from 6 to 2.
//Using either type of loop add all of the numbers not divisible by 2 and 3 from 0 to a number of your choice.

let i = 1;
while(i < 10) {
	i += i
	i++
}

for(let i = 5; i < 15; i++){
	console.log(i)
}

let number = 36;
for(let i = 6; i >= 2; i--) {
	number /= i;
	console.log(number);	
}