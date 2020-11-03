// JavaScript Document
let number = 10;
if(number % 2 != 0 && number % 3 != 0){}


let value = 0;
while(number > 0) {
	if(number % 2 != 0 && number % 3 != 0){
		value += number
	}
	number--
}

console.log(value)

const nextFunc = function(subFunc, aNumber){
	for(let i = 0; i <= aNumber; i++) {
		console.log(i)
	}
	subFunc();
}

nextFunc(function(){
	console.log('yee haw!')
}, 20)