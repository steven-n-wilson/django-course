/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

var num = 1;

// While Loop
while (num < 6) {
    console.log("hello")
    num += 1
}

// For Loop

for (var num = 1; num < 6; num++) {
    console.log("hello")
}




/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop

var i = 1;

while (i < 26) {
    if (i % 2 === 1) {
        console.log("Odd num: " + i)
    }
    i += 1
}


// METHOD TWO
// For Loop

for (var i = 1; i < 26; i++) {
    if (i % 2 === 1) {
        console.log("Odd num: " + i)
    }

}