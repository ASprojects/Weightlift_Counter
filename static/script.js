// $$$ SINGLE BUTTONS $$$
function add_show_all_button() {
    new XMLHttpRequest();
    document.getElementById("show_all")
    window.location.href = "http://127.0.0.1:5001/show_all"
}

show_all.addEventListener("click", add_show_all_button);