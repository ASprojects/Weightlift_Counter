// $$$ SINGLE BUTTONS $$$
function go_to_menu() {
    window.location.href = "/summary_menu"
}
var find_summary_menu = document.getElementById("summary_menu");
find_summary_menu.addEventListener("click", go_to_menu);


function go_to_show_all() {
    window.location.href = "/show_all"
}
var find_show_all = document.getElementById("show_all");
find_show_all.addEventListener("click", go_to_show_all);


function go_to_clear_data() {
    window.location.href = "/clear"
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
            bodyparts_list.forEach(element => add_option(element, find_bodypart));
         };
    };
};

find_bodypart.addEventListener("click", get_bodypart_choice, {once: true});


function remove_options(remove_element) {
    var i, L = remove_element.options.length - 1;
    for(i = L; i >= 0; i--) {
        remove_element.remove(i);
    }
}


var find_exercise = document.getElementById("form_exercise");
function get_exercise_choice() {
    var bodypart_value = find_bodypart.value;
    remove_options(find_exercise);
    const Http = new XMLHttpRequest();
    const url=`/exercise?bodypart_var=${bodypart_value}`;   //wysyła zmienną bodypart_value pod nazwą bodypart_var na podstronę exercise
    Http.open("POST", url);
    Http.send();
    Http.onreadystatechange = (e) => {
         if(Http.readyState === 4){
            var exercises_list = Http.responseText.split(';');
            exercises_list.forEach(element => add_option(element, find_exercise));
         };
    };
};

find_bodypart.addEventListener("change", get_exercise_choice);


// $$$ CALCULATE $$$
//####################################
//### UNDONE, PLEASE WAIT, WORKING ###
//####################################
var find_add_new_stats = document.getElementById("add_new_stats")
function get_new_stats() {
    var choice_dict = {
        bodypart_value : find_bodypart.value,
        exercise_value : find_exercise.value,
        series_value : document.getElementById("form_series").value,
        reps_value : document.getElementById("form_reps").value,
        weight_value : document.getElementById("form_weight").value,
    };
    console.log(choice_dict)
    const request = new Request(`/exercise`, {method: 'POST', body: 'choice_dict'})
    const url = request.url;
    const method = request.method;
    const credentials = request.credentials;
    const bodyUsed = request.bodyUsed;
    fetch(request)
        .then(response => {
            if (response.status === 200) {
                return response.json();
            } else {
            throw new Error('Something went wrong on api server!');
            }
        })
        .then(response => {
            console.debug(response);
            // ...
        }).catch(error => {
            console.error(error);
        });
};

find_add_new_stats.addEventListener("click", get_new_stats);
//####################################
//######   UNDER CONSTRUCTION   ######
//####################################
