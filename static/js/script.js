var dropdown_toggle = document.getElementById("dropdown-toggle");
var dropdown_menu = document.getElementById("dropdown-menu");
var dropdown_icon = document.getElementById("dropdown-icon");
var dropdown_toggle2 = document.getElementById("dropdown-toggle2");
var dropdown_menu2 = document.getElementById("dropdown-menu2");
var dropdown_icon2 = document.getElementById("dropdown-icon2");

dropdown_toggle2.addEventListener("click", function(){
    if(dropdown_menu2.style.display == "none"){
        dropdown_menu2.style.display = "block";
        dropdown_icon2.style.transform = "rotate(180deg)";
    }
    else{
        dropdown_menu2.style.display = "none";
        dropdown_icon2.style.transform = "rotate(0deg)";
    };
});

dropdown_toggle.addEventListener("click", function(){
    if(dropdown_menu.style.display == "none"){
        dropdown_menu.style.display = "block";
        dropdown_icon.style.transform = "rotate(180deg)";
    }
    else{
        dropdown_menu.style.display = "none";
        dropdown_icon.style.transform = "rotate(0deg)";
    };
});

function close_dropdown(event){
    if (!dropdown_toggle.contains(event.target) && !dropdown_menu.contains(event.target)) {
        dropdown_menu.style.display = "none";
        dropdown_icon.style.transform = "rotate(0deg)"
    }
}

window.addEventListener("click", close_dropdown);

function close_dropdown2(event){
    if (!dropdown_toggle2.contains(event.target) && !dropdown_menu2.contains(event.target)) {
        dropdown_menu2.style.display = "none";
        dropdown_icon2.style.transform = "rotate(0deg)"
    }
}

window.addEventListener("click", close_dropdown2);

