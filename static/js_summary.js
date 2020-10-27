function go_back_to_homepage() {
    window.location.href = "/"
}
var find_go_back = document.getElementById("go_back");
find_go_back.addEventListener("click", go_back_to_homepage);


// $$$ SELECT OPTION $$$
function add_option(option_name, button_name) {
    var option = document.createElement("option");
    option.text = option_name;
    option.value = option_name;
    button_name.add(option);
};


var find_trening_date = document.getElementById("form_trening_date");

function get_trening_date_choice() {
    const Http = new XMLHttpRequest();
    const url='/trening_date';
    Http.open("POST", url);
    Http.send();
    Http.onreadystatechange = (e) => {
         if(Http.readyState === 4){
            var trening_datas_list = Http.responseText.split(';');
            trening_datas_list.forEach(element => add_option(element, find_trening_date));
        };
    };
};

get_trening_date_choice();


//####################################
//### UNDONE, PLEASE WAIT, WORKING ###
//####################################
function go_to_single_trening() {
    window.location.href = "/single_trening_summary"
    var single_trening = document.getElementById("form_trening_date");
    var test = single_trening.options[single_trening.selectedIndex].innerHTML;
    console.log(test)
}
var find_submit_date = document.getElementById("submit_date");
find_submit_date.addEventListener("click", go_to_single_trening);
//####################################
//######   UNDER CONSTRUCTION   ######
//####################################
