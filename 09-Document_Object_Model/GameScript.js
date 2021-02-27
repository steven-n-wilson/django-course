var boxes = document.querySelectorAll(".player")


boxes.forEach(changePlayer);

function changePlayer(box) {
    box.addEventListener("click", function () {

        if (box.textContent === "") {
            box.textContent = "X";
        }
        else if (box.textContent == "X") {
            box.textContent = "O";
        }
        else if (box.textContent == "O") {
            box.textContent = "";
        }
    })
}


function clearTable() {
    window.location.reload();
}

