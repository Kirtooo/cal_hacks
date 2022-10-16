
let courseList = [];


function buttonClicked(valueClicked) {
    if (isNaN(parseInt(valueClicked))) { //NaN means "Not a Number"
        //Hint: call a function we just created!
        makesSymbol(valueClicked);
    } else {
        //Hint: call a function we just created!
        makesNumber(valueClicked);
    }
    document.querySelector(".result-screen").innerText = strbuffer;
    // Hint: we need to change what number appears on the screen! to change html, one listener you could use is querySelector
}

function setListeners() {
    // document.querySelector(".buttons").addEventListener("click", function(event) {
    //     buttonClicked(event.target.innerText);
    // });
    //Hint: We want to select all buttons from html and make it so that something happens when you click on the buttons! querySelectorAll might be helpful
    let addButton = document.querySelector("#addCourse");
    addButton.addEventListener("click", function () {
        let inputVal = document.getElementById("inputCourse").value;
        if (!courseList.includes(inputVal) && inputVal !== "") {
            courseList.push(inputVal)
            document.getElementById("inputCourse").value = "";
            document.querySelector("#courses").innerText = "Current Courses: " + courseList;
        }
    })

    let deleteButton = document.querySelector("#deleteCourse");
    deleteButton.addEventListener("click", function () {
        courseList.pop();
        document.querySelector("#courses").innerText = "Current Courses: " + courseList;
    })
    //Hint: addEventListener might be useful.
    //Hint: event.target.innerText might be helpful. innerText return type is a string
}

//Make sure to call setListeners!!!
setListeners();
