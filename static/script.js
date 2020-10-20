// $$$ SINGLE BUTTONS $$$
function add_goback_button() {
    window.location.href = "http://127.0.0.1:5001/"
    }
var go_back = document.getElementById("go_back")
go_back.addEventListener("click", add_goback_button);


function add_gotomenu_button() {
    window.location.href = "http://127.0.0.1:5001/summary_menu"
    }
var summary_menu = document.getElementById("summary_menu")
summary_menu.addEventListener("click", add_gotomenu_button);


function add_show_all_button() {
    window.location.href = "http://127.0.0.1:5001/show_all"
    }
var show_all = document.getElementById("show_all")
show_all.addEventListener("click", add_show_all_button);


function add_clear_data_button() {
    window.location.href = "http://127.0.0.1:5001/clear"
    }
var clear_data = document.getElementById("clear_data")
clear_data.addEventListener("click", add_clear_data_button);





// $$$ FUNCTIONAL BUTTONS (calc) $$$
