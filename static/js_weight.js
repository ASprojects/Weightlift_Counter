function go_to_menu() {
    window.location.href = "http://127.0.0.1:5001/summary_menu"
    }
var find_summary_menu = document.getElementById("summary_menu")
find_summary_menu.addEventListener("click", go_to_menu);


function go_to_show_all() {
    window.location.href = "http://127.0.0.1:5001/show_all"
    }
var find_show_all = document.getElementById("show_all")
find_show_all.addEventListener("click", go_to_show_all);


function go_to_clear_data() {
    window.location.href = "http://127.0.0.1:5001/clear"
    }
var find_clear_data = document.getElementById("clear_data")
find_clear_data.addEventListener("click", go_to_clear_data);
