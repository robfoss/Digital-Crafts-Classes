// JavaScript Document
let myObj = {
	name: 'Rob',
	age: 31,
	tall: true,
}

//accessing properties bracket and dot notation.
console.log(myObj['name'])
console.log(myObj.name)

myObj.name = 'Bobby';
myObj.gender = 'male';

console.log(myObj)

//looping objects
for(key in myObj){
	console.log(key, myObj[key])
}

//Create an object called 'spaceship'.
//give it the following keys with whatever values seems reasonable to you. speed,acceleration, passangers, fuel.
//Using the spaceship object above add a payload key after the object has been created. (just give it a number)
//Using the same object above, lower the amount of fuel by 1/3.
//loop through the object and give a message to the console like the one below for every property in the object.

const spaceship = {
	speed: 'very fast',
	acceleration: 'turbo boost',
	fuel: 100,
	passengers: 50
}

spaceship.payload = 50;
spaceship.fuel -= 1/3;

for(key in spaceship){
	console.log(`${key}: ${spaceship[key]}`);
}


//array of objects and iterating through array of objects
let people = [
	{
		name: 'Rob',
		age: 31,
	},
	
	{
		name: 'Margaret',
		age: 30,
	},
	
]

console.log(people[0].name + people[0].age + ' years old.')

people.forEach(function(person){
	console.log(`${person.name} is ${person.age} years old.`)
})