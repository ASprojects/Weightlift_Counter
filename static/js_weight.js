// $$$ SINGLE BUTTONS $$$
function go_to_menu() {
    window.location.href = "http://127.0.0.1:5010/summary_menu"
    }
var find_summary_menu = document.getElementById("summary_menu");
find_summary_menu.addEventListener("click", go_to_menu);


function go_to_show_all() {
    window.location.href = "http://127.0.0.1:5010/show_all"
    }
var find_show_all = document.getElementById("show_all");
find_show_all.addEventListener("click", go_to_show_all);


function go_to_clear_data() {
    window.location.href = "http://127.0.0.1:5010/clear"
    }
var find_clear_data = document.getElementById("clear_data");
find_clear_data.addEventListener("click", go_to_clear_data);


// $$$ SELECT OPTION $$$
function add_option(option_name, button_name) {
    var option = document.createElement("option");
    option.text = option_name;
    option.value = option_name;
    button_name.add(option);
    };


var find_bodypart = document.getElementById("form_bodypart");

function get_bodypart_choice() {
    const Http = new XMLHttpRequest();
    const url='/bodypart';
    Http.open("POST", url);
    Http.send();
    Http.onreadystatechange = (e) => {
         if(Http.readyState === 4){
            var bodyparts_list = Http.responseText.split(';');
            console.log(bodyparts_list)
            bodyparts_list.forEach(element => add_option(element, find_bodypart));
            };
        };
    };

get_bodypart_choice();










//####################################
//### UNDONE, PLEASE WAIT, WORKING ###
//####################################
var find_exercise = document.getElementById("form_exercise");

function get_exercise_choice() {
    var exercise_value = find_bodypart.value;
    const Http = new XMLHttpRequest();
    const url='/exercise?bodypart=${exercise_value}';
    Http.open("POST", url);
    Http.send();
    Http.onreadystatechange = (e) => {
         if(Http.readyState === 4){
            var exercises_list = Http.responseText.split(';');
            console.log(exercises_list)
            exercises_list.forEach(element => add_option(element, find_exercise));
            };
        };
    };

find_bodypart.addEventListener("change", get_exercise_choice);
//####################################
//######   UNDER CONSTRUCTION   ######
//####################################