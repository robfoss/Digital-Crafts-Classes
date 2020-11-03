//1. Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.

let moveZeroes = function(nums) {
    let count = 0;
    for (let i = 0; i < nums.length; i++){
        if(nums[i] !== 0){
            nums[count++] = nums[i];
        }
    }

    for (let i = count; i < nums.length; i++){
        nums[i] = 0;
    }
    return nums;    
};

Write a function that counts the number of times the number 7 occurs in a given integer
# without converting it to a string.

let count_seven = function(large_num, digit{
    magic_num = 7;
    count = 0;
    for(){}
}
