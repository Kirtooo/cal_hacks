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

    let addGroup = document.querySelector("#addGroup");
    addGroup.addEventListener("click", function () {
        let groups = document.createElement("courseGroup");
        groups.innerHTML = "<div class=\"Groups\">\n" +
            "            <div class=\"courseGroup\">\n" +
            "                <h2>Course Group 1</h2>\n" +
            "                <h4 id=\"semester1\">Semester Selected: </h4>\n" +
            "                <h4 id=\"courses\">Current Courses: </h4>\n" +
            "                <h4>Add Course Here!</h4>\n" +
            "                Subject: <input type=\"text\" id=\"inputSubject\"/><br>\n" +
            "                Course Number: <input type=\"text\" id=\"inputNumber\"><br>\n" +
            "                <button id = \"addCourse\">add course</button>\n" +
            "                <button id = \"deleteCourse\">delete course</button>\n" +
            "                <select id = \"semester\">\n" +
            "                    <option value=\"spring2023\">spring-2023</option>\n" +
            "                    <option value=\"fall2022\">fall-2022</option>\n" +
            "                </select>\n" +
            "                <button id = \"semesterSubmit\">Submit</button>\n" +
            "            </div>";
        groups.appendChild(groups);
    })
}

setListeners();


window.onload = function() {
    $(".createGroup").html("<div class=\"Groups\">\n" +
        "            <div class=\"courseGroup\">\n" +
        "                <h2>Course Group 1</h2>\n" +
        "                <h4 id=\"semester1\">Semester Selected: </h4>\n" +
        "                <h4 id=\"courses\">Current Courses: </h4>\n" +
        "                <h4>Add Course Here!</h4>\n" +
        "                Subject: <input type=\"text\" id=\"inputSubject\"/><br>\n" +
        "                Course Number: <input type=\"text\" id=\"inputNumber\"><br>\n" +
        "                <button id = \"addCourse\">add course</button>\n" +
        "                <button id = \"deleteCourse\">delete course</button>\n" +
        "                <select id = \"semester\">\n" +
        "                    <option value=\"spring2023\">spring-2023</option>\n" +
        "                    <option value=\"fall2022\">fall-2022</option>\n" +
        "                </select>\n" +
        "                <button id = \"semesterSubmit\">Submit</button>\n" +
        "            </div>");
}