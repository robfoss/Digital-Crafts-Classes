// JavaScript Document
function funcName() {
	return 'I have returned'
}


let message = funcName() + ' and I like it a lot.';
console.log(message)

function myName(name) {
	return `${name} is here and I like it a lot.`
}

function foo(bar1, bar2, bar3) {
	if(!bar3) bar3 = 10;
	return bar1 + bar2 + bar3
}

console.log(foo(1, 5));

const myFunc = function(someArg) {
	console.log("I'm a annonymous function")
}

