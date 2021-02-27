var firstName = prompt("Please enter your first name: ")
var lastName = prompt("Please enter your last name: ")
var age = prompt("Enter your age: ")
var height = prompt("Enter your height in cm: ")
var petName = prompt("Enter your pet's name: ")




if (firstName[0] === lastName[0]) {
    if (age > 20 && age < 30) {
        if (height > 169) {
            if (petName[petName.length - 1]) {
                console.log("Welcome to the spy team")
            }

        }

    }
}
else {
    console.log("Nothing to see here")
}

