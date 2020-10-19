// $$$ SINGLE BUTTONS $$$
function add_show_all_button() {
    new XMLHttpRequest();
    window.location.href = "http://127.0.0.1:5001/show_all"
    }
var show_all = document.getElementById("show_all")
show_all.addEventListener("click", add_show_all_button);


function add_clear_data_button() {
    new XMLHttpRequest();
    window.location.href = "http://127.0.0.1:5001/clear"
    }
var clear_data = document.getElementById("clear_data")
clear_data.addEventListener("click", add_clear_data_button);


// $$$ FUNCTIONAL BUTTONS (menu, calc) $$$
