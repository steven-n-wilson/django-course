var playerOne = prompt("Player One enter your name, you will be BLUE: ")
var playerTwo = prompt("Player Two enter your name, you will be RED: ")

var countPlayer = 0;

var tdItems = $('.circle');
// console.log(tdItems);


var gameMatrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
];

var m = gameMatrix.length;
var n = gameMatrix[0].length;


function playerTurn() {
    if (countPlayer % 2 === 0) {
        $('#instructor').text()
        $('#instructor').text(playerTwo + " your turn! (RED)")
        countPlayer += 1
        return 1;
    }
    else {
        countPlayer += 1
        $('#instructor').text()
        $('#instructor').text(playerOne + " your turn! (BLUE)")
        return 2;
    }

}


// function that checks and adds player id to the matrix
function fillColumns(column, player) {
    for (var i = gameMatrix.length - 1; i >= 0; i--) {
        if (gameMatrix[i][column] === 0) {
            gameMatrix[i][column] = player;
            console.log(gameMatrix);
            break
        }
    }

}


function checkColors() {
    var count = 0;
    for (row in gameMatrix) {
        // console.log(gameMatrix[row])
        for (data in gameMatrix[row]) {
            // console.log("count " + count + " ID " + gameMatrix[row][data]);
            if (gameMatrix[row][data] === 1) {
                tdItems.eq(count).css('background-color', '#3471eb');
            }
            else if (gameMatrix[row][data] === 2) {
                tdItems.eq(count).css('background-color', '#f05646');
            }
            count += 1
        };
    }
}

function checkHorizontalWin(player) {
    // Check horizontal win
    for (row in gameMatrix) {
        var connectFour = 0;
        // console.log(gameMatrix[row]);
        for (id in gameMatrix[row]) {
            if (gameMatrix[row][id] === player) {
                connectFour++;
                // console.log(connectFour);
                if (connectFour === 4) {
                    $('#instructor').text()
                    $('#instructor').text("Player " + player + " Wins!")
                    console.log("Player " + player + "Win!");
                }
            }
            else {
                connectFour = 0;
            }
        }
    }
}

function checkVerticalWin(player) {
    // Check vertical win
    for (var j = gameMatrix.length - 1; j >= 0; j--) {
        var connectFour = 0;
        for (var i = gameMatrix.length - 1; i >= 0; i--) {
            if (gameMatrix[i][j] === player) {
                connectFour++
                // console.log(connectFour);
                if (connectFour === 4) {
                    $('#instructor').text()
                    $('#instructor').text("Player " + player + " Wins!")
                    console.log("Player " + player + "Win!");
                }
            }
            else {
                connectFour = 0;
            }
        }
    }
}

function checkDiagonalWin(player) {
    for (k = 0; k <= m - 1; k++) {
        var connectFour = 0;
        i = k;
        j = 0;
        while (i >= 0) {
            if (gameMatrix[i][j] === player) {
                connectFour++
                if (connectFour === 4) {
                    $('#instructor').text()
                    $('#instructor').text("Player " + player + " Wins!")
                    console.log("Player " + player + " Win!");
                }
            }
            else {
                connectFour = 0;
            }
            console.log(connectFour);
            // console.log(gameMatrix[i][j]);
            i = i - 1;
            j = j + 1;

        }
    }

    for (k = 1; k <= n - 1; k++) {
        i = m - 1;
        j = k;
        while (j <= n - 1) {
            if (gameMatrix[i][j] === player) {
                connectFour++

                if (connectFour === 4) {
                    $('#instructor').text()
                    $('#instructor').text("Player " + player + " Wins!")
                    console.log("Player " + player + "Win!");
                }
            }
            else {
                connectFour = 0;
            }
            console.log(connectFour);
            // console.log(gameMatrix[i][j]);
            i = i - 1;
            j = j + 1;
        }
    }

}


function checkPlayerWin(player) {
    checkHorizontalWin(player);
    checkVerticalWin(player);
    checkDiagonalWin(player)
}


function fillBoard(event) {
    fillColumns(event.data.column, playerTurn());
    checkColors();
    checkPlayerWin(1)
    checkPlayerWin(2)
}




$(".column0").on("click", { column: 0 }, fillBoard);
$(".column1").on("click", { column: 1 }, fillBoard);
$(".column2").on("click", { column: 2 }, fillBoard);
$(".column3").on("click", { column: 3 }, fillBoard);
$(".column4").on("click", { column: 4 }, fillBoard);
$(".column5").on("click", { column: 5 }, fillBoard);
$(".column6").on("click", { column: 6 }, fillBoard);



