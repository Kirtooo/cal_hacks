let courseList = [];
let semester;

function setListeners() {
    let addButton = document.querySelector("#addCourse");
    addButton.addEventListener("click", function () {
        let inputSub = document.getElementById("inputSubject").value;
        let inputNum = document.getElementById("inputNumber").value;
        if (inputSub === "" || inputNum === "") {
            document.querySelector("#courses").innerText = "Lack of course Subject or Number!"
        } else if (!courseList.includes(inputSub + "-" + inputNum) && inputSub !== "") {
            courseList.push(inputSub + "-" + inputNum);
            document.querySelector("#courses").innerText = "Current Courses: " + courseList;
        }
        document.getElementById("inputSubject").value = "";
        document.getElementById("inputNumber").value = "";
    })

    let deleteButton = document.querySelector("#deleteCourse");
    deleteButton.addEventListener("click", function () {
        courseList.pop();
        document.querySelector("#courses").innerText = "Current Courses: " + courseList;
    })

    let semesterButton = document.querySelector("#semesterSubmit");
    semesterButton.addEventListener("click", function () {
        let id = document.querySelector("select").value;
        let name = $("#semester option:checked").text();
        semester = "name";
        document.querySelector("#semester1").innerText = "Semester Selected: " + name;
    })
}

setListeners();
