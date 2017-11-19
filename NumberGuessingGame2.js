var min = prompt("Enter a lower limit: ");
var max = prompt("Enter an upper limit: ");

var randomNumber = 8;

function game(randomNumber) {
    var guess = prompt("Guess a number: ");
    while (true) {
        if (guess === randomNumber) {
            break;
        }
        else if (guess < randomNumber) {
            guess = prompt("Guess a higher number: ");
        }
        else if (guess > randomNumber) {
            guess = prompt("Guess a lower number: ");
        }
    }
}

game(randomNumber)
document.write("My number was " + randomNumber);
