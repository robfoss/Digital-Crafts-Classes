// JavaScript Document
let myArr = ['a', 'b', 'c', 'd', 'e'];
myArr.push('d')//adds items to back of list
let removedItem = myArr.pop();//removes items from back of list.

myArr.unshift('z');//add items to front of array
myArr.shift()//removes items from front of list.

//looping
for(let i = 0; i < myArr.length; i++){
	console.log(myArr[i])
}

//new was of looping through arrays
myArr.forEach(function(letter, idx){
	console.log(letter, idx)
})

//Create a list of letters at with at least 10 items.
//print the 4th item.
//concatinate the 6th and 3rd item and print the results.
//add 4 more letters one at a time to the end of the array.
//remove the first item of the array.
//join all of the letters together and send the results to the console.
//(bonus) sort the letters!

const letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
let fourth = letters[3];
console.log(fourth);

let concat = `${letters[6]}${letter[3]}`;
console.log(concat);

letters.push('k')
letters.push('l')
letters.push('m')
letters.push('n')

letters.shift();

let joinedLetters = letters.join('');
console.log(joinedLetters);