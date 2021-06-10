// Write a function that given a sorted array of page numbers, return a string representing a book index. Combine consecutive pages to create ranges.
// assume that all numbers are poisitive

// Example: [1,3,4,5,7,8,10,12] --> "1, 3-5, 7-8, 10, 12"




function bookIndex(arr){
    for (var i = 0; i < arr.lenghth - 1; i++){
        for (var j = i + 1; i < arr.lenghth; i++)
    }

console.log(bookIndex([1,3,4,5,6,7,8,10]))